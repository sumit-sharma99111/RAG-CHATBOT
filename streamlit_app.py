import streamlit as st
from src.ragchain import build_chain
import warnings

warnings.filterwarnings("ignore")

# 🔥 Force dark theme using custom CSS
st.set_page_config(
    page_title="RBI RAG Chatbot",
    page_icon="🏦",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Inject dark theme styles manually
dark_theme_css = """
<style>
body {
    background-color: #0E1117;
    color: #FAFAFA;
}
.stApp {
    background-color: #0E1117;
}
div[data-testid="stChatMessage"] {
    background-color: #262730;
    color: #FAFAFA;
    border-radius: 10px;
    padding: 10px;
}
div[data-testid="stChatInput"] textarea {
    background-color: #262730;
    color: white;
}
</style>
"""

st.markdown(dark_theme_css, unsafe_allow_html=True)
# 🏦 --- TITLE ---
st.title("🏦 RBI RAG Chatbot")
st.caption("An AI assistant trained on RBI notifications and documents.")

# 🔗 --- LOAD CHAIN ---
@st.cache_resource
def load_chain():
    chain, _ = build_chain(k=4)
    return chain

try:
    chain = load_chain()
except Exception as e:
    st.error(f"❌ Failed to load model or index. Run ingestion first.\n\nDetails: {e}")
    st.stop()

# 💬 --- CHAT HISTORY ---
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 🧠 --- USER INPUT ---
query = st.chat_input("Type your question here...")

if query:
    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.markdown(query)

    try:
        with st.chat_message("assistant"):
            with st.spinner("🤔 Thinking..."):
                # Try invoke(), fallback to direct call
                try:
                    response = chain.invoke(query)
                except AttributeError:
                    response = chain(query)

                # Extract clean answer
                answer = (
                    response.content.strip()
                    if hasattr(response, "content")
                    else str(response)
                )

                st.markdown(answer)
                st.session_state.messages.append({"role": "assistant", "content": answer})

    except Exception as e:
        st.error(f"❌ Error while answering: {e}")

# 🧾 --- FOOTER ---
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:gray;'>© 2025 RBI RAG Chatbot | Powered by LangChain + Gemini</p>",
    unsafe_allow_html=True,
)
