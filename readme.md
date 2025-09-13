# 🩺 AI Disease Prediction & Recommendation System  

This is a **learning project** where I built an AI-powered medical recommendation system using **Machine Learning + Streamlit**.  
The app takes user-selected symptoms, predicts the most likely disease, and provides **description, precautions, medications, diet plans, and workout recommendations** for that disease.  

https://github.com/user-attachments/assets/1da5248e-72cb-41bd-96ed-75e9927bfcc9 

---
## 🌐 Live Demo  

🔗 **Try it online:** [MediPredict App](https://ai-powered-disease-recommendation-system.streamlit.app/)

## 🚀 Features  
✅ **Symptom-based Disease Prediction** – Select symptoms, get a prediction instantly.  
✅ **Medical Recommendations** – View description, precautions, medications, diets, and workouts.  
✅ **User-Friendly UI** – Built with Streamlit for an interactive experience.  
✅ **Fully Offline Model** – Uses a trained ML model (SVC/XGBoost/Random Forest) stored in `models/`.  

---

## 🛠 Tech Stack  
- **Python** 🐍  
- **Pandas** for data preprocessing  
- **Scikit-learn** for training ML models  
- **Streamlit** for the interactive web UI  
- **Joblib** for saving & loading models  

---

## 📂 Project Structure  
```
├── dataset/
│ ├── Training.csv
│ ├── description.csv
│ ├── diets.csv
│ ├── medications.csv
│ ├── precautions_df.csv
│ ├── workout_df.csv
│
├── models/
│ ├── svc_model.pkl
│ ├── label_encoder.pkl
│ ├── log_reg_model.pkl
│ ├── random_forest_model.pkl
│ ├── xgboost_model.pkl
│
├── app.py # Main Streamlit app
├── requirements.txt # Python dependencies
├── medicine_recommendation_system.ipynp
├── README.md # You are here
```


---

## ▶️ How to Run  

1. **Clone this repo**  
```bash
git clone https://github.com/moelnefary/AI-Powered-Disease-Recommendation-System.git

cd AI-Powered-Disease-Recommendation-System

##Install dependencies
pip install -r requirements.txt

##Run the Streamlit app
streamlit run app.py

##Open your browser at http://localhost:8501 and start predicting diseases!

```

## 📚 Learning Goals  

This project helped me learn:  

- 🏗️ **Building an End-to-End ML Pipeline**  
  From data preprocessing → model training → saving models → loading them in the app.  

- 🏷️ **Encoding Multi-Class Labels**  
  Using `LabelEncoder` to handle multiple diseases and map predictions back to human-readable class names.  

- 🌐 **Deploying Machine Learning Apps**  
  Learning how to take a trained model, build a Streamlit app, and deploy it online for anyone to use.  

## ⚠️ Disclaimer  

This project is for **educational purposes only**.  
It is not intended to replace professional medical advice, diagnosis, or treatment.  
Always consult with a qualified healthcare professional for any medical concerns.  






