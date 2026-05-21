from config import llm
import json
import re


with open("prompts/evaluator.txt", "r") as f:
    SYSTEM_PROMPT = f.read()


def evaluate_answer(question, answer):

    answer_lower = answer.lower().strip()

    # ---------------- UNKNOWN ANSWERS ---------------- #

    unknown_phrases = [
        "i don't know",
        "dont know",
        "not sure",
        "no idea",
        "forgot",
        "haven't learned",
        "have not learned"
    ]

    if any(p in answer_lower for p in unknown_phrases):

        return {
            "positive_feedback":
                "It's completely okay to not know every answer.",

            "improvement_feedback":
                "Try revisiting the basics of this topic and practice a few beginner examples.",

            "better_answer":
                "I haven't explored this topic deeply yet, but I'm currently learning it through projects and practice."
        }

    # ---------------- VERY SHORT ANSWERS ---------------- #

    if len(answer.split()) < 6:

        return {
            "positive_feedback":
                "Good attempt.",

            "improvement_feedback":
                "Try explaining your thought process in slightly more detail.",

            "better_answer":
                "A stronger answer should explain the approach, tools used, and what you learned from the experience."
        }

    # ---------------- PARTIAL ANSWERS ---------------- #

    if len(answer.split()) < 20:

        return {
            "positive_feedback":
                "You explained the basic idea clearly.",

            "improvement_feedback":
                "Try adding more detail about your implementation or reasoning.",

            "better_answer":
                "A better interview answer usually explains the situation, your approach, the tools or technologies used, and the final outcome."
        }

    # ---------------- STRONG ANSWERS ---------------- #

    prompt = f"""
    {SYSTEM_PROMPT}

    Interview Question:
    {question}

    Candidate Answer:
    {answer}

    IMPORTANT:
    - Give personalized feedback based on the actual answer.
    - Do NOT sound robotic.
    - Do NOT mention scores.
    - Keep feedback short and realistic.
    - Better answer should ONLY contain a better sample answer.
    - Do NOT ask another question.
    - Do NOT include 'Next question'.
    - Return ONLY valid JSON.

    Required JSON format:

    {{
        "positive_feedback": "...",
        "improvement_feedback": "...",
        "better_answer": "..."
    }}
    """

    response = llm.invoke(prompt)

    content = response.content.strip()

    # ---------------- CLEAN RESPONSE ---------------- #

    content = re.sub(r"```json", "", content)
    content = re.sub(r"```", "", content)

    try:

        result = json.loads(content)

        return {
            "positive_feedback":
                result.get(
                    "positive_feedback",
                    "Good explanation overall."
                ),

            "improvement_feedback":
                result.get(
                    "improvement_feedback",
                    "Try making the answer slightly more structured."
                ),

            "better_answer":
                result.get(
                    "better_answer",
                    "A stronger answer could include more clarity and practical examples."
                )
        }

    except Exception as e:

        print("JSON ERROR:", e)
        print(content)

        return {
            "positive_feedback":
                "Good effort answering the question.",

            "improvement_feedback":
                "Try organizing the answer more clearly and adding practical details.",

            "better_answer":
                "A stronger answer should explain the approach, tools used, and the outcome in a structured way."
        }