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
cd mockmate-ai
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
