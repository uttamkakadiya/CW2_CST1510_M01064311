import streamlit as st
import pandas as pd
from app.db import get_connection
from app.cyber_incidents import get_all_cyber_incidents

conn = get_connection()
data = get_all_cyber_incidents(conn)

st.title("Cyber Incidents Dashboard")

# Check if user is logged in
if not st.session_state.get('logged_in', False):
    st.warning("Please log in to access the dashboard.")
    st.stop() 

else:
    st.success(f"Welcome, {st.session_state['username']}! You are logged in.")

with st.sidebar:
    st.header("Navigation")
    severity_ = st.selectbox('severity', data['severity'].unique())

filtered_data = data[data['severity'] == severity_]

data['timestamp'] = pd.to_datetime(data['timestamp'])
col1, col2 = st.columns(2)

with col1:
    st.header("Data 1st Column")
    st.line_chart(filtered_data['status'].value_counts())

with col2:
    st.header("Data 2nd Column")
    st.line_chart(filtered_data, x='timestamp', y='incident_id')

st.write(filtered_data)
