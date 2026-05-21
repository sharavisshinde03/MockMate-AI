# MockMate AI

Adaptive AI-powered mock interview coach with voice interaction, resume-based questioning, personalized feedback, and multi-agent orchestration.

---

# Overview

MockMate AI is an intelligent AI interview platform designed to simulate realistic recruiter-style interviews for:
- students
- interns
- freshers
- professionals

The system dynamically adapts interview difficulty based on:
- qualifications
- experience level
- resume/projects
- previous answers
- communication quality
- confidence and practical understanding

The platform focuses on creating a supportive and realistic interview experience while helping candidates improve technical communication, confidence, and structured answering skills.

---

# Features

## Adaptive AI Interviewer
- Dynamically adjusts question difficulty
- Beginner-friendly for FY/SY students
- Intermediate-level intern/fresher questions
- Advanced questions for experienced professionals
- Handles follow-up questions naturally

---

## Voice Interaction
- Real-time voice input
- AI voice output using browser speech synthesis
- Conversational interview experience

---

## Resume-Based Questioning
- Optional resume upload
- Project-based and technology-specific questions
- Personalized interview flow

---

## Multi-Agent Architecture
- Interviewer Agent
- Evaluator Agent
- Coach Agent

---

## Personalized Feedback
- Positive feedback
- Improvement suggestions
- Better sample answers
- Final interview report

---

## PDF Report Generation
- Downloadable interview report
- Structured strengths and improvement areas

---

## Intelligent Conversation Handling

The interviewer can intelligently handle:
- “I don’t know”
- nervous candidates
- off-topic answers
- vague responses
- requests for easier questions
- requests to stop the interview

The AI dynamically simplifies questions when needed.

---

# Tech Stack

- Python
- Streamlit
- Groq LLM API
- Streamlit Mic Recorder
- SpeechRecognition
- Browser Speech Synthesis API
- PyPDF
- Prompt Engineering
- Multi-Agent Architecture

---

# Setup & Run Instructions

## 1. Clone the Repository

```bash
git clone https://github.com/sharavisshinde03/MockMate-AI.git
cd MockMate-AI
```

---

## 2. Create Virtual Environment

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

---

## 5. Run the Application

```bash
streamlit run app.py
```

---

# Architecture Overview

MockMate AI uses a multi-agent architecture where each AI agent performs a specialized responsibility.

---

## 1. Interviewer Agent

### Responsibilities
- Generates adaptive interview questions
- Controls conversation flow
- Adjusts difficulty dynamically
- Handles follow-up questions
- Uses resume context when available

### Behavior
- Beginner-friendly for students
- Intermediate for interns/freshers
- Advanced for experienced candidates
- Maintains recruiter-like conversational tone

---

## 2. Evaluator Agent

### Responsibilities
- Evaluates candidate answers
- Identifies strengths
- Suggests improvements
- Generates realistic supportive feedback
- Creates ideal sample answers

### Behavior
- Encouraging and non-harsh
- Recognizes partial correctness
- Handles nervous candidates supportively
- Focuses on communication and clarity

---

## 3. Coach Agent

### Responsibilities
- Generates final interview report
- Summarizes overall performance
- Identifies improvement areas
- Provides actionable final advice
- Generates downloadable PDF report

---

# Agent Orchestration Flow

```text
User
 ↓
Interviewer Agent
 ↓
Candidate Response
 ↓
Evaluator Agent
 ↓
Feedback + Better Answer
 ↓
Adaptive Follow-up Question
 ↓
Coach Agent
 ↓
Final Report + PDF
```

---

# Key Design Decisions & Tradeoffs

## 1. Multi-Agent Separation

### Decision
Separate interviewer, evaluator, and coach responsibilities into independent agents.

### Benefits
- Cleaner prompt engineering
- Better modularity
- Easier debugging
- More realistic interview behavior

### Tradeoff
- Increased orchestration complexity
- More API calls

---

## 2. Adaptive Difficulty System

### Decision
Questions dynamically adapt based on:
- qualification level
- candidate confidence
- previous answers

### Benefits
- More realistic interview experience
- Better support for beginners
- Prevents overwhelming candidates

### Tradeoff
- Harder prompt balancing
- Requires careful conversation memory management

---

## 3. Browser-Based Voice Output

### Decision
Use browser Speech Synthesis API instead of external TTS services.

### Benefits
- Faster response
- No additional API cost
- Simpler deployment

### Tradeoff
- Voice quality differs across browsers/devices
- Less control over voice consistency

---

## 4. Lightweight Streamlit Frontend

### Decision
Use Streamlit for rapid UI development.

### Benefits
- Fast prototyping
- Simple deployment
- Minimal frontend complexity

### Tradeoff
- Limited advanced frontend customization
- Less flexible than React-based frontend architectures

---

# Example Interview Transcripts

# 1. Strong Candidate — AI Engineer Intern

## Interviewer
Can you explain an AI project you worked on recently?

## Candidate
I built an AI mock interview platform using Streamlit, Gemini API, and speech recognition. The system asks adaptive interview questions and gives real-time feedback.

### Feedback

