import streamlit as st
import pandas as pd
import joblib


# LOAD DATASETS

df_train = pd.read_csv("dataset/Training.csv")
description = pd.read_csv("dataset/description.csv")
diets = pd.read_csv("dataset/diets.csv")
medications = pd.read_csv("dataset/medications.csv")
precautions = pd.read_csv("dataset/precautions_df.csv")
workout = pd.read_csv("dataset/workout_df.csv")
symptom_columns = df_train.columns[:-1]

# Load model + encoder
model = joblib.load("models/svc_model.pkl")
encoder = joblib.load("models/label_encoder.pkl")



st.set_page_config(page_title="AI Disease Prediction", page_icon="🩺", layout="centered")
st.title("🩺 AI Disease Prediction System")
st.markdown("###### Enter your symptoms below and get AI-powered disease prediction with treatment suggestions.")


selected_symptoms = st.multiselect(
    "Select your symptoms:",
    options=symptom_columns
)



if st.button("🔮 Predict Disease"):
    if not selected_symptoms:
        st.warning("Please select at least one symptom.")
    else:
        
        input_data = [0] * len(symptom_columns)
        for symptom in selected_symptoms:
            input_data[list(symptom_columns).index(symptom)] = 1

        pred_label = model.predict([input_data])[0]
        predicted_disease = encoder.inverse_transform([pred_label])[0]

    
        # STYLISH RESULT CARD
        st.markdown(f"""
        <div style="padding:20px; border-radius:12px; background-color:#f8f9fa; border:1px solid #ddd; text-align:center;">
        <h3 style="color:#d63384; margin-bottom:5px;">🧾 Predicted Disease</h3>
        <h2 style="color:#198754; font-weight:bold;">{predicted_disease}</h2>
        </div>
        """, unsafe_allow_html=True)

      
        st.markdown("### 🧠 Description")
        st.info(description[description["Disease"] == predicted_disease]["Description"].values[0])

       
        col1, col2, col3 = st.columns(3)

        # Precautions
        with col1:
            st.markdown("### 🛡 Precautions")
            precautions_list = precautions[precautions["Disease"] == predicted_disease].iloc[:, 2:].dropna(axis=1).values.flatten()
            for p in precautions_list:
                st.write(f"- {p}")

        # Medications
        with col2:
            st.markdown("### 💊 Medications")
            meds_str = medications.loc[medications["Disease"] == predicted_disease, "Medication"].values[0]
            meds = [m.strip().strip("'\"") for m in meds_str.strip("[]").split(",")]
            
            for m in meds:
                st.write(f"- {m}")


        # Diets
        with col3:
            st.markdown("### 🥗 Diet")
            diets_str = diets.loc[diets["Disease"] == predicted_disease,"Diet"].values[0]
            diets = [d.strip().strip("'\"") for d in diets_str.strip("[]").split(",")]
            for d in diets:
                st.write(f"- {d}")

        
        st.markdown("<h3 style='text-align:left;'>🏋️ Recommended Workouts</h3>", unsafe_allow_html=True)

        workouts = workout[workout["disease"] == predicted_disease].iloc[:, 3:].dropna(axis=1).values.flatten()

       
        for i in range(0, len(workouts), 2):
            cols = st.columns([1, 1, 1, 1, 1])  
            
            if i < len(workouts):
                with cols[0]:
                    st.write(f"- {workouts[i]}")
            if i + 1 < len(workouts):
                with cols[3]:
                    st.write(f"- {workouts[i+1]}")



