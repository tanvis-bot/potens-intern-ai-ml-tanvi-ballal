# AI Infrastructure Incident Triage Agent

An AI-powered incident triage system built for the Potens Internship Hiring 2026 Take-Home Assignment.

This project processes free-text operational incidents and produces structured triage decisions using semantic retrieval, tool orchestration, and LLM reasoning.

The system focuses on infrastructure and AI operational workflows including:
- deployment failures
- hallucination incidents
- security alerts
- billing complaints
- infrastructure degradation

---

# Features

## Real Tool Calling
The system uses callable Python tools instead of string-matching shortcuts.

Implemented tools:
1. Similar Incident Search Tool
2. Infrastructure Health Tool
3. Acknowledgment Generator Tool
4. Human Escalation Tool

---

## Structured Triage Output

Each request returns:

```json
{
  "category": "",
  "priority": "",
  "next_tool": "",
  "reasoning": "",
  "why": ""
}
```

Priority levels:
- P0 → Critical
- P1 → Major
- P2 → Minor

---

## Semantic Similarity Search

The project uses SentenceTransformers embeddings for semantic retrieval of historical incidents.

This allows the system to retrieve related incidents even when wording differs.

Example:
- "GPU machines crashing"
- "GPU inference servers failing"

Both retrieve semantically related incidents.

---

## Reasoning Trace Visibility

The full reasoning path is exposed for every decision:
- retrieval steps
- tool usage
- operational checks
- escalation decisions

No silent magic.

---

## Human-in-the-Loop Escalation

Low-confidence or safety-sensitive issues trigger escalation to a simulated human operator.

Examples:
- medical hallucinations
- contradictory legal guidance
- ambiguous incidents

---

# Tech Stack

| Component | Technology |
|---|---|
| Backend API | FastAPI |
| Frontend UI | Streamlit |
| LLM Provider | Groq |
| Embeddings | SentenceTransformers |
| Similarity Search | cosine similarity |
| Language | Python 3.13 |

---

# Architecture

User Input  
→ Similar Incident Retrieval  
→ Infrastructure Status Check  
→ LLM Reasoning  
→ Structured Triage Decision  
→ Optional Human Escalation

---

# Project Structure

```text
triage-agent/
│
├── app.py
├── agent.py
├── prompts.py
├── streamlit_app.py
├── README.md
├── .env
│
├── data/
│   └── incidents.json
│
├── tools/
│   ├── similarity_tool.py
│   ├── status_tool.py
│   ├── draft_tool.py
│   └── escalation_tool.py
│
├── examples/
│   ├── example1.json
│   ├── example2.json
│   ├── ...
│
└── vector_db/
```

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone <your-github-repo>
cd potens-intern-ai-ml-tanvi-ballal
```

---

## 2. Create Virtual Environment

```bash
python3 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install fastapi uvicorn streamlit groq python-dotenv sentence-transformers scikit-learn
```

---

## 4. Configure Environment Variables

Create `.env`

```env
GROQ_API_KEY=your_groq_api_key
```

---

# Running The Project

## Terminal 1 → Backend API

```bash
source venv/bin/activate
python -m uvicorn app:app --reload
```

Backend:
```text
http://127.0.0.1:8000/docs
```

---

## Terminal 2 → Streamlit Frontend

```bash
source venv/bin/activate
streamlit run streamlit_app.py
```

Frontend:
```text
http://localhost:8501
```

---

# Example Inputs

## Infrastructure Incident

```text
GPU inference servers are failing after deployment
```

---

## Security Incident

```text
Suspicious login attempts detected from multiple countries
```

---

## Model Quality Incident

```text
Users are receiving hallucinated medical responses from chatbot
```

---

# Design Decisions

## Why explicit orchestration instead of full autonomous agents?

Initially, the project experimented with LangChain agent abstractions. During implementation, explicit orchestration was chosen instead because:
- easier debugging
- clearer reasoning visibility
- predictable tool execution
- lower framework complexity within a 24-hour constraint

This improved traceability and operational clarity.

---

## Why semantic retrieval?

Semantic embeddings were chosen over keyword matching because infrastructure incidents are often described differently by users while referring to similar operational failures.

---

## Why expose reasoning traces?

The assignment explicitly emphasized “no silent magic”.

The system therefore exposes:
- evidence gathering
- retrieval reasoning
- tool usage
- escalation decisions

for every triage result.

---

# Current Limitations

- Infrastructure health tool uses mocked status responses.
- Embeddings are stored in-memory.
- No persistent vector database yet.
- Confidence scoring is heuristic.
- No authentication or production hardening.
- Limited incident dataset for retrieval.

---

# Future Improvements

- Persistent vector database (ChromaDB/pgvector)
- Confidence scoring calibration
- Async tool execution
- Reranking layer for retrieval
- Incident clustering
- Multi-user operational dashboard
- Real infrastructure telemetry integration

---

# AI Use Log

| Tool | Approx Usage | Purpose |
|---|---|---|
| ChatGPT | ~150 prompts | architecture planning, debugging, FastAPI integration, Streamlit UI |
| Groq API | inference requests | triage reasoning |
| SentenceTransformers | embedding generation | semantic similarity retrieval |

---

# Submission Notes

This project was intentionally kept focused and operational rather than overengineered. The primary goal was building a working, debuggable, and explainable triage workflow within the 24-hour assignment constraint.