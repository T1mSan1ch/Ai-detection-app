import torch

from transformers import (
    AutoModelForImageClassification,
    AutoImageProcessor,
)

PATH = "t1msanswin-tiny-patch4-window7-224-Kontur-competition-52K"


class Inference:
    def __init__(self):
        self.model = AutoModelForImageClassification.from_pretrained(PATH)
        self.image_processor = AutoImageProcessor.from_pretrained(PATH)
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    def predict(self, image):
        encoding = self.image_processor(image.convert("RGB"), return_tensors="pt")

        outputs = self.model(**encoding)
        result = torch.nn.functional.softmax(outputs.logits, dim=-1).tolist()[0][0]
        return result



