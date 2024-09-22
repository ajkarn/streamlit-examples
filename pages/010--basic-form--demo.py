import streamlit as st

import datetime

today = datetime.datetime.now()
last_30year = today.year - 30
jan_1_last30years = datetime.date(last_30year, 1, 1)
 
with st.form('feedback_form'):
    name = st.text_input('Enter your name:')
    rating = st.slider('Rate this app:', 0, 100, 20, step=5)
    dob = st.date_input('Enter your date of birth:', min_value=jan_1_last30years)
    buy = st.radio('Will you buy this app?', ('Yes', 'No', 'Not sure'))
    submitted = st.form_submit_button('Submit')
 
    if submitted:
        st.write('**Name:**', name, '**DOB**', dob, \
            '**Rating**',rating, '**Buy**', buy)