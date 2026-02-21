
import streamlit as st
from datetime import date

st.title("Age Calculator")
today = date.today()
dob = st.date_input("Enter your date of birth",
                    min_value=date(1900, 1, 1),
                    max_value=date.today())

if dob:
    age = today.year - dob.year

    if (today.month, today.day) < (dob.month, dob.day):
        age -= 1

    st.success(f"Your Current Age is: {age} years")
    st.balloons()
    
fedd = st.feedback('stars')
cl = st.button('Done')   
if fedd and cl:
    st.subheader('Thankyou for your feedback😊')