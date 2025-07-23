from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.llms import Ollama
import logging

# llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
llm = Ollama(model="llama2")
logger = logging.getLogger(__name__)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful support assistant. Use the context to write a response."),
    ("human", "Ticket:\n{ticket}\n\nContext:\n{context}")
])


def generate_draft(state):
    ticket = state.ticket.dict()
    logger.info("Generating draft response...")
    context = "".join(state.context)
    chain = prompt | llm
    response = chain.invoke({"ticket": ticket, "context": context})
    draft = response.strip()
    logger.info("Draft generated.")
    return state.copy(update={"draft": draft})
