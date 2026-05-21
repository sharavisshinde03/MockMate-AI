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

/* Main Title */

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

/* Sidebar */

section[data-testid="stSidebar"] {
    background: #0B1120;
    border-right: 1px solid rgba(255,255,255,0.05);
}

/* Buttons */

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

/* Inputs */

.stTextInput input,
.stTextArea textarea {

    background-color: #111827;
    color: white;
    border-radius: 12px;
}

/* Select */

.stSelectbox div[data-baseweb="select"] {

    background-color: #111827;
    border-radius: 12px;
}

/* Chat Cards */

[data-testid="stChatMessage"] {

    background: rgba(255,255,255,0.03);

    border: 1px solid rgba(255,255,255,0.06);

    border-radius: 18px;

    padding: 18px;

    margin-bottom: 20px;
}

/* Chat Input */

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
            "Marketing Intern",
            "HR Intern",
            "Software Engineer",
            "Frontend Developer",
            "Backend Developer",
            "Full Stack Developer",
            "Data Analyst",
            "Data Scientist",
            "Machine Learning Engineer",
            "AI Engineer",
            "DevOps Engineer",
            "Cloud Engineer",
            "Product Manager",
            "Business Analyst",
            "Cybersecurity Analyst",
            "UI/UX Designer",
            "HR Interview",
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
            "HR Round",
            "Problem Solving"
        ]
    )

    resume = st.file_uploader(
        "Upload Resume (Optional)",
        type=["pdf"]
    )

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("Start Interview"):

        # VALIDATION

        if not target_role.strip():

            st.sidebar.error(
                "Please enter/select a target role."
            )

        elif not qualifications.strip():

            st.sidebar.error(
                "Please enter your qualifications."
            )

        elif not focus_area.strip():

            st.sidebar.error(
                "Please select a focus area."
            )

        else:

            st.session_state.started = True

            st.session_state.target_role = target_role
            st.session_state.qualifications = qualifications
            st.session_state.focus_area = focus_area

            # RESUME PARSING

            resume_text = ""

            if resume:

                resume_text = extract_resume_text(
                    resume
                )

            st.session_state.resume_text = resume_text

            # INTERVIEW HISTORY

            st.session_state.history = """
            This is the beginning of the interview.
            Avoid greetings and introductions.
            Start directly with a concise interview question.
            """

            st.session_state.messages = []
            st.session_state.round = 0
            st.session_state.feedback = ""
            st.session_state.last_spoken = ""

# ---------------- MAIN UI ---------------- #

st.markdown(
    "<div class='main-title'>AI Voice Mock Interview Coach</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Adaptive AI interviewer with voice interaction, live feedback, and personalized coaching.</div>",
    unsafe_allow_html=True
)

# ---------------- INTERVIEW FLOW ---------------- #

if (
    st.session_state.started
    and st.session_state.target_role
    and st.session_state.qualifications
    and st.session_state.focus_area
):

    # FIRST QUESTION

    if st.session_state.round == 0:

        first_question = ask_question(
            st.session_state.target_role,
            st.session_state.qualifications,
            st.session_state.focus_area,
            st.session_state.history,
            st.session_state.resume_text
        )

        st.session_state.messages.append({
            "role": "assistant",
            "content": first_question
        })

        st.session_state.round += 1

    # ---------------- DISPLAY CHAT ---------------- #

    for msg in st.session_state.messages:

        # ---------------- AI MESSAGE ---------------- #

        if msg["role"] == "assistant":

            with st.chat_message(
                "assistant",
                avatar="https://cdn-icons-png.flaticon.com/512/4140/4140048.png"
            ):

                st.markdown(
                    msg["content"]
                )

                # REALTIME BROWSER VOICE

                latest_ai_message = ""

                for m in reversed(st.session_state.messages):

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

                    window.speechSynthesis.cancel();

                    const speech = new SpeechSynthesisUtterance(text);

                    const voices = window.speechSynthesis.getVoices();

                    let femaleVoice =
                        voices.find(v =>
                            v.name.includes("Samantha")
                        ) ||
                        voices.find(v =>
                            v.name.includes("Google UK English Female")
                        ) ||
                        voices.find(v =>
                            v.name.includes("Female")
                        ) ||
                        voices[0];

                    speech.voice = femaleVoice;

                    speech.rate = 1;
                    speech.pitch = 1;

                    window.speechSynthesis.speak(speech);

                    </script>
                    """

                    st.components.v1.html(
                        speak_html,
                        height=0
                    )

                    st.session_state.last_spoken = msg["content"]

        # ---------------- USER MESSAGE ---------------- #

        else:

            with st.chat_message(
                "user",
                avatar="https://cdn-icons-png.flaticon.com/512/847/847969.png"
            ):

                st.markdown(
                    msg["content"]
                )

                # FEEDBACK

                if "feedback" in msg:

                    feedback = msg["feedback"]

                    st.success(
                        feedback["positive_feedback"]
                    )

                    st.warning(
                        feedback["improvement_feedback"]
                    )

                    with st.expander(
                        "See Better Answer"
                    ):

                        st.write(
                            feedback["ideal_answer"]
                        )

    # ---------------- INPUT SECTION ---------------- #

    st.markdown("## Answer the Question")

    typed_answer = st.chat_input(
        "Type your answer here..."
    )

    st.markdown(
        "#### Voice Input"
    )

    audio = mic_recorder(
        start_prompt="Start Speaking",
        stop_prompt="Recording...",
        just_once=True,
        use_container_width=True,
        key="voice_recorder"
    )

    # ---------------- PROCESS USER INPUT ---------------- #

    if audio or typed_answer:

        # TYPED ANSWER

        if typed_answer:

            user_answer = typed_answer

        # VOICE ANSWER

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

        # LAST QUESTION

        last_question = ""

        for msg in reversed(
            st.session_state.messages
        ):

            if msg["role"] == "assistant":

                last_question = msg["content"]

                break

        # EVALUATE ANSWER

        evaluation = evaluate_answer(
            last_question,
            user_answer
        )

        # ADD USER MESSAGE WITH FEEDBACK

        st.session_state.messages.append({

            "role": "user",

            "content": user_answer,

            "feedback": evaluation
        })

        # SAVE HISTORY

        st.session_state.history += f"""

        Interviewer:
        {last_question}

        Candidate:
        {user_answer}

        """

        # NEXT QUESTION

        if st.session_state.round < 5:

            next_question = ask_question(
                st.session_state.target_role,
                st.session_state.qualifications,
                st.session_state.focus_area,
                st.session_state.history,
                st.session_state.resume_text
            )

            st.session_state.messages.append({
                "role": "assistant",
                "content": next_question
            })

            st.session_state.round += 1

            st.rerun()

        # FINAL ROUND

        else:

            st.success(
                "Interview Completed Successfully."
            )

            st.info(
                "Generating final interview report..."
            )

            feedback = generate_feedback(
                st.session_state.history
            )

            st.session_state.feedback = feedback

            st.markdown("## Final Interview Report")

            st.write(feedback)

            pdf_path = generate_pdf(
                feedback
            )

            with open(pdf_path, "rb") as file:

                st.download_button(
                    label="Download PDF Report",
                    data=file,
                    file_name="Interview_Report.pdf",
                    mime="application/pdf"
                )