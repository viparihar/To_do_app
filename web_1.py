import streamlit as st
import functions

todos = functions.get_todos("todos.txt")

st.title("My Todo App")
st.subheader("This is my Todo app")
st.write("This app is to increase your productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label = "Enter a todo",placeholder = "Add new todo...")


