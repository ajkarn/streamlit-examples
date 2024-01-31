import streamlit as st
from datetime import datetime
import time


# Initialize connection.
conn = st.connection("postgresql", type="sql")

on = st.toggle('Sync database', True)
last_update = st.empty()
table = st.empty()
chart = st.empty()

while on:
# Perform query.
    df = conn.query('SELECT * FROM hourly_temperature;', ttl=1)

    df = df.set_index('timestamp')
    table.write(df)
    chart.line_chart(df)
    
    current_dateTime = datetime.now()
    last_update.write("Last updated: "+str(current_dateTime.strftime("%c")))
    
    time.sleep(60)
    

