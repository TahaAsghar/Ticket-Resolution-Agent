from langgraph.graph import StateGraph
from models import SupportState
from nodes.classifier import classify_ticket
from nodes.retriever import retrieve_context
from nodes.drafter import generate_draft
from nodes.reviewer import review_draft
from nodes.escalate import handle_escalation


def build():
    builder = StateGraph(SupportState)

    builder.add_node("classify", classify_ticket)
    builder.add_node("retrieve", retrieve_context)
    builder.add_node("draft", generate_draft)
    builder.add_node("review", review_draft)
    builder.add_node("escalate", handle_escalation)

    builder.set_entry_point("classify")
    builder.add_edge("classify", "retrieve")
    builder.add_edge("retrieve", "draft")
    builder.add_edge("draft", "review")

    def review_decision(state):
        if state.reviewer_feedback == "✅":
            return "end"
        elif state.attempts >= 2:
            return "escalate"
        else:
            return "retrieve"

    builder.add_conditional_edges("review", review_decision)
    return builder.compile()
