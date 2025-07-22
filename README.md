# 🛡️ Transformer Security Checker

This project demonstrates how to evaluate the robustness of transformer models (like BERT) against adversarial attacks using the `textattack` library.

## 📁 Structure

- `notebook/adversarial_demo.ipynb` — Interactive Jupyter Notebook walkthrough
- `scripts/run_attacks.py` — Scripted attack simulation
- `requirements.txt` — Install dependencies

## 🚀 Usage

1. Install dependencies:
```
pip install -r requirements.txt
```

2. Run attack demo:
```
python scripts/run_attacks.py
```

## 🧪 Tested Models
- BERT (`textattack/bert-base-uncased-imdb`)

## 📚 Dataset
- IMDB movie reviews (binary classification)

## 🔒 Goal
Showcase vulnerabilities in NLP models to raise awareness of robustness and AI security issues.
