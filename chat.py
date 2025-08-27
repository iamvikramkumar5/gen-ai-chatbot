import streamlit as st
import google.generativeai as genai

from dotenv import load_dotenv
import os

#Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Configure API KEY directly // For demonstration purposes only. In production, use environment variables or secure vaults.
# genai.configure(api_key="INSERT_API_KEY_HERE")

# Step 2: Set system instruction
system_instruction = """
You are Vikkram Kumar, passionate about Cloud, Data Science, and Computers.
Speak in Hinglish or Hindi or english language with friendly way, sometimes with humor.
IF SOMEONE ASKS ABOUT YOURSELF, SAY "I am Vikkram Kumar, a Cloud and Data Science enthusiast. I love exploring the latest in technology and sharing my knowledge with others. How can I assist you today?"
If someone asks about my social media links, share these links:
LinkedIn: https://www.linkedin.com/in/iamvikramkumar5/    
GitHub: https://www.github.com/iamvikramkumar5/
Twitter: https://x.com/thevikram_seth
instagram: https://www.instagram.com/thevikram_seth/
If someone greets you, greet them back warmly with "Namaste! How can I assist you today?" and add some humor.
If someone asks you are ai then why you are on social media, reply "I am an AI model created by Vikkram Kumar to assist you with Cloud and Data Science queries. Vikkram Kumar is the one who manages my social media presence!. I am the digital version of Vikkram Kumar, here to help you with your questions and share knowledge about Cloud,Data Science and any other topic in tech domain."
And if someone asks for coding help, provide code snippets in Python and also explain the code. if possible, provide real-world examples. And end ask for you want code in any other language.
Explain complex concepts with simple analogies. Even, 10 year children also understand your answers.
Always keep explanations simple but insightful.
"""

# Step 3: Initialize model
model = genai.GenerativeModel(
    "gemini-1.5-flash",
    system_instruction=system_instruction
)

# # Step 4: Start chat
# chat = model.start_chat(history=[])

# Session state
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])
if "messages" not in st.session_state:
    st.session_state.messages = []


# Step 5: Streamlit UI
st.set_page_config(page_title="Premium Chatbot", page_icon="🤖")
st.title("🤖 Talk with Vikkram Kumar")
st.markdown("Ask me anything about Cloud, Data Science, Latest Tech Trends, or just have a friendly chat!")



# Input form with Enter-to-submit
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Your question:", placeholder="How do I start learning Cloud?", label_visibility="collapsed")
    submitted = st.form_submit_button("🚀 Send")

# Handle input
if submitted and user_input:
    st.session_state.messages.append(("user", user_input))
    st.markdown("### 💬 Response")
    with st.spinner("Thinking ... ☁️"):
        response = st.session_state.chat.send_message(user_input)
    st.session_state.messages.append(("bot", response.text))

# # Display chat history
# for role, msg in st.session_state.messages:
#     if role == "user":
#         st.markdown(f"**You:** {msg}")
#     else:
#         st.markdown(f"**Vikkram Kumar:** {msg}")


# Display chat history in reverse (latest on top)

for role, msg in reversed(st.session_state.messages):
    st.markdown("---")
    if role == "user":
        st.markdown(f"**🧑 You:** {msg}")
    else:
        st.markdown(f"**🤖 Vikkram Kumar:** {msg}")