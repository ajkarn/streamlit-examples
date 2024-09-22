import streamlit as st

def display_name(name):
    st.info(f'**Name:** {name}')

name = st.text_input('Please enter your name')

if len(name)<5:
    st.error('Name too short')
else:
    display_name(name)

# แบบฝึกหัด
# ถ้าไม่มีชื่อ แสดง Error ไม่มีชื่อ
# ถ้าสั้นกว่า 5 ตัวอักษร  แสดง Error ชื่อสั้นเกิน
# ถ้าความยาว 5 หรือมากกว่า แสดงชื่อปกติ 