# Getting Started

This guide will help you set up and run the chatbot on your local machine.

## Prerequisites

- **Python 3.8+** (Python 3.11 recommended)
- **pip** (Python package manager)
- **OpenAI API Key** - Get one from [OpenAI Platform](https://platform.openai.com/account/api-keys)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Farhanillahiclass/chatbot.git
cd chatbot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

This installs the following packages:
- `streamlit` - Web application framework
- `openai` - OpenAI Python client library

### 3. Run the Application

```bash
streamlit run streamlit_app.py
```

The app will open in your default browser at `http://localhost:8501`.

## Using GitHub Codespaces

This project includes a Dev Container configuration for GitHub Codespaces:

1. Navigate to the [repository](https://github.com/Farhanillahiclass/chatbot)
2. Click the green **Code** button
3. Select the **Codespaces** tab
4. Click **Create codespace on main**

The environment will automatically install dependencies and start the Streamlit server.

## Next Steps

- Read the [Usage Guide](Usage-Guide) to learn how to interact with the chatbot
- Check out the [Configuration](Configuration) page for customization options
