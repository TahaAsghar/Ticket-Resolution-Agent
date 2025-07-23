# 🛠️ Support Ticket Resolution Agent (LangGraph)

This project implements a multi-step AI support ticket agent using the LangGraph framework. It receives a support ticket, classifies it, retrieves context, drafts a response, reviews it, and retries or escalates if necessary.

## 📦 Features

- ✅ LLM-based classification (Billing, Technical, Security, General)
- ✅ Contextual retrieval (mocked RAG using local `.txt` files)
- ✅ Draft generation using GPT-3.5
- ✅ Automated review with feedback loop
- ✅ Retry up to 2 times on failure
- ✅ Escalation to CSV if all retries fail

## 📁 Project Structure

support_ticket_agent/
├── .env
├── main.py
├── graph_def.py
├── models.py
├── README.md
├── escalation_log.csv
├── sample_docs/
│ ├── billing.txt
│ ├── technical.txt
│ ├── security.txt
│ └── general.txt
└── nodes/
├── classifier.py
├── drafter.py
├── escalate.py
├── retriever.py
└── reviewer.py


## .env
OPENAI_API_KEY=sk-...

## 🧪 Requirements

uv add langgraph-cli[inmem] langchain openai python-dotenv


## 🚀 Run with LangGraph CLI
   langgraph dev

## 🧠 How It Works
classify: Categorizes ticket using GPT

retrieve: Loads static docs from sample_docs/

draft: Generates response using ticket + context

review: Approves or rejects draft

If rejected → retry with feedback (max 2)

If still failing → escalate and log