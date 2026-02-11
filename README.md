# LangChain Learning

My journey learning LangChain chains with practical, working examples.

## Concepts

**Simple Chain** — Prompt → Model → Output. The basics of how LangChain works.

**Sequential Chain** — Chain multiple steps together. Output of one becomes input to the next.

**Parallel Chain** — Run multiple processes at the same time. Combine their results.

**Conditional Chain** — Execute different chains based on logic. Think of it as if-else for LLMs.

## Setup

```bash
# Clone the repo
git clone https://github.com/15utkarsh15/LangChain.git
cd LangChain

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Configuration

Add your OpenAI API key to a `.env` file:

```
OPENAI_API_KEY=your_key_here
```

## Run Examples

```bash
python simple_chain.py
python sequential_chain.py
python parallel_chain.py
python conditional_chain.py
```

Each script shows the results and visualizes the chain structure.

## Files

- `simple_chain.py` — Getting started with chains
- `sequential_chain.py` — Multi-step processing 
- `parallel_chain.py` — Running things concurrently
- `conditional_chain.py` — Smart branching with LLMs
