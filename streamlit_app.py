import streamlit as st
st.header('User Input Parameters')

First_integer=st.number_input("1st Integer")
Second_integer=st.number_input("2nd Integer")
Third_integer=st.number_input("3rd Integer")

# Check which number is the largest
if (First_integer >= Second_integer) and (First_integer >= Third_integer):
    st.write("The largest value  is ", First_integer)
elif (Second_integer >= First_integer) and (Second_integer >= Third_integer):
    st.write("The largest value is " , Second_integer )
else:
    st.write("The largest value is " ,Third_integer )
