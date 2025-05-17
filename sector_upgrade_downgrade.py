import streamlit as st
import pandas as pd

# Sample data
data = {
    "Sector": ["Auto", "FMCG", "IT", "Pharma", "Banking"],
    "Action": ["Upgrade", "Downgrade", "Upgrade", "Downgrade", "Upgrade"],
    "Previous Rating": ["Neutral", "Overweight", "Underweight", "Neutral", "Neutral"],
    "Current Rating": ["Overweight", "Underweight", "Neutral", "Underweight", "Overweight"],
    "Reason": [
        "EV growth and rural pickup",
        "Weak rural demand, margin pressure",
        "Cost optimization, AI growth",
        "USFDA issues, pricing pressure",
        "Strong credit growth, low NPAs"
    ]
}

df = pd.DataFrame(data)

st.set_page_config(page_title="Sector Upgrade-Downgrade Screener", layout="wide")
st.title("📈 Sector Upgrade-Downgrade Screener")

selected_action = st.selectbox("Filter by Action", options=["All", "Upgrade", "Downgrade"])
if selected_action != "All":
    df = df[df["Action"] == selected_action]

st.dataframe(df, use_container_width=True)

st.markdown("### 📊 Highlights")

def highlight_row(row):
    if row.Action == "Upgrade":
        return ['background-color: #d4edda']*len(row)
    else:
        return ['background-color: #f8d7da']*len(row)

st.dataframe(df.style.apply(highlight_row, axis=1))

