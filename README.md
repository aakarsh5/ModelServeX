# 🚀 ModelServeX

ModelServeX is a lightweight and scalable web application that enables seamless deployment of machine learning models as REST APIs.  
It simplifies the process of serving trained models, making them accessible to applications, researchers, and developers without worrying about infrastructure complexities.

---

## ✨ Features
- 📦 Deploy machine learning models as REST APIs  
- ⚡ Fast and lightweight (built with **FastAPI**)  
- 🌐 Ready-to-use endpoints for model inference  
- 🔒 Secure and reliable with structured error handling  
- ☁️ Deployable on **Render**, **Docker Hub**, or any cloud service  

---

## 🛠️ Tech Stack
- **Backend:** Python, FastAPI  
- **Model Serving:** TensorFlow (CIFAR-10 image classification model)  
- **Deployment:** Docker & Render  

---

## 📂 Project Structure
ModelServeX/ │── app.py # Main FastAPI application │── model.h5 # Pre-trained CIFAR-10 model │── train.py # Training script │── try.py # Local testing script │── requirements.txt # Python dependencies │── Dockerfile # Docker setup │── .gitignore # Files ignored in version control │── README.md # Project documentation

Code

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/aakarsh5/ModelServeX.git
cd ModelServeX
```
2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows
```
4. Install Dependencies
```bash
pip install -r requirements.txt
```
6. Run the Application
```bash
uvicorn app:app --host 0.0.0.0 --port 8000
The server will start at: 👉 http://127.0.0.1:8000 Swagger UI available at: 👉 http://127.0.0.1:8000/docs
```

📡 API Endpoints
Root Endpoint
http
GET /
Response:

json
{ "message": "Welcome to ModelServeX API" }
Prediction Endpoint
http
POST /predict
Request Body (JSON):

json
{ "input": [ /* image array data */ ] }
Response:

json
{ "prediction": "airplane" }
🧪 Predict via Swagger UI (/docs)
ModelServeX includes an interactive frontend powered by FastAPI's Swagger UI, accessible at:

👉 http://127.0.0.1:8000/docs

This allows users to test the /predict endpoint directly from their browser.

🖼️ How to Use
Download a CIFAR-10 image You can grab sample images from the CIFAR-10 dataset or use any 32×32 RGB image.

Open Swagger UI Navigate to http://127.0.0.1:8000/docs

Click on /predict → Try it out → Choose File Upload your image (e.g., cat.png, truck.jpg, etc.)

Execute The API will return a JSON response with:

predicted_class: e.g., "dog"

confidence: e.g., 0.968

probabilities: dictionary of class-wise scores

☁️ Deployment on Render
Push your code to GitHub

Go to Render and create a new Web Service

Connect your GitHub repository

Set the following:

Build Command: pip install -r requirements.txt

Start Command: uvicorn app:app --host 0.0.0.0 --port 8000

Your model API will be live! 🎉

🤝 Contributing
Contributions are welcome! Please fork the repo and submit a pull request.

📜 License
This project is licensed under the MIT License.

👨‍💻 Author
Developed by Aakarsh Lohani GitHub: @aakarsh5
