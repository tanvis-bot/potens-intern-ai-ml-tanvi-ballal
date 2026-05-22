import streamlit as st
import requests

st.set_page_config(
    page_title="AI Triage Agent",
    layout="wide"
)

st.title("AI Infrastructure Incident Triage Agent")

st.write(
    "Enter an infrastructure issue below and let the AI agent analyze it."
)

issue = st.text_area(
    "Describe the issue"
)

if st.button("Analyze Incident"):

    response = requests.post(
        "http://127.0.0.1:8000/triage",
        json={"issue": issue}
    )

    result = response.json()["response"]

    st.subheader("Triage Decision")
    st.write(result["triage_decision"])

    st.subheader("Similar Historical Incident")
    st.json(result["similar_incident"])

    st.subheader("Infrastructure Status")
    st.json(result["system_status"])

    st.subheader("Acknowledgment Message")
    st.write(result["acknowledgment"])

    st.subheader("Reasoning Trace")

    for step in result["reasoning_trace"]:
        st.write("•", step)