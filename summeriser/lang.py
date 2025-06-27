# Alternative Simple Solution - lang_simple.py
# This version fixes the chain compatibility issues

import os
from langchain.schema import Document
from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

# Use the updated imports
try:
    from langchain_ollama import OllamaEmbeddings, ChatOllama
except ImportError:
    from langchain_community.embeddings import OllamaEmbeddings
    from langchain_community.chat_models import ChatOllama

from langchain_community.vectorstores import Chroma

# Initialize models
embedding = OllamaEmbeddings(model="llama3.1")
llm = ChatOllama(model="llama3.1", temperature=0)

def pdf_extract(pdf_path):
    """Extract text from PDF file"""
    text = ""
    try:
        pdf_reader = PdfReader(pdf_path)
        for page in pdf_reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"
    except Exception as e:
        raise Exception(f"Error reading PDF: {str(e)}")
    
    if not text.strip():
        raise Exception("No text found in PDF")
    
    return text

def get_text_chunk(text):
    """Split text into chunks"""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, 
        chunk_overlap=200
    )
    
    text_chunks = splitter.split_text(text)
    chunks = [Document(page_content=chunk, metadata={"source": "pdf"}) 
              for chunk in text_chunks if chunk.strip()]
    
    return chunks

def create_agent_with_tools(chunks):
    """Create an agent with both PDF retriever and Wikipedia tools"""
    try:
        # Create vector store and retriever
        vectordb = Chroma.from_documents(chunks, embedding)
        retriever = vectordb.as_retriever(search_kwargs={"k": 3})
        
        # Wikipedia tool
        from langchain_community.tools import WikipediaQueryRun 
        from langchain_community.utilities import WikipediaAPIWrapper
        api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=200)
        wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)

        # Retriever tool
        from langchain.tools.retriever import create_retriever_tool
        retriever_tool = create_retriever_tool(
            retriever,
            "pdf_context",
            "Search for context related to user query from the uploaded PDF document"
        )
        
        tools = [wiki_tool, retriever_tool]
        
        # Create agent
        from langchain.agents import initialize_agent, AgentType
        agent = initialize_agent(
            tools=tools,
            llm=llm,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            handle_parsing_errors=True,
            verbose=True
        )
        
        return agent
        
    except Exception as e:
        raise Exception(f"Error creating agent: {str(e)}")

def create_simple_qa_chain(chunks):
    """Create a simple QA chain for PDF context only"""
    try:
        # Create vector store
        vectordb = Chroma.from_documents(chunks, embedding)
        retriever = vectordb.as_retriever(search_kwargs={"k": 3})
        
        # Create custom prompt
        prompt_template = """
        Use the following pieces of context to answer the question at the end. 
        If you don't know the answer based on the context, just say that you don't know, 
        don't try to make up an answer.

        Context: {context}

        Question: {question}
        
        Answer:"""
        
        PROMPT = PromptTemplate(
            template=prompt_template, 
            input_variables=["context", "question"]
        )
        
        # Create RetrievalQA chain
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=retriever,
            chain_type_kwargs={"prompt": PROMPT},
            return_source_documents=False
        )
        
        return qa_chain
        
    except Exception as e:
        raise Exception(f"Error creating QA chain: {str(e)}")

def ask_question_agent(agent, question):
    """Ask a question using the agent"""
    try:
        # Use invoke for newer versions, run for older versions
        try:
            result = agent.invoke({"input": question})
            return result.get("output", str(result))
        except AttributeError:
            # Fallback for older versions
            result = agent.run(question)
            return result
            
    except Exception as e:
        raise Exception(f"Error asking question: {str(e)}")

def ask_question_qa(qa_chain, question):
    """Ask a question using the QA chain"""
    try:
        # Use invoke for newer versions
        try:
            result = qa_chain.invoke({"query": question})
            return result.get("result", str(result))
        except AttributeError:
            # Fallback for older versions
            result = qa_chain.run(question)
            return result
            
    except Exception as e:
        raise Exception(f"Error asking question: {str(e)}")

def process_pdf_question_with_agent(pdf_path, question):
    """Process PDF and answer question using agent with both PDF and Wikipedia access"""
    try:
        # Extract text
        text = pdf_extract(pdf_path)
        print(f"Extracted {len(text)} characters from PDF")
        
        # Create chunks
        chunks = get_text_chunk(text)
        print(f"Created {len(chunks)} chunks")
        
        # Create agent with tools
        agent = create_agent_with_tools(chunks)
        print("Agent created successfully")
        
        # Ask question
        answer = ask_question_agent(agent, question)
        print(f"Generated answer: {answer[:100]}...")
        
        return answer
        
    except Exception as e:
        raise Exception(f"Error processing PDF question with agent: {str(e)}")

def process_pdf_question_simple(pdf_path, question):
    """Process PDF and answer question using simple QA chain"""
    try:
        # Extract text
        text = pdf_extract(pdf_path)
        print(f"Extracted {len(text)} characters from PDF")
        
        # Create chunks
        chunks = get_text_chunk(text)
        print(f"Created {len(chunks)} chunks")
        
        # Create QA chain
        qa_chain = create_simple_qa_chain(chunks)
        print("QA chain created successfully")
        
        # Ask question
        answer = ask_question_qa(qa_chain, question)
        print(f"Generated answer: {answer[:100]}...")
        
        return answer
        
    except Exception as e:
        raise Exception(f"Error processing PDF question: {str(e)}")