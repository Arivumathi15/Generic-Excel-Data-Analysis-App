import pandas as pd
import os
import streamlit as st
from langchain.agents import AgentType
from langchain_openai import ChatOpenAI
from langchain_experimental.agents import create_pandas_dataframe_agent
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Set your OpenAI API key from environment
openai_api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI client (if needed)
client = OpenAI(api_key=openai_api_key)

# Initialize the chat model
llm = ChatOpenAI(
    temperature=0,
    model="gpt-4o",  # Adjust model as needed
    openai_api_key=openai_api_key,
    streaming=True
)

# ----------------------------
# Helper Functions
# ----------------------------

@st.cache_data
def load_excel_data(file):
    """
    Loads an Excel file (which may contain single or multiple sheets) into a dictionary.
    Keys are sheet names and values are pandas DataFrames.
    """
    try:
        excel_data = pd.read_excel(file, sheet_name=None)
        return excel_data
    except Exception as e:
        st.error(f"Error loading Excel file: {e}")
        return None

def chat_with_dataframe_generic(df, query):
    """
    Creates a LangChain agent for the provided DataFrame and sends a query.
    """
    pandas_df_agent = create_pandas_dataframe_agent(
        llm,
        df,
        verbose=True,
        agent_type=AgentType.OPENAI_FUNCTIONS,
        allow_dangerous_code=True  # Use with caution
    )

    messages = [
        {
            "role": "system", 
            "content": (
                "You are an experienced data analyst. Your job is to provide clear, concise answers "
                "based on the data provided. Interpret the data carefully and answer the user's query."
            )
        },
        {"role": "user", "content": query}
    ]

    response = pandas_df_agent.invoke(messages)
    return response

# ----------------------------
# Streamlit App Interface
# ----------------------------

st.title("Generic Excel Data Analysis App")

# File uploader for Excel files
uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx"])

if uploaded_file is not None:
    st.info("Processing the uploaded file...")
    excel_data = load_excel_data(uploaded_file)

    if excel_data is None:
        st.error("Failed to load Excel data.")
    else:
        # List available sheet names
        sheet_names = list(excel_data.keys())
        st.subheader("Available Sheets")
        sheet_choice = st.selectbox("Select a sheet to view and query", sheet_names)

        # Display the chosen sheet's data
        df_selected = excel_data[sheet_choice]
        st.subheader(f"Data from '{sheet_choice}'")
        st.dataframe(df_selected)

        st.markdown("---")
        st.subheader("Query the Data")
        query = st.text_input("Enter your query about the data", "")

        if st.button("Submit Query"):
            if query.strip() == "":
                st.warning("Please enter a valid query.")
            else:
                try:
                    with st.spinner("Processing your query..."):
                        response = chat_with_dataframe_generic(df_selected, query)
                        st.markdown("### Query Response")
                        # If using OpenAI functions, the output is typically in response['output']
                        st.write(response.get("output", response))
                except Exception as e:
                    st.error(f"Error processing query: {e}")
