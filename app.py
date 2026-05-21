import streamlit as st
import tempfile

from streamlit_mic_recorder import mic_recorder

from agents.interviewer import ask_question
from agents.evaluator import evaluate_answer
from agents.coach import generate_feedback

from pdf_generator import generate_pdf
from resume_parser import extract_resume_text

from utils import speech_to_text

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="AI Voice Interview Coach",
    layout="wide"
)

# ---------------- CUSTOM CSS ---------------- #

st.markdown("""
<style>

.stApp {
    background-color: #030712;
    color: white;
}

.main-title {
    font-size: 56px;
    font-weight: 700;
    color: white;
    margin-bottom: 8px;
}

.subtitle {
    color: #94A3B8;
    font-size: 18px;
    margin-bottom: 35px;
}

section[data-testid="stSidebar"] {
    background: #0B1120;
    border-right: 1px solid rgba(255,255,255,0.05);
}

.stButton>button {
    width: 100%;
    height: 52px;
    border: none;
    border-radius: 14px;
    background: linear-gradient(
        90deg,
        #2563EB,
        #7C3AED
    );
    color: white;
    font-size: 16px;
    font-weight: 600;
}

.stTextInput input,
.stTextArea textarea {
    background-color: #111827;
    color: white;
    border-radius: 12px;
}

.stSelectbox div[data-baseweb="select"] {
    background-color: #111827;
    border-radius: 12px;
}

[data-testid="stChatMessage"] {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 18px;
    padding: 18px;
    margin-bottom: 20px;
}

.stChatInput textarea {
    background: #111827 !important;
    color: white !important;
    border-radius: 14px !important;
}

.block-container {
    padding-top: 2rem;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SESSION STATE ---------------- #

if "started" not in st.session_state:
    st.session_state.started = False

if "history" not in st.session_state:
    st.session_state.history = ""

if "messages" not in st.session_state:
    st.session_state.messages = []

if "round" not in st.session_state:
    st.session_state.round = 0

if "feedback" not in st.session_state:
    st.session_state.feedback = ""

if "last_spoken" not in st.session_state:
    st.session_state.last_spoken = ""

if "target_role" not in st.session_state:
    st.session_state.target_role = ""

if "qualifications" not in st.session_state:
    st.session_state.qualifications = ""

if "focus_area" not in st.session_state:
    st.session_state.focus_area = ""

if "resume_text" not in st.session_state:
    st.session_state.resume_text = ""

# ---------------- SIDEBAR ---------------- #

with st.sidebar:

    st.markdown("## Interview Setup")

    target_role = st.selectbox(
        "Target Role",
        [
            "Software Engineer Intern",
            "Frontend Developer Intern",
            "Backend Developer Intern",
            "Full Stack Developer Intern",
            "Data Analyst Intern",
            "Data Scientist Intern",
            "Machine Learning Engineer Intern",
            "AI Engineer Intern",
            "DevOps Engineer Intern",
            "Cloud Engineer Intern",
            "Product Manager Intern",
            "Business Analyst Intern",
            "Cybersecurity Analyst Intern",
            "UI/UX Designer Intern",
            "Software Engineer",
            "Frontend Developer",
            "Backend Developer",
            "Full Stack Developer",
            "Data Analyst",
            "Data Scientist",
            "Machine Learning Engineer",
            "AI Engineer",
            "Custom"
        ]
    )

    if target_role == "Custom":

        target_role = st.text_input(
            "Enter Custom Role"
        )

    qualifications = st.text_area(
        "Qualifications",
        placeholder="Type Here...."
    )

    focus_area = st.selectbox(
        "Focus Area",
        [
            "Technical Interview",
            "Behavioral Interview",
            "Mixed Interview",
            "System Design",
            "HR Round"
        ]
    )

    resume = st.file_uploader(
        "Upload Resume (Optional)",
        type=["pdf"]
    )

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("Start Interview"):

        if not target_role.strip():

            st.sidebar.error(
                "Please enter/select a target role."
            )

        elif not qualifications.strip():

            st.sidebar.error(
                "Please enter your qualifications."
            )

        else:

            st.session_state.started = True

            st.session_state.target_role = target_role
            st.session_state.qualifications = qualifications
            st.session_state.focus_area = focus_area

            resume_text = ""

            if resume:

                resume_text = extract_resume_text(
                    resume
                )

            st.session_state.resume_text = resume_text

            st.session_state.history = """
Start the interview naturally.
Ask concise realistic questions.
Ask one question at a time.
"""

            st.session_state.messages = []
            st.session_state.round = 0
            st.session_state.feedback = ""
            st.session_state.last_spoken = ""

            st.rerun()

# ---------------- MAIN TITLE ---------------- #

st.markdown(
    "<div class='main-title'>AI Voice Mock Interview Coach</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Adaptive AI interviewer with voice interaction, live feedback, and personalized coaching.</div>",
    unsafe_allow_html=True
)

# ---------------- INTERVIEW ---------------- #

if st.session_state.started:

    # ---------------- FIRST QUESTION ---------------- #

    if st.session_state.round == 0:

        resume_context = ""

        if st.session_state.resume_text.strip():
            resume_context = st.session_state.resume_text
        else:
            resume_context = """
No resume was uploaded.

IMPORTANT:
- Do NOT mention resume
- Do NOT mention internships
- Do NOT mention projects
- Do NOT assume experience
unless the candidate explicitly mentions them.
"""

        first_question = ask_question(
            st.session_state.target_role,
            st.session_state.qualifications,
            st.session_state.focus_area,
            st.session_state.history,
            resume_context
        )

        st.session_state.messages.append({
            "role": "assistant",
            "content": first_question
        })

        st.session_state.round += 1

    # ---------------- DISPLAY CHAT ---------------- #

    for msg in st.session_state.messages:

        # ---------------- BOT ---------------- #

        if msg["role"] == "assistant":

            with st.chat_message(
                "assistant",
                avatar="https://cdn-icons-png.flaticon.com/512/4712/4712109.png"
            ):

                st.markdown(
                    msg["content"]
                )

                latest_ai_message = ""

                for m in reversed(
                    st.session_state.messages
                ):

                    if m["role"] == "assistant":

                        latest_ai_message = m["content"]

                        break

                if (
                    msg["content"] == latest_ai_message
                    and st.session_state.last_spoken != msg["content"]
                ):

                    escaped_text = msg["content"] \
                        .replace("`", "") \
                        .replace('"', "") \
                        .replace("\n", " ")

                    speak_html = f"""
                    <script>

                    const text = `{escaped_text}`;

                    function speakMessage() {{

                        window.speechSynthesis.cancel();

                        const speech =
                            new SpeechSynthesisUtterance(text);

                        const voices =
                            window.speechSynthesis.getVoices();

                        let robotVoice =
                            voices.find(v =>
                                v.name.includes("Google UK English")
                            ) ||
                            voices[0];

                        speech.voice = robotVoice;

                        speech.rate = 1;
                        speech.pitch = 1;

                        window.speechSynthesis.speak(speech);
                    }}

                    if (
                        speechSynthesis.getVoices().length === 0
                    ) {{

                        speechSynthesis.onvoiceschanged =
                            speakMessage;

                    }} else {{

                        setTimeout(() => {{
                            speakMessage();
                        }}, 300);
                    }}

                    </script>
                    """

                    st.components.v1.html(
                        speak_html,
                        height=0
                    )

                    st.session_state.last_spoken = msg["content"]

        # ---------------- USER ---------------- #

        else:

            with st.chat_message(
                "user",
                avatar="https://cdn-icons-png.flaticon.com/512/9131/9131529.png"
            ):

                st.markdown(
                    msg["content"]
                )

                if "feedback" in msg:

                    feedback = msg["feedback"]

                    positive_feedback = feedback.get(
                        "positive_feedback",
                        "Good explanation of your approach."
                    )

                    improvement_feedback = feedback.get(
                        "improvement_feedback",
                        "You can make the answer slightly more structured."
                    )

                    st.success(
                        positive_feedback
                    )

                    st.warning(
                        improvement_feedback
                    )

                    # ---------------- BETTER ANSWER ---------------- #

                    better_answer = feedback.get(
                        "better_answer",
                        ""
                    )

                    remove_phrases = [
                        "Next question:",
                        "Let's move on",
                        "Follow-up question:",
                        "Can you explain",
                        "Can you walk me through"
                    ]

                    for phrase in remove_phrases:

                        if phrase in better_answer:
                            better_answer = better_answer.split(phrase)[0]

                    with st.expander(
                        "See Better Answer"
                    ):

                        st.info(
                            better_answer.strip()
                        )

    # ---------------- INPUT ---------------- #

    st.markdown("## Answer the Question")

    typed_answer = st.chat_input(
        "Type your answer here..."
    )

    st.markdown("#### Voice Input")

    audio = mic_recorder(
        start_prompt="Start Speaking",
        stop_prompt="Stop Recording",
        just_once=True,
        use_container_width=True,
        key="voice_recorder"
    )

    # ---------------- PROCESS INPUT ---------------- #

    if audio or typed_answer:

        if typed_answer:

            user_answer = typed_answer

        else:

            with tempfile.NamedTemporaryFile(
                delete=False,
                suffix=".wav"
            ) as temp_audio:

                temp_audio.write(
                    audio["bytes"]
                )

                temp_audio_path = temp_audio.name

            user_answer = speech_to_text(
                temp_audio_path
            )

        # ---------------- LAST QUESTION ---------------- #

        last_question = ""

        for msg in reversed(
            st.session_state.messages
        ):

            if msg["role"] == "assistant":

                last_question = msg["content"]

                break

        # ---------------- STOP INTERVIEW ---------------- #

        stop_words = [
            "stop",
            "end interview",
            "finish interview",
            "i am done",
            "i'm done",
            "quit",
            "can we stop"
        ]

        if any(
            word in user_answer.lower()
            for word in stop_words
        ):

            st.success(
                "Interview Ended Successfully."
            )

            final_feedback = generate_feedback(
                st.session_state.history
            )

            st.markdown(
                "## Final Interview Report"
            )

            st.write(
                final_feedback
            )

            pdf_path = generate_pdf(
                final_feedback
            )

            with open(pdf_path, "rb") as file:

                st.download_button(
                    label="Download PDF Report",
                    data=file,
                    file_name="Interview_Report.pdf",
                    mime="application/pdf"
                )

            st.stop()

        # ---------------- EVALUATE ---------------- #

        evaluation = evaluate_answer(
            last_question,
            user_answer
        )

        evaluation["question"] = last_question

        # ---------------- STORE USER MESSAGE ---------------- #

        st.session_state.messages.append({

            "role": "user",

            "content": user_answer,

            "feedback": evaluation
        })

        # ---------------- HISTORY ---------------- #

        st.session_state.history += f"""

Interviewer:
{last_question}

Candidate:
{user_answer}

"""

        # ---------------- NEXT QUESTION ---------------- #

        if st.session_state.round < 15:

            resume_context = ""

            if st.session_state.resume_text.strip():
                resume_context = st.session_state.resume_text
            else:
                resume_context = """
No resume was uploaded.

IMPORTANT:
- Do NOT mention resume
- Do NOT mention internships
- Do NOT mention projects
- Do NOT assume experience
unless the candidate explicitly mentions them.
"""

            next_question = ask_question(
                st.session_state.target_role,
                st.session_state.qualifications,
                st.session_state.focus_area,
                st.session_state.history,
                resume_context
            )

            st.session_state.messages.append({
                "role": "assistant",
                "content": next_question
            })

            st.session_state.round += 1

            st.rerun()

        # ---------------- FINAL REPORT ---------------- #

        else:

            st.success(
                "Interview Completed Successfully."
            )

            final_feedback = generate_feedback(
                st.session_state.history
            )

            st.markdown(
                "## Final Interview Report"
            )

            st.write(
                final_feedback
            )

            pdf_path = generate_pdf(
                final_feedback
            )

            with open(pdf_path, "rb") as file:

                st.download_button(
                    label="Download PDF Report",
                    data=file,
                    file_name="Interview_Report.pdf",
                    mime="application/pdf"
                )