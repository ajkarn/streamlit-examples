import streamlit as st
import time

on = st.toggle('Activate counter', True)

counter = st.empty()
count = 0
while on:
    counter.header(count)
    time.sleep(0.1)
    count +=1

# แบบฝึกหัด เพิ่มปุ่ม reset เพื่อรีเซต counter เป็น 0