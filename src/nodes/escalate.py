import csv

def handle_escalation(state):
    with open("escalation_log.csv", "a") as f:
        writer = csv.writer(f)
        writer.writerow([
            state.ticket.subject,
            state.ticket.description,
            state.draft,
            state.reviewer_feedback
        ])
    return {"message": "Escalated and logged."}