import streamlit as st
import functions

todos=functions.get_todos()
def add_todo():
    todo=st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox_key = f"checkbox_{index}"
    checkbox=st.checkbox(todo, key=checkbox_key)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[checkbox_key]
        st.experimental_rerun()

st.text_input(label="",placeholder="Add new todo....",
              on_change=add_todo,key='new_todo')