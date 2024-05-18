from transformers import ( # type: ignore
    AutoModelForImageClassification,
    AutoImageProcessor,
    pipeline
)




DEFAULT_PATH = ''




class Predict:
    def __init__(self, model: Model, config: Config, device: int = 0):
        self.device = device
        self.repo_name = 't1msan/' + config.default_repo_name
        self.image_processor = AutoImageProcessor.from_pretrained(self.repo_name)
        self.model = AutoModelForImageClassification.from_pretrained(self.repo_name)
        self.pipe = pipeline('image-classification', model=self.repo_name, device=self.device)

    def set_device(self, device):
        self.device = device
        print(f"Вычисления производятся на {'GPU' if not self.device else 'CPU'}")

    def show_device(self):
        print(f"Вычисления производятся на {'GPU' if not self.device else 'CPU'}")

    def set_repo_name(self, new_repo_name):
        self.repo_name = new_repo_name
        self.image_processor = AutoImageProcessor.from_pretrained(self.repo_name)
        self.model = AutoModelForImageClassification.from_pretrained(self.repo_name)
        self.pipe = pipeline('image-classification', model=self.repo_name, device=self.device)
        print(f'Установлен новый репозиторий для загрузки предобученной модели. \n'
              f'Актуальный репозиторий: {self.repo_name}')

    def _data_preprocess(self, df: pd.DataFrame) -> tuple[pd.DataFrame, Dataset]:
        if df.empty:
            raise(Exception("Dataset is empty"))
        if 'id' not in df.columns:
            raise ValueError()
        else:
            df = df[['id']]
        if isinstance(df, pd.DataFrame):
            dataset_test = Dataset.from_pandas(df).cast_column("id", Image())
            return df, dataset_test

    def predict(self, dataset: pd.DataFrame) -> pd.DataFrame:

        df, dataset_test = self._data_preprocess(dataset)

        def check_fake_score(i):
            image = dataset_test[i]["id"]
            data = self.pipe(image)
            for item in data:
                if item['label'] == 'ai':
                    return item['score']

        df['target'] = df.index.to_series().apply(check_fake_score)

        return df