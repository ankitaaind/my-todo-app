import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    if "new_todo" in st.session_state:
        todo = st.session_state["new_todo"].strip()
        if todo:
            todos.append(todo + "\n")
            functions.write_todos(todos)
        st.session_state["new_todo"] = ""


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

new_todo = st.text_input(label=" ", placeholder="Add a new todo...",
                         key="new_todo")
if st.button("Add Todo"):
    add_todo()
