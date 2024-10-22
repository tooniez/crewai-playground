<h1 align="center">CrewAI Playground 🤖🚀</h1>

<h2 align="center">Explore AI-powered applications using CrewAI</h2>

<!-- Badges -->
<p align="center">
<a href="https://github.com/tooniez/crewai-playground/issues"><img alt="GitHub issues" src="https://img.shields.io/github/issues/tooniez/crewai-playground"></a>
<a href="https://github.com/tooniez/crewai-playground/network"><img alt="GitHub forks" src="https://img.shields.io/github/forks/tooniez/crewai-playground"></a>
<a href="https://github.com/tooniez/crewai-playground/stargazers"><img alt="Github Stars" src="https://img.shields.io/github/stars/tooniez/crewai-playground"></a>
<a href="https://github.com/tooniez/crewai-playground/blob/master/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/tooniez/crewai-playground"></a>

<!-- package versions -->
<img src="https://img.shields.io/badge/CrewAI-Latest-blue" alt="CrewAI Latest" />
<img src="https://img.shields.io/badge/Streamlit-Latest-blue" alt="Streamlit Latest" />
<img src="https://img.shields.io/badge/LangChain-Latest-blue" alt="LangChain Latest" />
<img src="https://img.shields.io/badge/Ollama-Latest-blue" alt="Ollama Latest" />

</p>

## Contents

1. [Introduction](#introduction)
    - [Features](#features)
    - [Configuration](#configuration)
2. [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Setup](#setup)
    - [Run](#run)
3. [Join the Community!](#join-the-community)
4. [License](#license)

## Introduction

CrewAI Playground is a Streamlit-based application that showcases the power of CrewAI in creating intelligent, collaborative AI systems. It currently features an AI Travel Planner that demonstrates how multiple AI agents can work together to plan a vacation.

### Features

- AI Travel Planner
- Multiple AI agents with specific roles (City Selection Expert, Local Expert, Travel Concierge)
- Integration with external APIs for search and web scraping
- Streamlit-based user interface

### Configuration

The application uses various API keys for its functionality. These are stored in the `.streamlit/secrets.toml` file:

```yaml
SERPER_API_KEY="API_KEY_HERE" # https://serper.dev/ (free tier)
BROWSERLESS_API_KEY="API_KEY_HERE" # https://www.browserless.io/ (free tier)
OPENAI_API_KEY="NA" # Using localOllama for LLM
```

## Getting Started

### Prerequisites

- Python 3.7+
- Streamlit
- CrewAI
- LangChain
- Ollama (for local LLM)

### Setup

1. Clone the repository
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
3. Set up your API keys in `.streamlit/secrets.toml`

### Run

To run the application, use the following command:

```
streamlit run streamlit_app.py
```

## Join the Community!

Got ideas? We'd love your input! Check out our [Contributing Guidelines](.github/CONTRIBUTING.md) and dive in. Don't forget to drop a ⭐️ if you like what you see!


## License

Copyright © 2024 [tooniez](https://github.com/tooniez). <br />
This project is [MIT](https://github.com/tooniez/crewai-playground/blob/main/LICENSE) licensed.
