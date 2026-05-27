# Configuration

## Model Configuration

The chatbot uses GPT-3.5-turbo by default. To change the model, edit the `model` parameter in `streamlit_app.py`:

```python
stream = client.chat.completions.create(
    model="gpt-3.5-turbo",  # Change this to use a different model
    messages=[
        {"role": m["role"], "content": m["content"]}
        for m in st.session_state.messages
    ],
    stream=True,
)
```

### Available Models

| Model            | Description                       |
|------------------|-----------------------------------|
| gpt-3.5-turbo    | Fast, cost-effective (default)    |
| gpt-4            | More capable, higher cost         |
| gpt-4-turbo      | Latest GPT-4 with improved speed  |
| gpt-4o           | Optimized GPT-4 variant           |

## API Key Configuration

### Via UI Input (Default)
The default behavior prompts the user to enter their API key in the browser.

### Via Streamlit Secrets
For a more permanent setup:

1. Create the secrets directory:
   ```bash
   mkdir -p .streamlit
   ```

2. Create `.streamlit/secrets.toml`:
   ```toml
   OPENAI_API_KEY = "sk-your-api-key-here"
   ```

3. Access in code:
   ```python
   openai_api_key = st.secrets["OPENAI_API_KEY"]
   ```

> **Note**: Never commit your API key to version control. The `.gitignore` file already excludes `.streamlit/secrets.toml`.

## Streamlit Configuration

You can customize the Streamlit server behavior by creating `.streamlit/config.toml`:

```toml
[server]
port = 8501
enableCORS = false
enableXsrfProtection = false

[theme]
primaryColor = "#FF4B4B"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
```

## System Prompt

To add a system prompt that guides the chatbot's behavior, modify the messages list:

```python
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]
```
