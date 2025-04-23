import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model

# Class labels (in same order as training)
CLASS_NAMES = ['Alluvial Soil', 'Black Soil', 'Clay Soil', 'Red Soil']

# Crop recommendations
CROP_RECOMMENDATIONS = {
    'Alluvial Soil': ['Wheat', 'Sugarcane', 'Rice', 'Maize', 'Pulses'],
    'Black Soil': ['Cotton', 'Soybean', 'Sorghum', 'Sunflower', 'Peanuts'],
    'Clay Soil': ['Rice', 'Broccoli', 'Cabbage', 'Lettuce', 'Cauliflower'],
    'Red Soil': ['Groundnut', 'Millets', 'Potatoes', 'Cotton', 'Vegetables']
}

CROP_CALENDAR = {
    'Wheat': 'Start Growing : Nov - Dec | Collect Crops : Apr - May',
    'Sugarcane': 'Start Growing : Feb - Mar | Collect Crops : Dec - Jan',
    'Rice': 'Start Growing : Jun - Jul | Collect Crops : Oct - Nov',
    'Maize': 'Start Growing : Jun - Jul | Collect Crops : Sep - Oct',
    'Pulses': 'Start Growing : Oct - Nov | Collect Crops : Feb - Mar',
    'Cotton': 'Start Growing : Jun - Jul | Collect Crops : Oct - Nov',
    'Soybean': 'Start Growing : Jun - Jul | Collect Crops : Sep - Oct',
    'Sorghum': 'Start Growing : Jun - Jul | Collect Crops : Sep - Oct',
    'Sunflower': 'Start Growing : Jan - Feb | Collect Crops : May - Jun',
    'Peanuts': 'Start Growing : Jun - Jul | Collect Crops : Oct - Nov',
    'Broccoli': 'Start Growing : Oct - Nov | Collect Crops : Jan - Feb',
    'Cabbage': 'Start Growing : Sep - Oct | Collect Crops : Dec - Jan',
    'Lettuce': 'Sow: Oct - Nov | Collect Crops : Dec - Jan',
    'Cauliflower': 'Start Growing : Sep - Oct | Collect Crops : Jan - Feb',
    'Groundnut': 'Start Growing : Jun - Jul | Collect Crops : Oct - Nov',
    'Millets': 'Start Growing : Jul - Aug | Collect Crops : Oct - Nov',
    'Potatoes': 'Start Growing : Oct - Nov | Collect Crops : Feb - Mar',
    'Vegetables': 'Year-round based on type'
}

def load_soil_model(model_path='model/soil_classifier.h5'):
    return load_model(model_path)

def preprocess_image(uploaded_img):
    img = image.load_img(uploaded_img, target_size=(224, 224))
    img_array = image.img_to_array(img) / 255.0
    return np.expand_dims(img_array, axis=0)

def predict_soil(model, preprocessed_img):
    predictions = model.predict(preprocessed_img)
    class_index = np.argmax(predictions)
    predicted_label = CLASS_NAMES[class_index]
    return predicted_label

def get_recommendations(soil_type):
    crops = CROP_RECOMMENDATIONS.get(soil_type, [])
    calendar = {crop: CROP_CALENDAR.get(crop, 'Calendar not available') for crop in crops}
    return crops, calendar
