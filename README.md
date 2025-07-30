# 🌿 Plant Disease Prediction Website

This project is a **Deep Learning-powered web application** designed to identify and classify diseases in plant leaves from uploaded images. By leveraging modern computer vision techniques, this tool helps farmers, researchers, and agricultural professionals diagnose plant health issues quickly and accurately.

> 🧪 This project is a research initiative under the **AWaDH Lab**, sponsored by **IIT Ropar**.

---

## 📌 Table of Contents

- [Features](#features)
- [Demo](#demo)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Model Details](#model-details)
- [Project Structure](#project-structure)
- [Acknowledgements](#acknowledgements)
- [License](#license)

---

## 🚀 Features

- 📷 Upload a plant leaf image via a web interface.
- 🤖 Get real-time disease prediction using a trained deep learning model.
- 📊 View confidence scores for each disease class.
- 💡 Clean, user-friendly interface for all levels of users.
- 🔬 Designed for both academic and practical agricultural use.

---

## 🛠️ Tech Stack

- **Frontend**: HTML5, CSS3, Bootstrap, JavaScript
- **Backend**: Python, Flask (or Django)
- **Model**: Convolutional Neural Networks (CNN) using TensorFlow or PyTorch
- **Deployment**: (Heroku, AWS, PythonAnywhere, etc.)

---

## 🔧 Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/plant-disease-predictor.git
   cd plant-disease-predictor
2.Create Virtual Environment (Optional but Recommended)

    ```bash
     python -m venv venv
     source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Dependencies

   ```bash
    pip install -r requirements.txt
4.Run the Web App

    ```bash
     python manage.py runserver
5.Visit the App in Browser
   http://localhost:5000
🧠 Model Details
Architecture: CNN / Transfer Learning (e.g., ResNet, MobileNet)

Dataset: Publicly available plant leaf datasets

Preprocessing: Resizing, normalization, augmentation

Training Metrics:

Accuracy: 98% (replace with actual value)

Classes: [List of diseases detected, e.g., Apple Scab, Tomato Mosaic Virus, etc.]

✅ Usage Instructions
Go to the homepage.

Upload an image of a plant leaf.

Click on Predict.

View the disease diagnosis and confidence score.

🙏 Acknowledgements
AWaDH Lab – Agriculture and Water Technology Development Hub

IIT Ropar – Indian Institute of Technology Ropar

Open-source contributors and dataset providers

📄 License
This project is licensed under the MIT License. See the LICENSE file for details.

