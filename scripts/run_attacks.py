from textattack.attack_recipes import TextFoolerJin2019
from textattack.datasets import HuggingFaceDataset
from textattack.models.wrappers import HuggingFaceModelWrapper
from transformers import AutoModelForSequenceClassification, AutoTokenizer

def main():
    print("[INFO] Loading pre-trained model and tokenizer...")
    model = AutoModelForSequenceClassification.from_pretrained("textattack/bert-base-uncased-imdb")
    tokenizer = AutoTokenizer.from_pretrained("textattack/bert-base-uncased-imdb")
    model_wrapper = HuggingFaceModelWrapper(model, tokenizer)

    print("[INFO] Loading IMDB test dataset...")
    dataset = HuggingFaceDataset("imdb", None, "test")

    print("[INFO] Running adversarial attack (TextFooler)...")
    attack = TextFoolerJin2019.build(model_wrapper)
    attack.attack_dataset(dataset, num_examples=1)

if __name__ == "__main__":
    main()
