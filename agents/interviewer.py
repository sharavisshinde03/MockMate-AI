from config import llm

with open("prompts/interviewer.txt", "r") as f:
    SYSTEM_PROMPT = f.read()


def ask_question(
    target_role,
    qualifications,
    focus_area,
    history,
    resume_text=""
):

    prompt = f"""
    {SYSTEM_PROMPT}

    Target Role:
    {target_role}

    Qualifications:
    {qualifications}

    Focus Area:
    {focus_area}

    Resume Content:
    {resume_text}

    Previous Interview History:
    {history}

    Ask the next interview question.

    If resume projects/skills exist,
    ask personalized questions based on them.
    """

    response = llm.invoke(
        prompt[:5000]
    )

    return response.content