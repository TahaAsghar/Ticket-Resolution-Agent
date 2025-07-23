from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.llms import Ollama
from dotenv import load_dotenv
import logging

load_dotenv()
logger = logging.getLogger(__name__)
# llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
llm = Ollama(model="llama2")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a ticket classifier. Classify the ticket into one of: Billing, Technical, Security, General."),
    ("human", "Subject: {subject}\nDescription: {description}")
])


def classify_ticket(state):
    ticket = state.ticket
    logger.info(f"Classifying ticket: {ticket.subject}")
    chain = prompt | llm
    response = chain.invoke({"subject": ticket.subject, "description": ticket.description})
    category = response.strip().splitlines()[0]
    logger.info(f"Ticket classified as: {category}")
    return state.copy(update={"category": category})
