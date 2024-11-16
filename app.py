import streamlit as st
favourtite_colour = st.text_input("favourtite_colour:")
favorite_animal = st.text_input ("favorite animal:")
you_number = st.number_input("your lucky number:")
superpower = st.selectbox("choose your superpower:", ["fly", "teleport","jumper"])
superhero_name = st.write(f"{favourtite_colour} {favorite_animal} of {you_number}")
