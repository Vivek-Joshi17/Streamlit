import streamlit as st

#Text Input

fname= st.text_input("Enter first name",max_chars=10)
st.title(fname)

#Text Area 
message =st.text_area("Enter message",height=150)
st.write(message)

#Numbers
number =st.number_input("Enter the number",1,25)

#Date input
myappointment =st.date_input("Appointment")

#Time input 
mytime = st.time_input("My Time")

#Hidding password
password = st.text_input("Enter password",type='password')


#Color Picker
color = st.color_picker("Select Color")