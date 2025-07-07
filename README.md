# 🕵️‍♀️ Image Forgery Detection using ELA and CNN

This project detects whether an image is **real** or **tampered** using **Error Level Analysis (ELA)** and a **Convolutional Neural Network (CNN)**.

![Accuracy](https://img.shields.io/badge/Accuracy-93%25-brightgreen)
![License](https://img.shields.io/badge/License-MIT-blue)
![Made with Python](https://img.shields.io/badge/Made%20with-Python-yellow)

---

## 📌 Table of Contents

* [📖 Overview](#-overview)
* [📂 Dataset](#-dataset)
* [⚙️ Setup](#️-setup)
* [📁 Folder Structure](#-folder-structure)
* [▶️ How to Run](#️-how-to-run)
* [📈 Model Performance](#-model-performance)
* [✅ Results](#-results)
* [🙋 Contributors](#-contributors)
* [📜 License](#-license)

---

## 📖 Overview

This project is based on:

* 🖼️ **ELA (Error Level Analysis)** for image preprocessing
* 🧠 **CNN** for binary image classification (real vs tampered)

---

## 📂 Dataset

We use the **CASIA v2.0 Tampering Dataset**, which contains:

* 🟢 Real images: `/CASIA2/Au/`
* 🔴 Tampered images: `/CASIA2/Tp/`

📁 Additional test images can be added inside the `data/` folder.

---

## ⚙️ Setup

### 1. 🔁 Clone the repository

git clone https://github.com/MGaul6/image-forgery-detection.git
cd image-forgery-detection
```

### 2. 🐍 Create a virtual environment (optional)

python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3. 📦 Install dependencies
pip install -r requirements.txt
```

---

## 📁 Folder Structure

```
image-forgery-detection/

├── README.md

├── requirements.txt

├── model/

│   └── model_casia_run1.h5

├── data/

│   ├── sample_real.jpg

│   └── sample_fake.jpg

├── src/
│   ├── train_model.py

│   ├── inference.py

│   ├── utils.py

│   └── ela_converter.py

├── output/
│   ├── accuracy_loss_plot.png

│   └── confusion_matrix.png

└── notebook/

    └── image_forgery_detection.ipynb
```

---

## ▶️ How to Run

### 1. 🏋️ Train Model

python src/train_model.py
```

### 2. 🔍 Run Inference on a New Image

```bash
python src/inference.py --image data/sample_fake.jpg
```

---

## 📈 Model Performance

* ✅ **Validation Accuracy**: \~93%
* ⚙️ **Model**: CNN with two Conv2D layers + Dropout

📊 Plots saved in `output/`:

* Accuracy & Loss Curves
* Confusion Matrix

---

## ✅ Results

| Class | 🖼️ Sample       | 📊 Confidence |
| ----- | ---------------- | ------------- |
| Real  | sample\_real.jpg | 99.99%        |
| Fake  | sample\_fake.jpg | 98.45%        |

---

## 🙋 Contributors

* 👩‍💻 Mansi Gaul ([GitHub](https://github.com/MGaul6))

💡 Feel free to **fork** this repo, improve it, and submit a **pull request**! 💬

---

## 📜 License

MIT License. Feel free to use and share! ✨

---
