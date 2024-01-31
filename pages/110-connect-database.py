import streamlit as st

# Initialize connection.
conn = st.connection("postgresql", type="sql")

# Perform query.
df = conn.query('SELECT * FROM hourly_temperature;', ttl=1)

df = df.set_index('timestamp')
st.write(df)
st.line_chart(df)
