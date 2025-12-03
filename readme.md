# 🏦 RBI RAG Chatbot

A Retrieval-Augmented Generation (RAG) chatbot built using **LangChain**, **Google Gemini**, **FAISS**, and **Streamlit**.

---

## 🚀 Features
- Answers questions from RBI PDF documents
- Uses FAISS for vector search
- Streamlit UI for interactive chat
- Secure `.env` for API keys
- 1-click launcher (`start_chatbot.bat`)

---

## 🧠 How to Run

### 1️⃣ Setup Environment
```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt


### 2️⃣ Run Ingestion
python -m src.ingest

### 3️⃣ Run Chatbot (2 options)
UI (Recommended) → double-click or run code of start_chatbot.bat

CLI → python -m src.chat_cli

### 🧩 **Step 4 — Verify everything works**

Just do one final check before zip:

```bash
streamlit run streamlit_app.py
If it opens in browser → ✅ perfect.

### Step 5 — Creating ZIP.


⚙️ Requirements
See requirements.txt.


💡 Credits
Built by Sumit Sharma for an interview demonstration.
Powered by Google Gemini & LangChain RAG.
