import streamlit as st
from src.langgraph_agenticai.LLMs.groqllm import GroqLLM
from src.langgraph_agenticai.graph.graph_builder import GraphBuilder
from src.langgraph_agenticai.ui.streamlit.display_result import DisplayResultStreamlit
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
    

    user_message = st.chat_input("Enter your messsage:")

    if user_message:
        try:
            ## configure the LLM
            obj_llm_config = GroqLLM(user_controls_input=user_input)
            model = obj_llm_config.get_llm_model()

            if not model:
                st.error("Error: LLM model could not be initialised")
                return 
            
            usecase = user_input.get("selected_usecase")
            if not usecase:
                st.error('Error: No usecase selected')


            ## Graph builder
            graph_builder=GraphBuilder(model)
            try:
                graph = graph_builder.setup_graph(usecase)
                print(user_message)
                DisplayResultStreamlit(usecase,graph,user_message).display_result_on_ui()
            except Exception as e:
                st.error(f"Error:Graph set up failed- {e}")
                return


        except Exception as e:
            st.error(f"Error: Graph set up failed {e}")
            return

        

