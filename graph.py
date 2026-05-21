from agents.interviewer import ask_question
from agents.evaluator import evaluate_answer
from agents.coach import generate_feedback


def run_interview():

    print("\n========== AI MOCK INTERVIEW ==========\n")

    preparation_goal = input(
        "What are you preparing for?\n> "
    )

    qualifications = input(
        "\nWhat are your qualifications?\n> "
    )

    practice_area = input(
        "\nWhat would you like to practice today?\n> "
    )

    history = ""

    for round in range(5):

        print(f"\n========== ROUND {round + 1} ==========\n")

        # Generate Question
        question = ask_question(
            preparation_goal,
            qualifications,
            practice_area,
            history
        )

        print("🎤 Interviewer:\n")
        print(question)

        # Candidate Response
        answer = input("\n🧑 Your Answer:\n> ")

        # Evaluate Response
        evaluation = evaluate_answer(
            question,
            answer
        )

        print("\n📊 Evaluation:\n")
        print(evaluation)

        # Save Interview History
        history += f"""

        ROUND {round + 1}

        Interviewer:
        {question}

        Candidate:
        {answer}

        Evaluation:
        {evaluation}

        """

    # Final Coach Feedback
    print("\n========== FINAL FEEDBACK ==========\n")

    feedback = generate_feedback(history)

    print(feedback)