import streamlit as st

from src.langgraph_agenticai.ui.streamlit.loadui import LoadStreamlitUI

def load_langgraph_agenticai_app():
    """
    loads and runs the langgraph agenticai application with streamlit UI.
    
    
    """
    ## load UI
    ui =LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error('Error: Failed to load user input from the UI.')
        return
    

    user_message = st.chat_input("Enter your messsage")
