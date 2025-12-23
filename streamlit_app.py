import streamlit as st
import requests

st.set_page_config(page_title="Gold Price Predictor")

st.title("💰 Gold Price Prediction")
st.write("Predict gold price using USD-INR value")

usd_inr = st.number_input(
    "Enter USD to INR value",
    min_value=50.0,
    max_value=120.0,
    value=86.0,
    step=0.01
)

if st.button("Predict Gold Price"):
    payload = {
        "USD_INR": usd_inr
    }

    API_URL="web-production-bc33c.up.railway.app"

    response = requests.post(
        API_URL,
        json=payload
    )
    try:
        response=requests.post(API_URL,json=payload)

        if response.status_code == 200:
            result = response.json()
            st.success(f"Predicted Gold Price: ₹ {result['predicted_gold_price']}")
        else:
            st.error("API ERROR :",response.text)
    except Exception as e:
        st.error(f"connection failed:{e}")
