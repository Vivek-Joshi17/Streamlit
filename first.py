#Streamlit is a python framework for developing web applications especially for data science
import streamlit as st

st.title("Hello Streamlit")
st.text("Hello World this is a text")
###input format 
name ="Wewake"
st.text("This is so {}".format(name))

### Header 
st.header("Section 1")
st.subheader("Section 1.1")

###Markdown
st.markdown("- Home")
st.success("Approved")
st.warning("Denied")
st.info("Help")
st.error("Error")
st.exception("Exception")

## super power function
st.write("This is a text")

## helping function
st.help(range)