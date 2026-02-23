from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

prompt1 = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

model = ChatOpenAI()

parser = StrOutputParser()

prompt2 = PromptTemplate(
    template='Explain the following joke - {text}',
    input_variables=['text']
)

chain = prompt1 | model | parser | prompt2 | model | parser
result = chain.invoke({'topic': 'Impact of AI in job market'})

print(result)

chain.get_graph().print_ascii()
print(chain.invoke({'topic':'AI'}))