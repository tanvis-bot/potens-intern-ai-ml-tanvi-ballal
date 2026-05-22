import os
import json

from dotenv import load_dotenv
from groq import Groq

from tools.similarity_tool import search_similar_incidents
from tools.status_tool import check_system_status
from tools.draft_tool import generate_acknowledgment
from tools.escalation_tool import escalate_to_human

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def run_agent(user_input):

    reasoning = []

    reasoning.append("Analyzing user issue")

    similar_incident = search_similar_incidents(user_input)

    reasoning.append(
        f"Found similar incident: {similar_incident['issue']}"
    )

    system_status = check_system_status("gpu_cluster")

    reasoning.append(
        f"Checked infrastructure status: {system_status}"
    )

    prompt = f"""
    You are an AI Infrastructure Incident Triage Agent.

    User issue:
    {user_input}

    Similar incident:
    {similar_incident}

    System status:
    {system_status}

    Determine:
    1. category
    2. priority (P0/P1/P2)
    3. next_tool
    4. reasoning
    5. why

    Return STRICT JSON ONLY in this format:

    {
    "category": "",
    "priority": "",
    "next_tool": "",
    "reasoning": "",
    "why": ""
    }

    Return JSON only.
    """

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0,
        max_tokens=300
    )

    llm_response = completion.choices[0].message.content

    if "unsure" in llm_response.lower():
        escalation = escalate_to_human(user_input)
        reasoning.append("Escalated to human due to low confidence")
    else:
        escalation = "No escalation required"
    
    llm_response = llm_response.replace("```json", "")
    llm_response = llm_response.replace("```", "")

    reasoning.append("LLM generated triage decision")

    acknowledgment = generate_acknowledgment(user_input)

    reasoning.append("Generated acknowledgment message")

    return {
    "triage_decision": llm_response,
    "similar_incident": similar_incident,
    "system_status": system_status,
    "acknowledgment": acknowledgment,
    "reasoning_trace": reasoning,
    "escalation": escalation
}