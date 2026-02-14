# LangChain Learning
LangChain Learning 🚀

This repository documents my journey learning LangChain by building small, practical, and working examples.

Instead of just reading documentation, I wanted to understand how chains actually work — so this repo contains simple scripts that demonstrate each core chaining pattern clearly.

If you're learning LangChain too, this might help you think in “LLM workflows” rather than just prompts.

🛠 Tech Stack

Python 3.9+

LangChain

OpenAI API

python-dotenv

⚙️ Setup
1️⃣ Clone the repository
git clone https://github.com/15utkarsh15/LangChain.git
cd LangChain

2️⃣ Create a virtual environment (recommended)
python -m venv venv


Activate it:

Mac/Linux

source venv/bin/activate


Windows

venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

🔐 Configuration

Create a .env file in the root directory:

OPENAI_API_KEY=your_openai_api_key


Make sure you have an API key from OpenAI.

▶️ Run the Examples
python simple_chain.py
python sequential_chain.py
python parallel_chain.py
python conditional_chain.py


Each script:

Executes the chain

Prints the output

Shows how the chain is structured

🎯 Why I Built This

I built this repository to:

Understand how chaining really works

Move beyond basic prompting

Think in structured AI workflows

Prepare for building larger LLM applications
