import streamlit as st

# --- Page Configuration ---
st.set_page_config(
    page_title = "My Todo App",
    page_icon = "📝",
    layout = "centered"
)

# --- Custom CSS for styling ---
st.markdown(
    """
    <style>
    .title{
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        color: #4CAF50;
    }
    div[data-testid="stTextInput"] label
    div[data-testid="stMarkdownContainer"] p{
        font-size: 24px;
        font-weight: 700;
        color: #4CAF50;
        margin-top: 12px;
        margin-bottom: 6px;
        line-height: 1.4;
    }
    div[data-testid="stTextInput"] input{
        border: 2px solid #4CAF50;
        border-radius: 10px;
        padding: 12px;
        font-size: 16px;
    }
    div[data-testid="stTextInput"] input:focus{
        border-color: #2E7D32;
        box-shadow: 0 0 6px rgba(76, 175, 80, 0.5);
        outline: none;
    }
    div[data-testid="stTextInput"] input::placeholder {
        color: #999999;
        font-style: italic;
    }   
    </style>
    """,
    unsafe_allow_html=True
)


# --- Initialize session state ---
if "tasks" not in st.session_state:
    st.session_state.tasks = []


# --- App title ---
st.markdown('<div class="title">📝 My Todo Application</div>', unsafe_allow_html=True)

# --- input section ---
task_input = st.text_input("Add a new task", placeholder="Type your task here...")

add_button = st.button("➕ Add Task")

if add_button and task_input.strip():
    st.session_state.tasks.append(
        {"task": task_input, "done": False}
    )

st.session_state.tasks

# --- Display section ---
st.write("### Your Tasks")

for index, task in enumerate(st.session_state.tasks):
    col1, col2, col3 = st.columns([0.1, 0.7, 0.2])

    with col1:
        done = st.checkbox("", value=task["done"], key=f"done_{index}")

    with col2:
        if done:
            st.markdown(f"~~{task['task']}~~")
        else:
            st.markdown(task['task'])

    with col3:
        delete = st.button("🗑️", key=f"delete_{index}")

    if done != task['done']:
        st.session_state.tasks[index]['done'] = done

    if delete:
        st.session_state.tasks.pop(index)
        st.rerun()

