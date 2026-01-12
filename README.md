# PDFfusion 📄✨

**"Don't just read — ask."**

PDFfusion is a modern, AI-powered web application that allows users to upload PDF documents and ask questions about their content . Built with Flask and LangChain, it provides an intuitive chat interface for document analysis.

<img width="1920" height="972" alt="Screenshot (85)" src="https://github.com/user-attachments/assets/f62941bd-03d4-4aa0-82f1-389106eaf7f3" />


## 🌟 Features

- **Smart PDF Analysis**: Upload any PDF and get intelligent answers to your questions
- **Wikipedia Integration**: Access external knowledge through Wikipedia API for comprehensive answers
- **Dual Processing Modes**: Choose between simple QA chain or advanced agent-based processing
- **Modern UI**: Beautiful, responsive interface with animated particles and glassmorphism design
- **Drag & Drop Upload**: Easy file upload with visual feedback
- **Real-time Chat**: Interactive chat interface for seamless Q&A experience
- **Local AI Processing**: Uses Ollama for privacy-focused, local AI processing
- **Vector Search**: Efficient document retrieval using ChromaDB for accurate context
- **Agentic RAG**: Advanced Retrieval-Augmented Generation with intelligent agent decision-making
- **Simple QA Chain**: Efficient question-answering using retrieval-augmented generation


## 🛠️ Technologies Used

- **Backend**: Flask (Python)
- **AI/ML**: LangChain, Ollama (Llama 3.1)
- **RAG Architecture**: Agentic RAG with tool integration and simple rag also (options)
- **External Knowledge**: Wikipedia API integration
- **Vector Database**: ChromaDB
- **PDF Processing**: PyPDF2
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Custom CSS with animations and modern design

## 📋 Prerequisites

Before running PDFfusion, make sure you have:

- Python 3.8 or higher
- [Ollama](https://ollama.ai/) installed and running
- Llama 3.1 model downloaded via Ollama

### Installing Ollama and Llama 3.1

```bash
# Install Ollama (macOS/Linux)
curl -fsSL https://ollama.ai/install.sh | sh

# Pull Llama 3.1 model
ollama pull llama3.1

# Start Ollama service
ollama serve
```

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/pdffusion.git
   cd pdffusion
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create required directories**
   ```bash
   mkdir uploads templates
   ```

5. **Move HTML template**
   ```bash
   # Make sure index.html is in the templates/ directory
   mv index.html templates/
   ```

## 📦 Dependencies

Create a `requirements.txt` file with:

```txt
Flask==2.3.3
langchain==0.1.0
langchain-community==0.0.10
langchain-ollama==0.1.0
langchain-text-splitters==0.0.1
PyPDF2==3.0.1
chromadb==0.4.18
requests==2.31.0
wikipedia==1.4.0
```

## 🚀 Usage

1. **Start the application**
   ```bash
   python app.py
   ```

2. **Open your browser**
   Navigate to `http://localhost:5000`

3. **Upload a PDF**
   - Click the upload area or drag & drop a PDF file
   - Supported format: PDF only

4. **Ask questions**
   - Type your question in the chat input
   - Get AI-powered answers based on the PDF content

## 📁 Project Structure

```
pdffusion/
├── app.py              # Main Flask application
├── lang.py             # LangChain processing logic
│                       # - Simple QA Chain
│                       # - Agentic RAG with Wikipedia
│                       # - PDF processing utilities
├── templates/
│   └── index.html      # Frontend template
├── uploads/            # Temporary file storage
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## ⚙️ Configuration

The application uses the following default settings:

- **Upload folder**: `uploads/`
- **Ollama model**: `llama3.1`
- **Processing modes**: 
  - Simple QA Chain (default in current setup)
  - Agentic RAG with Wikipedia integration (available in code)
- **Chunk size**: 1000 characters
- **Chunk overlap**: 200 characters
- **Vector search results**: Top 3 relevant chunks
- **Wikipedia search**: Top 1 result, max 200 characters

### Switching Between Processing Modes

The application includes two processing approaches:

1. **Simple QA Chain** (`process_pdf_question_simple`): 
   - Fast, direct PDF-only processing
   - Currently used in `app.py`

2. **Agentic RAG** (`process_pdf_question_with_agent`):
   - Advanced agent with PDF retriever + Wikipedia tools
   - Makes intelligent decisions about which sources to use
   - To enable: Change `app.py` import to use `process_pdf_question_with_agent`

## 🔄 Future Enhancements

- [ ] Support for multiple PDF uploads
- [ ] Additional external knowledge sources (beyond Wikipedia)
- [ ] Document comparison features
- [ ] Export conversation history
- [ ] Advanced search filters
- [ ] Support for other document formats (DOCX, TXT)
- [ ] User authentication and session management
- [ ] Cloud deployment options
- [ ] Custom agent tools and workflows

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 Contact

**Author** - Khushi Kumari

⭐ If you found this project helpful, please give it a star!
