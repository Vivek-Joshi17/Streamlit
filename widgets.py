import streamlit as st
st.title("working with widgets")
### Working with widgets

# Working with buttons
name ="Wewake"

if st.button("OK?"):
    st.write("Name : {}".format(name.upper()))

#It will give error if we create a same button with same key

if st.button("OK?",key='newsubmit'):
    st.write("Name: {}".format(name.upper()))

#working with radio button 
status = st.radio("What is your status ",("active","inactive"))

if status == "active":
    st.success("You are active")
else:
    st.error("You are inactive")

### working with checkbox
if st.checkbox("show/hide"):
    st.text("showing something")

#working with  expander
with st.expander("Python"):
    st.success("Hello Python")