import streamlit as st
from streamlit import checkbox

import functions

todos = functions.get_todos("todos.txt")
col1,col2,col3 = st.columns(3)
def add_todo():
    todo = st.session_state["new_todo"]+'\n' #session_state is a dictionary which stores the key value of the input box
    # After pressing enter after typing something in the input box,
    # todo variable stores that value
    todos.append(todo)
    functions.write_todos(todos,"todos.txt")
    st.session_state["new_todo"] = ''



st.title("My Todo App")
st.subheader("This is my Todo app")
st.write("This app is to increase your productivity")

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos,'todos.txt')
        del st.session_state[todo]
        st.rerun()  # It reruns the entire script

st.text_input(label = "Enter a todo",placeholder = "Add new todo...",
              on_change=add_todo,key='new_todo')

st.session_state

