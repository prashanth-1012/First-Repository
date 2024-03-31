import streamlit as st
name = st.text_input('Enter the name of the friend whom you want wish')
st.title("HBD wishes")

def HBD(name):
  str.write(f"Happy Birthday {name}. May god bless you with abundance")
