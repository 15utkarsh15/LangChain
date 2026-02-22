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

# LangChain Chains — Examples

A small set of Python examples showing simple, sequential, parallel, and conditional chains.

Quick start
- Create a virtual environment and install dependencies:

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Run an example

```powershell
python simple_chain.py
python sequential_chain.py
python parallel_chain.py
python conditional_chain.py
```

What’s here
What’s here
- `simple_chain.py` — a single prompt → model → output example (get started fast)
- `sequential_chain.py` — multiple steps where each output feeds the next
- `parallel_chain.py` — run independent tasks at the same time and combine results
- `conditional_chain.py` — choose different paths based on simple logic

Contributing
- Open issues or pull requests with small, focused changes.

License
- See project files for license details.
