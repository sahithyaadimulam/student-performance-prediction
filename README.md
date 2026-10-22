# Student Performance Prediction

## 1. Live Project (Render)
https://student-performance-prediction-cafm.onrender.com

## 2. GitHub Repository (Source Code)
https://github.com/sahithyaadimulam/student-performance-prediction

## 3. Render Dashboard
https://dashboard.render.com/

## 4. Local Docker App
http://localhost:8501

Note: The local Docker link works only when the Docker container is running on your computer.

## 5. Google Colab
https://colab.research.google.com/

Open your saved Student Performance Prediction notebook from Google Drive.

## 6. Kaggle Dataset
https://www.kaggle.com/datasets/nikhil7280/student-performance-multiple-linear-regression

## Technologies Used
- Python
- Pandas
- Scikit-learn
- Streamlit
- GitHub
- Render
- Docker

## Model Evaluation
- MAE: 1.61
- MSE: 4.08
- RMSE: 2.02
- R² Score: 0.989
# Student Performance Prediction

A machine learning application that predicts student performance using study habits and previous scores. Built with Python, Streamlit, scikit-learn, and Docker.

## Project Links

- **Docker Hub Repository:** https://hub.docker.com/r/sahithyaadimulam/student-performance-prediction
- **Docker Image Tags:** https://hub.docker.com/r/sahithyaadimulam/student-performance-prediction/tags
- **Run Locally:** http://localhost:8502

## Technologies Used

- Python
- Pandas
- scikit-learn
- Streamlit
- Docker

## Features

- Enter study hours and previous scores.
- Select extracurricular activity participation.
- Enter sleep hours and sample question papers practiced.
- Predict a student's performance index.

## Run the Docker Image

Make sure Docker Desktop is running, then open a terminal and execute:

```bash
docker pull sahithyaadimulam/student-performance-prediction:latest
docker run -p 8502:8501 sahithyaadimulam/student-performance-prediction:latest
```

Open this address in your browser:

http://localhost:8502

## Docker Image

Repository: `sahithyaadimulam/student-performance-prediction`

Tag: `latest`

Platform: `linux/amd64`

## Project Status

The Docker image has been built, tested locally, and pushed to Docker Hub.
