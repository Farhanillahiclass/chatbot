# Deployment

## Streamlit Community Cloud (Recommended)

The easiest way to deploy this chatbot is using [Streamlit Community Cloud](https://streamlit.io/cloud):

1. Push your code to a GitHub repository
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Sign in with your GitHub account
4. Click **New app**
5. Select your repository, branch (`main`), and main file (`streamlit_app.py`)
6. Click **Deploy**

### Setting Secrets on Community Cloud

1. In your deployed app's settings, go to **Secrets**
2. Add your OpenAI API key:
   ```toml
   OPENAI_API_KEY = "sk-your-api-key-here"
   ```

## Docker Deployment

### Using the Dev Container

The project includes a Dev Container configuration that can be adapted for production:

```dockerfile
FROM mcr.microsoft.com/devcontainers/python:1-3.11-bullseye

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

EXPOSE 8501
CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### Build and Run

```bash
docker build -t chatbot .
docker run -p 8501:8501 chatbot
```

## Other Platforms

### Heroku

1. Create a `Procfile`:
   ```
   web: streamlit run streamlit_app.py --server.port=$PORT --server.address=0.0.0.0
   ```

2. Deploy:
   ```bash
   heroku create
   git push heroku main
   ```

### Railway

1. Connect your GitHub repository on [Railway](https://railway.app)
2. Set the start command:
   ```
   streamlit run streamlit_app.py --server.port=$PORT --server.address=0.0.0.0
   ```

## Environment Variables

For any deployment platform, ensure the following environment variables are set if using secrets-based API key management:

| Variable         | Description          | Required |
|------------------|----------------------|----------|
| OPENAI_API_KEY   | Your OpenAI API key  | Yes      |
