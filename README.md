# 🌾 CROPxPERT - Intelligent Crop Advisory Platform

CROPxPERT is an intelligent and interactive crop advisory system built with **Streamlit**. It empowers farmers and agronomists with predictive insights related to **crop yield**, **soil analysis**, and **weather forecasting** to enhance agricultural productivity.

---

## 🚀 Features

### 🏠 Home - Dashboard
An intuitive landing dashboard providing easy navigation across all modules:
- Quick summary of services
- Navigable menu for Yield Prediction, Soil Analysis, and Weather Forecast

---

### 🌱 Page 1: Yield Prediction
Predict the expected **crop yield** based on user-provided agricultural parameters.

#### 📥 Inputs:
- Place (name of city or country)
- Year
- Type of crop
- Average Rainfall
- Average Temperature
- Pestisides used 

#### 🧠 Model:
- Built using **Random Forest Regressor**

#### 📤 Output:
- Estimated **Yield in kg/hectare**

---

### 🧪 Page 2: Soil Type Classification + Crop Recommendation
Upload a soil image to classify the soil type and get crop recommendations for the year.

#### 📥 Inputs:
- Upload a **soil image** (JPEG, PNG)

#### 🧠 Model:
- Image classifier built using **MobileNet-based CNN**
- Integrated with a knowledge base for **crop recommendation**

#### 📤 Output:
- Predicted **Soil Type**
- List of **Recommended Crops** for each season

#### 💬 Bonus Feature: Gemini Chat Assistant
Ask any agricultural queries! Integrated with **Gemini API** (Generative AI by Google) to:
- Answer soil-related queries
- Provide insights on fertilizers, pests, and more

---

### 🌤️ Page 3: 7-Day Weather Forecast
Plan ahead with accurate weather predictions.

#### 📥 Inputs:
- User's location (city or coordinates)

#### 🌐 API Used:
- Real-time weather API

#### 📤 Output:
- Daily weather forecast for 7 days:
  - Min/Max Temperature
  - Weather Conditions (e.g., Rain, Cloudy, Clear)

---

## 🛠️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **ML Models**: 
  - Random Forest Regressor (Yield Prediction)
  - MobileNet CNN (Soil Image Classification)
- **APIs**:
  - Gemini API (Chat assistant)
  - Weather API (Forecasting)
- **Deployment**: Can be hosted on **Streamlit Cloud**, **Render**, or **local server**

---

## 💾 Installation

```bash
git clone https://github.com/sanskarkumar109/CROPxPERT.git
cd CROPxPERT

# (Optional) Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run Home.py


📁 Project Structure
bash
Copy
Edit
CROPxPERT/
├── app.py                     # Main Streamlit app
├── pages/
│   ├── 1_Yield_Prediction.py
│   ├── 2_Soil_Classification.py
│   └── 3_Weather_Forecast.py
├── model/
│   ├── yield_model.pkl
│   └── soil_cnn_model.h5
├── utils/
│   ├── preprocessing.py
│   └── api_utils.py
├── assets/                    # Static files (soil images, icons)
├── .gitattributes             # Git LFS tracking
├── requirements.txt
└── README.md
⚙️ Requirements
Python 3.8+

Streamlit

scikit-learn

TensorFlow / Keras

OpenCV

Requests

Git LFS (for handling large model files)

Note on Large Files
This project uses Git LFS to manage large model files like model.pkl and .h5. If you're cloning or contributing:

git lfs install
git lfs pull


🤝 Contributors
Sanskar Kumar

🙌 Acknowledgements
Google Gemini API
OpenWeatherMap API
Streamlit Community
