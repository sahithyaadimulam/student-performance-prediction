# Student Performance Prediction

A machine learning web application that predicts a student's Performance Index using study habits, previous scores, sleep hours, extracurricular activities, and practice question papers.

## 🔗 Project Links

| Resource | Link |
|---|---|
| **Live Application (Render)** | [Open Live App](https://student-performance-prediction-cafm.onrender.com) |
| **GitHub Repository** | [View Source Code](https://github.com/sahithyaadimulam/student-performance-prediction) |
| **Render Dashboard** | [Manage Deployment](https://dashboard.render.com/) |
| **Docker Hub Repository** | [View Docker Image](https://hub.docker.com/r/sahithyaadimulam/student-performance-prediction) |
| **Docker Image Tags** | [View Available Tags](https://hub.docker.com/r/sahithyaadimulam/student-performance-prediction/tags) |
| **Local Application** | [http://localhost:8501](http://localhost:8501) |
| **Google Colab** | [Open Google Colab](https://colab.research.google.com/) |
| **Kaggle Dataset** | [Student Performance Dataset](https://www.kaggle.com/datasets/nikhil7280/student-performance-multiple-linear-regression) |

> **Note:** The live application may take a little time to start if the hosting service has put it to sleep. The local application link works only when the Docker container is running with port 8501 mapped to your computer.

## 🛠️ Technologies Used

- Python
- Pandas
- Scikit-learn
- Streamlit
- Joblib
- Docker
- GitHub
- Render
- Google Colab

## ✨ Features

- Predicts a student's Performance Index.
- Accepts hours studied and previous scores.
- Includes extracurricular activity participation.
- Considers sleep hours.
- Includes the number of sample question papers practiced.
- Provides an interactive web interface using Streamlit.
- Packages the application and trained model using Docker.

## 🤖 Machine Learning Model

**Algorithm:** Linear Regression

The model was trained using student performance data with five input features.

### Model Evaluation Results

| Metric | Result |
|---|---:|
| Mean Absolute Error (MAE) | 1.61 |
| Mean Squared Error (MSE) | 4.08 |
| Root Mean Squared Error (RMSE) | 2.02 |
| R² Score | 0.989 |

The R² score of 0.989 indicates that the model explains approximately 98.9% of the variance in the target values on the evaluated test set.

## 🐳 Run Using Docker

Make sure Docker Desktop is running.

### 1. Download the image

```bash
docker pull sahithyaadimulam/student-performance-prediction:latest
```

### 2. Run the container

```bash
docker run -p 8501:8501 sahithyaadimulam/student-performance-prediction:latest
```

### 3. Open the application

Visit:

http://localhost:8501

Keep the terminal running while you use the application.

## 📁 Main Project Files

- `app.py` — Streamlit web application.
- `requirements.txt` — Python dependencies.
- `Dockerfile` — Docker image build instructions.
- `student_performance_model.pkl` — Saved trained model.

## 🚀 Deployment

The application is available through Render, and the Docker image is published on Docker Hub.

- Live app: https://student-performance-prediction-cafm.onrender.com
- Source code: https://github.com/sahithyaadimulam/student-performance-prediction
- Docker image: https://hub.docker.com/r/sahithyaadimulam/student-performance-prediction

## 👩‍💻 Author

**Sahithya Adimulam**

GitHub: https://github.com/sahithyaadimulam

---

*This project demonstrates data preparation, machine learning model training and evaluation, interactive application development, containerization, and deployment.*
