# SOLUZIONE AI

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

question = input("Cosa ti serve sapere? >")
files = ["dipendenti.csv", "presenze.csv"]
files_id = []

for file in files:
    with open(f"../{file}", "rb") as csv:
        file = client.files.create(file=csv, purpose="user_data")
        files_id.append(file.id)

response = client.responses.create(
    model="gpt-6-luna",
    instructions="Sei il mio assistente personale chiamato Pippo! Ti occupi di utilizzare python per analizzare i CSV. Ordina per nome reparto e aggiungi totale generale alla fine.",
    input=question,
    include=["code_interpreter_call.outputs"],
    tools=[{
        "type": "code_interpreter",
        "container": {"type": "auto", "file_ids": files_id}
    }],
    tool_choice="required"
)

print(response.output_text)