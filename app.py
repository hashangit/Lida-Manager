import streamlit as st
from LidaManager import DataLoader, LidaEDA, LidaChat

# Initialize session states for results if not already done
if 'eda_results' not in st.session_state:
    st.session_state['eda_results'] = "No EDA results to display yet."
if 'chat_results' not in st.session_state:
    st.session_state['chat_results'] = "No chat results to display yet."

# Load data using DataLoader
data_loader = DataLoader()
data = data_loader.load_data()

# Sidebar for 'Chat with Data'
with st.sidebar:
    st.header("Chat with Data")
    user_query = st.text_input("Enter your query here:")
    ask_button = st.button("Ask")

# Initialize session states for managing expanders
if 'expand_eda' not in st.session_state:
    st.session_state['expand_eda'] = False
if 'expand_chat' not in st.session_state:
    st.session_state['expand_chat'] = False

# Main body for 'Exploratory Data Analysis'
st.header("Exploratory Data Analysis")
if st.button("Analyze Data", key="analyze"):
    st.session_state['expand_eda'] = True
    st.session_state['expand_chat'] = False
    lida_eda = LidaEDA(data)
    eda_images = lida_eda.process_data()
    eda_expander = st.expander("EDA Results", expanded=st.session_state['expand_eda'])
    with eda_expander:
        st.write(st.session_state['eda_results'])
        for img in eda_images:
            st.image(img)

# Handling user queries
if ask_button and user_query:
    st.session_state['expand_chat'] = True
    st.session_state['expand_eda'] = False
    lida_chat = LidaChat(data)
    chat_image = lida_chat.process_query(user_query)
    chat_expander = st.expander("Chat Results", expanded=st.session_state['expand_chat'])
    with chat_expander:
        st.write(st.session_state['chat_results'])
        if chat_image:
            st.image(chat_image)
        else:
            st.write("No image to display.")

