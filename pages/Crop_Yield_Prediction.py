import streamlit as st
import pickle
import pandas as pd

# Load saved model and encoders
model_data = pickle.load(open("model/model.pkl", "rb"))
model = model_data["model"]
feature_names = model_data["features"]

label_enc_area = pickle.load(open("model/label_enc_area.pkl", "rb"))
label_enc_item = pickle.load(open("model/label_enc_item.pkl", "rb"))

def predict(input_data):
    try:
        input_df = pd.DataFrame([input_data])
        input_df["Area"] = label_enc_area.transform([input_data["Area"]])
        input_df["Item"] = label_enc_item.transform([input_data["Item"]])
        input_df = input_df[feature_names]
        prediction = model.predict(input_df)
        return round(float(prediction[0]), 2)
    except Exception as e:
        return str(e)

# Streamlit UI
st.title("🌾 Crop Yield Prediction")
st.subheader("Estimate the expected yield based on input factors")

area = st.text_input("Enter Area (e.g., France)")
item = st.text_input("Enter Crop Item (e.g., Maize)")
year = st.number_input("Enter Year", min_value=2000, max_value=2100, step=1)
avg_rainfall = st.number_input("Average Rainfall (mm/year)", min_value=0.0)
avg_temp = st.number_input("Average Temperature (°C)", min_value=-50.0, max_value=50.0, step=0.1)
pesticides = st.number_input("Pesticides Used (tonnes)", min_value=0.0)

if st.button("Predict Yield"):
    if area and item:
        input_data = {
            "Area": area,
            "Item": item,
            "Year": year,
            "average_rain_fall_mm_per_year": avg_rainfall,
            "avg_temp": avg_temp,
            "pesticides_tonnes": pesticides
        }
        prediction = predict(input_data)
        st.success(f"🌿 Predicted Crop Yield: **{prediction} tonnes**")
    else:
        st.error("❌ Please enter valid Area and Crop Item.")
