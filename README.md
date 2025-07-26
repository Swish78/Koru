# Koru 🌿 Your Second Brain, Reimagined

Koru is a personal knowledge management system designed to help you capture, connect, and rediscover your thoughts. It transforms your notes and ideas into an interactive, interconnected web, allowing you to uncover hidden patterns and insights within your own knowledge base.

## ✨ Key Features

- **Interconnected Notes**: Create notes as "nodes" and form explicit links between them to build a personal knowledge graph.
- **Interactive Graph Visualization**: Navigate your thoughts visually with a dynamic, clickable graph interface.
- **AI-Powered Insights**: Receive smart suggestions for new connections, auto-generate summaries of long notes, and search by concept rather than just keywords.
- **Voice-to-Text**: Capture fleeting thoughts by speaking directly into the app using Whisper-powered transcription.
- **Timeline View**: View your events and ideas laid out chronologically for easy reflection and planning.
- **Secure & Private**: Keep sensitive thoughts separate with a dedicated "Secret" mode, ensuring your privacy.

## 🛠️ Tech Stack
This project leverages modern, scalable technologies—each chosen to run efficiently on free-tier services.

| Category           | Technology      |
|--------------------|-----------------|
| **Frontend**       | React           |
| **Backend**        | Python / FastAPI|
| **User Database**  | PostgreSQL      |
| **Graph Database** | Neo4j AuraDB    |
| **Vector Search**  | Pinecone        |
| **Task Queue**     | Celery + Redis  |
| **Background Worker** | Python / Celery|
| **AI / LLM**       | Groq API        |

## 🚀 Getting Started

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-org/koru.git
   ```

2. **Backend**

   ```bash
   cd koru/backend
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   uvicorn app.main:app --reload
   ```

3. **Frontend**

   ```bash
   cd ../frontend
   npm install
   npm run dev
   ```

Visit `http://localhost:3000` for the frontend and `http://localhost:8000/docs` for the API docs.

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for more details.
```
