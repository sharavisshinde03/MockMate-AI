from config import llm

with open("prompts/coach.txt", "r") as f:

    SYSTEM_PROMPT = f.read()


def generate_feedback(history):

    prompt = f"""
    {SYSTEM_PROMPT}

    ACTUAL INTERVIEW CONVERSATION:
    {history}

    IMPORTANT:
    Use ONLY the information available in the interview conversation.
    Do NOT invent missing details.
    """

    response = llm.invoke(
        prompt[:4000]
    )

    return response.content