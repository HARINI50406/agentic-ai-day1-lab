# Agentic AI – Foundations and Open-Source Practice
## Day 1 Lab

---

## 1. Lab Title

**Agentic AI: Foundations and Open-Source Practice – Day 1**

---

## 2. Aim

To set up a Python development environment in Visual Studio Code and understand the difference between a simple chatbot, a rule-based workflow, and an AI agent using an OpenAI-compatible LLM API.

---

## 3. Objectives

- Set up a Python virtual environment.
- Install the required Python packages.
- Configure an LLM provider using environment variables.
- Connect the project with the Groq API.
- Verify the LLM connection.
- Implement a simple chatbot.
- Implement a rule-based workflow.
- Create reusable tools.
- Implement a basic AI agent.
- Test the agent with course-fee questions.
- Compare the three approaches.
- Use Git and GitHub for version control.

---

## 4. Introduction

Agentic AI systems can be implemented using different approaches.

A **simple chatbot** sends a user's question directly to a language model and returns the generated response.

A **rule-based workflow** follows predefined instructions and uses programmed logic to perform specific tasks.

An **AI agent** combines a language model with information, instructions, tools, and a workflow to perform tasks based on user requests.

This laboratory demonstrates these approaches using a course-fee example.

---

## 5. Technologies Used

- Python 3.13
- Visual Studio Code
- Groq API
- OpenAI Python SDK
- python-dotenv
- Git
- GitHub
- `openai/gpt-oss-20b` model

---

## 6. LLM Configuration

The LLM provider used in this experiment is **Groq**.

```text
Provider : groq
Model    : openai/gpt-oss-20b
