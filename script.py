import streamlit as st
from google import genai # Assuming you've imported the SDK client here

# --- Configuration (Add your API Key) ---
# NOTE: Replace 'YOUR_API_KEY' with your actual key or load it from environment variables
try:
    client = genai.Client(api_key=st.secrets["API_KEY"]) 
except Exception as e:
    st.error(f"Error initializing GenAI Client: {e}")
    st.stop()


st.title("🤖 I am your fiancial assistant")

st.write("**Let's Explore, Financial Analysis, Cedit Risk and Asset Valuations!**")

# --- User Input and Processing ---
user_input = st.text_input("Ask a finance question:", key="user_prompt")

if st.button("Submit", use_container_width=True):
    if user_input:
        with st.spinner("Z-BOT is Thinking..."):
            try:
                # 1. Define the system instruction and other configuration
                config = {
                    "system_instruction": "You are an expert in finance, financial modeling, valuations and economics who only answers queries related to financial analysis, finance topics, valuation, credit risk analysis, IFRS-9. If a query is not related to finance, politely state that you can only assist with relevant topics and always explain your answers in detail with examples.",
                }
                
                # 2. Call the API with the model, user content, and configuration
                response = client.models.generate_content(
                    model='gemini-2.5-flash', 
                    contents=user_input, # The content (user's prompt)
                    config=config          # The configuration, including the system instruction
                )
                
                # 3. Display the response
                st.subheader("Z-BOT Response:")
                st.write(response.text)
                
            except Exception as e:
                st.error(f"An error occurred during API call: {e}")
    else:

        st.warning("Please enter a question first!")