**Positive Feedback:**  
Good explanation with clear mention of technologies and project functionality.

**Improvement Feedback:**  
You could briefly explain the system architecture and workflow.

### Better Answer

“I developed an AI mock interview platform using Streamlit for the frontend and Gemini API for adaptive questioning. I integrated speech recognition and real-time evaluation to create a realistic interview experience.”

---

## Interviewer
How did you manage conversational context?

## Candidate
I stored previous interview history in session state to generate adaptive follow-up questions.

### Feedback

**Positive Feedback:**  
Good understanding of contextual memory handling.

**Improvement Feedback:**  
You can also explain how it improves personalization.

### Better Answer

“I maintained interview history using session state so the AI could generate personalized follow-up questions and dynamically adjust interview difficulty.”

---

## Overall Candidate Feedback

### Overall Summary
The candidate demonstrated strong practical understanding of AI application development, conversational systems, and adaptive workflows. Their answers were structured, technically clear, and confidently communicated.

### Strengths
- Strong project explanation skills
- Good understanding of conversational AI workflows
- Clear communication and structured thinking

### Areas for Improvement
- Could explain architecture decisions in more depth
- Can improve scalability and optimization explanations

### Final Advice
Continue building real-world AI applications and focus on system design thinking. Your practical understanding already creates a strong foundation for AI engineering roles.

---

# 2. Weak Candidate — DevOps Engineer Intern

## Interviewer
What is Docker used for?

## Candidate
Docker is used for containers but I haven’t used it much.

### Feedback

**Positive Feedback:**  
Good honesty while identifying the core purpose correctly.

**Improvement Feedback:**  
Try mentioning one real-world use case for containers.

### Better Answer

“Docker packages applications and dependencies into containers so they run consistently across different environments.”

---

## Interviewer
What is CI/CD?

## Candidate
It automates deployment.

### Feedback

**Positive Feedback:**  
You identified the main concept correctly.

**Improvement Feedback:**  
Try explaining continuous integration and deployment separately.

### Better Answer

“CI/CD automates code integration, testing, and deployment to improve development speed and reliability.”

---

## Overall Candidate Feedback

### Overall Summary
The candidate demonstrated beginner-level understanding of DevOps concepts and communicated honestly about limited practical experience. They showed awareness of core tools but need stronger implementation knowledge.

### Strengths
- Honest communication
- Basic understanding of Docker and CI/CD
- Willingness to learn technical concepts

### Areas for Improvement
- Needs more hands-on DevOps practice
- Can improve technical depth and structured explanations

### Final Advice
Focus on building small deployment projects using Docker, GitHub Actions, and cloud platforms. Practical implementation experience will significantly improve confidence and technical understanding.

---

# 3. Tricky Edge Case — Cloud Engineer Intern

## Interviewer
What cloud platforms have you worked with?

## Candidate
I mostly explored AWS Free Tier and watched tutorials.

### Feedback

**Positive Feedback:**  
Good initiative in learning cloud concepts independently.

**Improvement Feedback:**  
Mention specific services you experimented with.

### Better Answer

“I explored AWS Free Tier and practiced using EC2, S3, and basic deployment workflows while learning cloud fundamentals.”

---

## Interviewer
How would you debug a cloud deployment issue?

## Candidate
I would first check logs and restart services if needed.

### Feedback

**Positive Feedback:**  
Good practical starting approach for debugging.

**Improvement Feedback:**  
You can also mention root cause analysis after restoring services.

### Better Answer

“I would review logs, identify the failing service, restore availability if required, and then investigate the root cause to prevent future failures.”

---

## Overall Candidate Feedback

### Overall Summary
The candidate initially showed limited confidence in cloud concepts but improved while discussing practical exposure and debugging approaches. Their responses reflected a growing understanding of cloud fundamentals.

### Strengths
- Demonstrated self-learning initiative
- Good debugging mindset
- Basic understanding of cloud services

### Areas for Improvement
- Needs deeper cloud implementation experience
- Can improve confidence while explaining concepts

### Final Advice
Continue practicing with cloud deployment projects and focus on understanding core AWS services practically. Consistent hands-on learning will strengthen both confidence and technical clarity.

---
# Screenshots
<img width="1438" height="791" alt="Screenshot 2026-05-22 at 2 32 11 AM" src="https://github.com/user-attachments/assets/eb2aa35e-a2f0-4c89-92f7-b5ec1d80be7f" />
<img width="1450" height="673" alt="Screenshot 2026-05-22 at 2 35 38 AM" src="https://github.com/user-attachments/assets/d6a3f9b0-00b7-427d-88b0-85449fa3df36" />
<img width="1470" height="707" alt="Screenshot 2026-05-22 at 2 36 55 AM" src="https://github.com/user-attachments/assets/f5b2861b-f004-4564-8217-323913ebc9d6" />

---

# Future Improvements

- Facial expression analysis
- Confidence scoring
- AI-generated interview analytics
- Real-time emotion detection
- Multi-language interview support
- Custom interviewer personalities
- Live coding interview integration

---

# License

MIT License

---

# Author

Built with AI-powered multi-agent orchestration and adaptive interview intelligence.
