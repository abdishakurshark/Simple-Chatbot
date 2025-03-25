import streamlit as st
# Install Streamlit on CMD or on colab
# !pip install streamlit

def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input:
        return "Hello! How can I assist you today?"
    elif "help" in user_input:
        return "Sure! What do you need help with?"
    elif "services" in user_input:
        return "We offer a range of services, including support, custom products, and more."
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "Sorry, I didn't understand that. Can you please rephrase?"

# Streamlit App
st.title("Simple Chatbot")
st.write("Welcome! Type your message below and chat with the bot.")

# User input
user_input = st.text_input("You:", "")

if user_input:
    response = chatbot_response(user_input)
    st.text_area("Chatbot:", response, height=100, disabled=True)

# Run the app using: streamlit run filename.py

# ! wget -q -O - ipv4.icanhazip.com
