from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.llms import Ollama

# llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
llm = Ollama(model="llama2")

prompt = ChatPromptTemplate.from_messages([
    ("system", "Review this response. Return ✅ if approved, ❌ if rejected with feedback."),
    ("human", "{draft}")
])


def review_draft(state):
    chain = prompt | llm
    review = chain.invoke({"draft": state.draft})
    if "✅" in review:
        return state.copy(update={"reviewer_feedback": "✅"})
    else:
        new_context = state.context + [review]
        return state.copy(update={"reviewer_feedback": "❌", "context": new_context})
