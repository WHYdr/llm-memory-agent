# llm-memory-agent

## Project Goal
This project aims to build a long-term memory AI agent.

The agent can:
- chat with users
- store important memories
- retrieve past conversations
- maintain long-term context
- support future extensions such as tools and planning

The project is designed as a learning-oriented LLM system for studying:
- memory systems
- retrieval augmented generation (RAG)
- agent workflows
- long-context interaction

## Workflow

1. User sends a message
2. The system embeds the message
3. Relevant memories are retrieved
4. Context is injected into the prompt
5. LLM generates a response
6. Important information is stored into memory

## Current Functionality
- [x] Basic chat interface
- [ ] Long-term memory
- [ ] Vector database retrieval
- [ ] Conversation summarization
- [ ] Tool usage

## System Structure (Design Goal)
The system currently contains the following modules:

- Chat Module
  Handles user interaction.

- LLM Module
  Use Ollama run local LLM model.

- Memory Module
  Stores and retrieves conversation history.

- Embedding Module
  Converts text into vector embeddings.

- Retrieval Module
  Searches relevant memories from the vector database.

User Input
    ↓
Embedding
    ↓
Vector Search
    ↓
Retrieve Memories
    ↓
Prompt Assembly
    ↓
LLM
    ↓
Response
    ↓
Store New Memory

## Tech Stack
- Python
- Ollama, Llama/Qwen
- LangChain
- ChromaDB
- HuggingFace Transformers
- sentence-transformers
- VSCode

## Road Map

### V1
- Basic chat system
- Local LLM integration
- Conversation storage

### V2
- Long-term memory
- Embedding retrieval
- Semantic search

### V3
- Tool usage
- File reading
- Multi-session memory

### V4
- Autonomous planning
- Multi-agent collaboration

## TO-DO
- [ ] Set up project structure
- [ ] LLM integration
- [ ] Build chat loop
- [ ] Save conversation history
- [ ] Add embedding model
- [ ] Integrate ChromaDB

## How to Run
Coming soon.
