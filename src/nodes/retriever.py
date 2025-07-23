import os


def retrieve_context(state):
    category = state.category.lower()
    file_path = os.path.join("sample_docs", f"{category}.txt")
    try:
        with open(file_path, "r") as f:
            docs = f.readlines()
    except FileNotFoundError:
        docs = ["No documents found for this category."]
    return state.copy(update={"context": docs})
