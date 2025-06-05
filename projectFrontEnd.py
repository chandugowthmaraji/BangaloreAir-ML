import streamlit as st
import pickle
import time

st.set_page_config(layout="wide")


st.markdown("""
<style>
/* Background */
html, body, .stApp {
  height: 100%;
  margin: 0;
  padding: 0;
  background: radial-gradient(circle at top left, #0f2027, #203a43, #2c5364);
  color: white;
  font-family: 'Segoe UI', sans-serif;
  overflow-x: hidden;
}

.input-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
  margin-top: 20px;
  background: rgba(255,255,255,0.05);
  padding: 25px;
  border-radius: 16px;
  box-shadow: 0 0 15px #00fff740;
}

input[type="number"] {
  background-color: #1a1a2e !important;
  color: #fff !important;
  border: 2px solid #00fff7 !important;
  border-radius: 10px !important;
  padding: 14px !important;
  font-size: 16px !important;
  box-shadow: inset 0 0 10px #00fff740;
}

input[type=number]::-webkit-inner-spin-button,
input[type=number]::-webkit-outer-spin-button {
  -webkit-appearance: none;
  margin: 0;
  transform: scale(0.7);
}


.dot-loader {
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 20px auto;
  height: 60px;
}
.dot-loader div {
  width: 15px;
  height: 15px;
  margin: 0 5px;
  background: #00fff7;
  border-radius: 50%;
  animation: dotPulse 1.4s infinite ease-in-out both;
}
.dot-loader div:nth-child(1) {
  animation-delay: -0.32s;
}
.dot-loader div:nth-child(2) {
  animation-delay: -0.16s;
}
.dot-loader div:nth-child(3) {
  animation-delay: 0;
}
@keyframes dotPulse {
  0%, 80%, 100% {
    transform: scale(0);
  } 40% {
    transform: scale(1);
  }
}


.result-box {
  background: #112d4e;
  border-radius: 15px;
  padding: 25px;
  margin-top: 30px;
  width: 700px;
  font-size: 20px;
  font-weight: bold;
  text-align: center;
  box-shadow: 0 0 25px #00fff7aa;
  animation: pulse 2s infinite;
  margin-left: auto;
  margin-right: auto;
}

@keyframes pulse {
  0% { box-shadow: 0 0 20px #00fff7aa; }
  50% { box-shadow: 0 0 40px #00fff7aa; }
  100% { box-shadow: 0 0 20px #00fff7aa; }
}

.result-good { color: #6ee56e; }
.result-moderate { color: #ffb74d; }
.result-sensitive { color: #ffcc00; }
.result-unhealthy { color: #ff7043; }
.result-veryunhealthy { color: #e65100; }
.result-hazardous { color: #d50000; }


.image-glow-right {
  display: block;
  margin-left: auto;
  margin-right: 1600px;
  margin-top: 20px;
  border: 6px solid #00fff7;
  border-radius: 20px;
  width: 480px;
  box-shadow: 0 0 40px #00fff7cc;
  transition: transform 0.3s ease;
}
.image-glow-right:hover {
  transform: scale(1.05);
}
</style>
""", unsafe_allow_html=True)


st.markdown('<div style="max-width:900px; margin:auto;">', unsafe_allow_html=True)


st.title("🌆 Air Quality Index - Bangalore")



a = st.number_input("🌫️ PM2.5 (Particulate Matter)", min_value=0.0, value=0.0, step=0.1, format="%.1f", key="pm25")
b = st.number_input("🌫️ PM10 (Particulate Matter)", min_value=0.0, value=0.0, step=0.1, format="%.1f", key="pm10")
c = st.number_input("🧪 Nitrogen Dioxide (NO₂)", min_value=0.0, value=0.0, step=0.1, format="%.1f", key="no2")
d = st.number_input("🧪 Sulfur Dioxide (SO₂)", min_value=0.0, value=0.0, step=0.1, format="%.1f", key="so2")
e = st.number_input("🚗 Carbon Monoxide (CO)", min_value=0.0, value=0.0, step=0.1, format="%.1f", key="co")
f = st.number_input("🌤️ Ozone (O₃)", min_value=0.0, value=0.0, step=0.1, format="%.1f", key="o3")

st.markdown('</div>', unsafe_allow_html=True)

if st.button("🎯 Predict AQI"):
    loading = st.empty()
    loading.markdown('<div class="dot-loader"><div></div><div></div><div></div></div>', unsafe_allow_html=True)
    time.sleep(2)
    loading.empty()

    try:
        with open(r"C:\\Users\\User\\Desktop\\Akira\\projectTrainmodifyDT.pkl", 'rb') as file:
            model = pickle.load(file)

        result = model.predict([[a, b, c, d, e, f]])[0]

        if 0 <= result <= 50:
            st.markdown(f'<div class="result-box result-good">✅ GOOD AIR QUALITY INDEX<br><span style="font-size:32px;">🌿</span><br><b>AQI: {result}</b></div>', unsafe_allow_html=True)
        elif result <= 100:
            st.markdown(f'<div class="result-box result-moderate">🔶 MODERATE AIR QUALITY INDEX<br><span style="font-size:32px;">🌤️</span><br><b>AQI: {result}</b></div>', unsafe_allow_html=True)
        elif result <= 150:
            st.markdown(f'<div class="result-box result-sensitive">⚠️ UNHEALTHY FOR SENSITIVE GROUPS<br><span style="font-size:32px;">😷</span><br><b>AQI: {result}</b></div>', unsafe_allow_html=True)
        elif result <= 200:
            st.markdown(f'<div class="result-box result-unhealthy">❗ UNHEALTHY AIR QUALITY INDEX<br><span style="font-size:32px;">😟</span><br><b>AQI: {result}</b></div>', unsafe_allow_html=True)
        elif result <= 300:
            st.markdown(f'<div class="result-box result-veryunhealthy">⚠️ VERY UNHEALTHY AIR QUALITY INDEX<br><span style="font-size:32px;">🤒</span><br><b>AQI: {result}</b></div>', unsafe_allow_html=True)
        elif result <= 500:
            st.markdown(f'<div class="result-box result-hazardous">🚨 HAZARDOUS AIR QUALITY INDEX - VACATE IMMEDIATELY<br><span style="font-size:32px;">🔥</span><br><b>AQI: {result}</b></div>', unsafe_allow_html=True)
        else:
            st.warning("❓ AQI OUT OF RANGE")

        st.markdown("""
            <img src="https://st.adda247.com/https://wpassets.adda247.com/wp-content/uploads/multisite/sites/5/2023/11/06110959/aqi_mini-1200x675-1.png" alt="AQI Visual" class="image-glow-right" />
        """, unsafe_allow_html=True)

    except FileNotFoundError:
        st.error("❌ Model file not found. Please check the path.")
    except Exception as e:
        st.error(f"❌ An error occurred: {e}")

st.markdown('</div>', unsafe_allow_html=True)
