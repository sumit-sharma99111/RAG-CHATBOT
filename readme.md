🏦 RBI RAG Chatbot
A Retrieval-Augmented Generation (RAG) system using LangChain, FAISS & Gemini
🚀 Overview

The RBI RAG Chatbot is an AI assistant that reads official RBI PDFs and answers user questions directly from those documents.

No hallucination.
No guessing.
Only PDF-based verified answers.

This chatbot automatically:

Downloads the RBI PDF

Extracts all text

Splits into meaningful chunks

Converts chunks into embeddings (text-embedding-004)

Stores them in a FAISS vector database

Retrieves the most relevant chunks

Sends them to Gemini 2.5 Flash

Generates an accurate answer based only on the PDF

A clean, simple UI is built using Streamlit.

🧠 Why RAG?

RAG = Retrieval Augmented Generation

It improves accuracy by giving the LLM real verified context, instead of letting it guess.

In this project, the “context” is always the RBI document.

✔ Reduces hallucinations
✔ Uses real regulatory content
✔ Gives fact-based answers

📂 Project Structure
RBI_RAG_Project/
│
├── src/
│   ├── ingest.py           # Pipeline to download PDF, split text & create FAISS index
│   ├── ragchain.py         # Creates RAG chain (retriever + prompt + LLM)
│   ├── chat_cli.py         # Terminal-based chatbot
│   └── utils.py            # API key loader, folder paths
│
├── streamlit_app.py        # Full Streamlit UI chatbot
├── evaluate.py             # Evaluation script to test sample questions
├── .env                    # API key (not uploaded)
├── requirements.txt        # All dependencies
├── start_chatbot.bat       # 1-click auto-start file for Streamlit app
└── README.md               # This file

1 Create Virtual Environment
python -m venv .venv

2 Activate Virtual Environment

Windows:

.\.venv\Scripts\activate

3 Install Requirements
pip install -r requirements.txt

4 Add API Key

Inside .env file:

GOOGLE_API_KEY=your_api_key_here

📥 Run Ingestion Pipeline

This step downloads the RBI PDF, splits it into chunks, creates embeddings, and stores them in FAISS.

python -m src.ingest


This will create:

artifacts/index/

🤖 Run Chatbot (Terminal Version)
python -m src.chat_cli

🌐 Run Streamlit UI (Web App)
streamlit run streamlit_app.py


Or simply double-click:

start_chatbot.bat

🖥️ Streamlit UI Preview
🏦 RBI RAG Chatbot  
Ask any RBI-related question...


🧩 Tech Stack
Component	Technology
LLM	Gemini 2.5 Flash
Embeddings	text-embedding-004
Framework	LangChain
Vector DB	FAISS
UI	Streamlit
PDF Processing	PyPDFLoader
Language	Python
🛠️ How It Works (Full Flow)

User asks a question

Question → converted to embedding

FAISS retrieves top-k similar chunks

Relevant chunks + question → Gemini

Gemini generates answer only using the PDF context

📊 Evaluation

Use this command:

python evaluate.py


The script tests multiple RBI FAQ questions and prints accuracy.

🔮 Future Improvements

Add multiple RBI PDFs

Multi-PDF retrieval

Chat history aware responses

Document upload feature

Deploy on cloud with Streamlit Hosting

👤 Author

Sumit
AI / GenAI Developer
LinkedIn: https://www.linkedin.com/in/sumit-sharma-58b169350/?isSelfProfile=true

⭐ If you find this project helpful

Give it a Star ⭐ on GitHub — it motivates me to build more AI projects!

