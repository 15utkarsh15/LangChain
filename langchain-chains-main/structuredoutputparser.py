from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field

load_dotenv()

# Define structured output schema using Pydantic
class Facts(BaseModel):
    fact_1: str = Field(description="Fact 1 about the topic")
    fact_2: str = Field(description="Fact 2 about the topic")
    fact_3: str = Field(description="Fact 3 about the topic")

# Create model with structured output
model = ChatOpenAI().with_structured_output(Facts)

# Prompt
template = PromptTemplate(
    template="Give 3 facts about {topic}",
    input_variables=["topic"],
)

chain = template | model

result = chain.invoke({"topic": "Zombies"})

print(result)
