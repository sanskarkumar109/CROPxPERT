import streamlit as st

# Page configuration
st.set_page_config(
    page_title="CROPxPERT Dashboard",
    page_icon="🌾",
    layout="centered"
)

# Header Section
st.title("🌾 CROPxPERT")
st.subheader("Your Smart Farming Assistant")

# Introduction
st.markdown("""
Welcome to **CROPxPERT** — your one-stop intelligent farming platform.

🔍 Use the sidebar to navigate through the tools:
- **Weather Forecast**
- **Soil Type Prediction**
- **Crop Yield Estimation**

---

### 🚀 Features at a Glance

- 📷 Upload or capture a soil image to identify the soil type.
- 🌤️ Get 7-day weather forecast for any Indian city.
- 📈 Predict crop yield using environmental and regional inputs.

---
""")

# Footer
st.info("👈 Use the sidebar to get started!")
st.markdown("© 2025 CROPxPERT Team | Built with ❤️ using Streamlit")
