import streamlit as st

# Título y autor
st.title("Mi primera app")
st.write("Esta app fue elaborada por Samuel Palomino")

# Preguntar al usuario su nombre
nombre_usuario = st.text_input("Por favor, ingresa tu nombre")

# Saludar al usuario
if nombre_usuario:
    st.write(f"Hola {nombre_usuario}, te doy la bienvenida a mi primera app.")
