# OFFLINE AI CHATBOT
**PBL project made by DEEP KIRAN KAUR**

This project is a standalone, offline AI chatbot application designed to run Large Language Models (LLMs) specifically on your local Windows machine without requiring an internet connection.

### Features
1. **Offline Chatbot**: Chat with AI models locally on your device.
2. **Local RAG (Retrieval Augmented Generation)**: Upload your own PDF or DOCX documents and ask questions based on their content.
3. **Private & Secure**: No data collection, no trackers, and fully functional offline.
4. **Markdown Support**: Responses are rendered with proper formatting.

### Quick Start
To run the application:
1. Ensure you have Python installed.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python main.py
   ```
   
### Models
The application supports various optimized ONNX models including `SmolLM2` and `Gemma3` for chat, and `all-MiniLM-L6-V2` for document embeddings.
