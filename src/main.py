from graph import build
from models import SupportTicket, SupportState

if __name__ == "__main__":
    graph = build()
    ticket = SupportTicket(
        subject="Refund not received",
        description="I was promised a refund two weeks ago but haven't seen it credited to my account."
    )
    result = graph.invoke(SupportState(tcoicket=ticket))
    print("Final Output:", result)
