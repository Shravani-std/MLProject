🎓 Student Performance Indicator


📌 Problem Statement
This project aims to understand how student performance (test scores) is influenced by variables such as gender, ethnicity, parental education level, lunch type, and test preparation. The goal is to build predictive models and visualize key insights.

📌 Project Overview
The Student Performance Indicator project aims to analyze and predict student performance based on multiple factors such as gender, ethnicity, parental education level, lunch type, and test preparation.
It uses data visualization to understand patterns and multiple regression methods for prediction.

The project also includes:
📊 Accuracy comparison of regression models
🧾 Logging and exception handling
⚙️ A clean ML pipeline for training and prediction
🌐 Web application for predictions
☁️ Deployment-ready configuration

✨ Features
Data ingestion, transformation, and preprocessing
Regression-based prediction models
Logging system to track execution
Exception handling for better debugging
Modular ML pipeline (training + prediction)
Model persistence (model.pkl and preprocessor.pkl)
Interactive visualization of student performance
Web application (Flask + HTML) for predictions
Deployment configuration for Elastic Beanstalk

🛠️ Tech Stack
Python 3.x
Pandas, NumPy, Scikit-learn – Data processing & ML
Matplotlib, Seaborn – Visualization
Flask – Web application
Pickle/Joblib – Model serialization
Logging & Custom Exception Handling
Jupyter Notebook – Data exploration & analysis
AWS Elastic Beanstalk – Deployment

🚀 Getting Started

1️⃣ Clone the repository
git clone https://github.com/Shravani-std/Student_Performance_Indicator.git
cd Student_Performance_Indicator

2️⃣ Create virtual environment
conda create -n spi_env python=3.8 -y
conda activate spi_env

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run training pipeline
python src/components/data_ingestion.py

This will create an artifacts/ folder with train.csv, test.csv, model.pkl, and preprocessor.pkl.

5️⃣ Run the web app
python app.py

Visit http://127.0.0.1:5000/
 in your browser to use the app.

📊 Workflow
Data Ingestion – Reads and splits dataset
Data Transformation – Feature engineering & preprocessing
Model Training – Trains multiple regression models, saves the best model
Evaluation – Compares accuracy of different models
Prediction – Uses trained model for new inputs
Web App – User inputs data → prediction displayed in UI
Deployment – AWS Elastic Beanstalk ready

📈 Results
Built regression models with accuracy evaluation
Visual insights on how factors affect student performance
Deployed interactive prediction web app

