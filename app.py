from fastapi import FastAPI
from pydantic import BaseModel

from agent import run_agent

app = FastAPI()

class Ticket(BaseModel):
    issue: str

@app.post("/triage")
def triage(ticket: Ticket):

    result = run_agent(ticket.issue)

    return {
        "response": result
    }