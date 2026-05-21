# MockMate AI

Adaptive AI-powered mock interview coach with voice interaction, resume-based questioning, personalized feedback, and multi-agent orchestration.

---

## Overview

MockMate AI is an intelligent mock interview platform designed to simulate realistic recruiter-style interviews for students, interns, freshers, and professionals.

The system dynamically adapts interview difficulty based on the candidate’s:
- qualifications
- experience level
- resume/projects
- previous answers
- communication quality

The goal is to create a realistic and supportive interview environment while providing personalized coaching and actionable feedback.

---

## Features

### Adaptive AI Interviewer
- Dynamically adjusts question difficulty
- Beginner-friendly for FY/SY students
- Intermediate questions for freshers/interns
- Advanced questions for experienced professionals

### Voice Interaction
- Real-time voice input
- AI voice output using browser speech synthesis
- Conversational interview experience

### Resume-Based Questioning
- Optional resume upload
- AI asks project-based and technology-specific questions

### Multi-Agent Architecture
- Interviewer Agent
- Evaluator Agent
- Coach Agent

### Personalized Feedback
- Strengths
- Weaknesses
- Suggested improvements
- Ideal answers

### PDF Report Generation
- Downloadable final interview report

### Intelligent Conversation Handling
- Handles:
  - "I don't know"
  - off-topic answers
  - vague responses
  - nervous candidates
- Dynamically simplifies questions when required

---

## Tech Stack

- Python
- Streamlit
- Groq LLM API
- Streamlit Mic Recorder
- SpeechRecognition
- Browser Speech Synthesis API
- PyPDF
- Multi-Agent Prompt Engineering

---

## Multi-Agent Architecture

### 1. Interviewer Agent
Responsible for:
- asking adaptive interview questions
- adjusting difficulty dynamically
- handling conversational flow
- asking resume-based questions

### 2. Evaluator Agent
Responsible for:
- evaluating candidate responses
- identifying strengths and weaknesses
- generating ideal answers
- giving constructive feedback

### 3. Coach Agent
Responsible for:
- generating final interview summary
- identifying improvement areas
- creating actionable coaching advice

---

## System Flow

```text
User
 ↓
Interviewer Agent
 ↓
Candidate Response
 ↓
Evaluator Agent
 ↓
Adaptive Follow-up Question
 ↓
Coach Agent
 ↓
Final Report + PDF