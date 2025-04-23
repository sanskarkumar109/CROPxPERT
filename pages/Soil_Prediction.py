# import streamlit as st
# from PIL import Image
# from utils import load_soil_model, preprocess_image, predict_soil, get_recommendations
# from database import save_prediction
# from sns_helper import send_sms

# import google.generativeai as genai  # 👈 For Gemini API
# import os

# # Load Gemini API Key from a secure place or hardcode (not recommended)
# GEMINI_API_KEY = "AIzaSyBIDRZDPQJF3wjTprSf4rbFqpCHOicIuJ8"  # 🔐 Replace with your actual key
# genai.configure(api_key=GEMINI_API_KEY)
# model_gemini = genai.GenerativeModel("gemini-2.0-flash")

# # Load model
# model_path = 'soil_classifier.h5'
# model = load_soil_model(model_path)

# st.title("🧪 CROPxPERT : One Stop Solution for Farmers")
# st.subheader("Upload a soil image to predict its type and get crop suggestions.")

# input_method = st.radio("Choose Image Source:", ["📁 Upload an Image", "📷 Use Camera"])
# img = None

# if input_method == "📁 Upload an Image":
#     uploaded_file = st.file_uploader("Upload a soil image", type=["jpg", "jpeg", "png"])
#     if uploaded_file:
#         img = uploaded_file
#         st.image(Image.open(img), caption="Uploaded Soil Image", use_container_width=True)

# elif input_method == "📷 Use Camera":
#     captured_img = st.camera_input("Capture a soil photo using your camera")
#     if captured_img:
#         img = captured_img
#         st.image(Image.open(img), caption="Captured Soil Image", use_container_width=True)

# if img is not None:
#     preprocessed = preprocess_image(img)
#     predicted_soil = predict_soil(model, preprocessed)
#     st.success(f"🧪 Predicted Soil Type: **{predicted_soil}**")

#     crops, calendar = get_recommendations(predicted_soil)
#     st.markdown("### 🌱 Recommended Crops")
#     for crop in crops:
#         st.markdown(f"**🌾 {crop}**")
#         st.markdown(f"🗓️ {calendar[crop]}")
#         st.markdown("---")

#     # Save prediction to DB
#     image_name = img.name if hasattr(img, 'name') else "camera_image"
#     save_prediction(image_name, predicted_soil, crops)
#     st.info("✅ Prediction saved to the database.")

#     # 🔔 Optional: Send results via SMS
#     if st.checkbox("📩 Send result via SMS"):
#         phone = st.text_input("Enter your phone number (e.g., +91XXXXXXXXXX)")
#         if st.button("Send SMS"):
#             message = f"Predicted Soil: {predicted_soil}\nRecommended Crops: {', '.join(crops)}"
#             send_sms(message, phone)
#             st.success("📬 SMS sent successfully!")

# # 💬 Gemini Chatbot Section
# st.markdown("---")
# st.subheader("💬 Talk to ChatBot (Powered by Gemini)")

# chat_query = st.text_input("Ask your question about soil, crops, or farming:")

# if st.button("Get Answer"):
#     if chat_query.strip() == "":
#         st.warning("Please enter a question.")
#     else:
#         with st.spinner("Thinking... 🤖"):
#             try:
#                 response = model_gemini.generate_content(chat_query)
#                 st.success("Response received:")
#                 st.write(f"🤖 {response.text}")
#             except Exception as e:
#                 st.error(f"Error: {str(e)}")











import streamlit as st
from PIL import Image
from utils import load_soil_model, preprocess_image, predict_soil, get_recommendations

import google.generativeai as genai  # 👈 For Gemini API
import os

# Load Gemini API Key from a secure place or hardcode (not recommended)
GEMINI_API_KEY = "AIzaSyBIDRZDPQJF3wjTprSf4rbFqpCHOicIuJ8"  # 🔐 Replace with your actual key
genai.configure(api_key=GEMINI_API_KEY)
model_gemini = genai.GenerativeModel("gemini-2.0-flash")

# Load model
model_path = 'model/soil_classifier.h5'
model = load_soil_model(model_path)

st.title("🧪 CROPxPERT : One Stop Solution for Farmers")
st.subheader("Upload a soil image to predict its type and get crop suggestions.")

input_method = st.radio("Choose Image Source:", ["📁 Upload an Image", "📷 Use Camera"])
img = None

if input_method == "📁 Upload an Image":
    uploaded_file = st.file_uploader("Upload a soil image", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        img = uploaded_file
        st.image(Image.open(img), caption="Uploaded Soil Image", use_container_width=True)

elif input_method == "📷 Use Camera":
    captured_img = st.camera_input("Capture a soil photo using your camera")
    if captured_img:
        img = captured_img
        st.image(Image.open(img), caption="Captured Soil Image", use_container_width=True)

if img is not None:
    preprocessed = preprocess_image(img)
    predicted_soil = predict_soil(model, preprocessed)
    st.success(f"🧪 Predicted Soil Type: **{predicted_soil}**")

    crops, calendar = get_recommendations(predicted_soil)
    st.markdown("### 🌱 Recommended Crops")
    for crop in crops:
        st.markdown(f"**🌾 {crop}**")
        st.markdown(f"🗓️ {calendar[crop]}")
        st.markdown("---")

# 💬 Gemini Chatbot Section
st.markdown("---")
st.subheader("💬 Talk to ChatBot (Powered by Gemini)")

chat_query = st.text_input("Ask your question about soil, crops, or farming:")

if st.button("Get Answer"):
    if chat_query.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking... 🤖"):
            try:
                response = model_gemini.generate_content(chat_query)
                st.success("Response received:")
                st.write(f"🤖 {response.text}")
            except Exception as e:
                st.error(f"Error: {str(e)}")
