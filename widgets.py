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

# working with select

my_lang = ["python","julia","go","rust"]
choice = st.selectbox("Language",my_lang)
st.write("You have selected {}".format(choice))

# working with multiple selection
spoken_lang =("English","French","Hindi","Pahadi","Japanese")
my_spoken_lang = st.multiselect("Spoken_lang",spoken_lang)

#working with slider(int/float/data)
age = st.slider("Age",1,100)

#working with select slider (any datatype)
color=st.select_slider("Choose color",options=["yellow","red","blue","black","white"],value=("black","yellow"))