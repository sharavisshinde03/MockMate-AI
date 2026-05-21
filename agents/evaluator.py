from config import llm
import json
import re

with open("prompts/evaluator.txt", "r") as f:
    SYSTEM_PROMPT = f.read()


def evaluate_answer(question, answer):

    prompt = f"""
    {SYSTEM_PROMPT}

    Interview Question:
    {question}

    Candidate Answer:
    {answer}

    Return ONLY valid JSON.
    """

    response = llm.invoke(prompt)

    content = response.content.strip()

    # Remove markdown wrappers
    content = re.sub(r"```json", "", content)
    content = re.sub(r"```", "", content)

    try:

        result = json.loads(content)

        return result

    except Exception as e:

        print("JSON ERROR:", e)
        print(content)

        return {
            "technical_score": 5,
            "communication_score": 5,
            "confidence_score": 5,
            "overall_score": 5,
            "positive_feedback": "Good effort attempting the answer.",
            "improvement_feedback": "Try adding more clarity and technical depth.",
            "ideal_answer": "Could not generate ideal answer.",
            "follow_up_needed": True,
            "difficulty_level": "medium"
        }