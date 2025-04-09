import os
import tempfile

def handle_file_upload(uploaded_file):
    os.makedirs("uploaded_files", exist_ok=True)
    file_path = os.path.join("uploaded_files", uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return f"File '{uploaded_file.name}' uploaded successfully."

def answer_query(query):
    return f"I understood your question: '{query}', but my smart brain is still learning the document part 😉."
