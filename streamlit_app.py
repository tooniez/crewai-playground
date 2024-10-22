
import streamlit as st



if __name__ == "__main__":
    st.set_page_config(page_icon="🤖", layout="wide")

    st.title("CrewAI Playground")
    st.subheader("Explore AI-powered applications using CrewAI", divider="rainbow")

    st.markdown("""
    Welcome to the CrewAI Playground! This application showcases the power of CrewAI in creating intelligent, collaborative AI systems.

    ## What is CrewAI?

    CrewAI is a framework for orchestrating role-playing AI agents. It allows multiple AI agents to work together, each with specific roles and goals, to solve complex tasks.

    ## Available Applications

    Currently, we have the following application available:

    1. **AI Travel Planner**: Let AI agents plan your next vacation! 
    [Go to Travel Planner](/Travel_Planner)

    ## Get Started

    Click on the link above to try out the AI Travel Planner. More applications will be added in the future, so stay tuned!
    """)

    st.sidebar.success("Select an application above.")