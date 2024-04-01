import streamlit as st
name = st.text_input('Enter the of the friend whom you want wish')
st.title("HBD wishes")

def HBD(name):
  return(f"Happy Birthday {name}. \n May god bless you with abundance")

wish = HBD(name)
st.write(wish)
