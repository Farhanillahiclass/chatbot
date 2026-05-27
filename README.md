# WhatsApp Automation MVP

A simple web application that auto-replies to incoming WhatsApp messages based on keyword rules, powered by the **official WhatsApp Cloud API**.

Built with **Python / Flask** and plain HTML.

---

## Features

- **User Authentication** — Register and log in with username / password.
- **Keyword Rules Dashboard** — Create rules like *"If the incoming message is `hello`, reply with `Hi! How can I help?`"*.
- **Webhook Handler** — A secure `/webhook` endpoint that receives messages from Meta, looks up matching keywords, and sends the auto-reply via the WhatsApp Cloud API.

---

## Quick Start

### 1. Prerequisites

| Requirement | Notes |
|---|---|
| Python 3.10+ | Any recent version works |
| Meta Developer Account | [developers.facebook.com](https://developers.facebook.com/) |
| WhatsApp Business App | Create one inside Meta Developer Portal and note your **Phone Number ID** and **Access Token** |

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Copy the example file and fill in your values:

```bash
cp .env.example .env
```

| Variable | Description |
|---|---|
| `SECRET_KEY` | Flask session secret (any random string) |
| `WHATSAPP_PHONE_NUMBER_ID` | From Meta Developer Portal → WhatsApp → API Setup |
| `WHATSAPP_ACCESS_TOKEN` | Permanent or temporary token from the same page |
| `WHATSAPP_VERIFY_TOKEN` | Any string you choose — must match the one you enter in Meta's webhook config |

### 4. Run the App

```bash
python run.py
```

The app starts at **http://localhost:5000**.

### 5. Expose Your Webhook (Development)

Meta needs a public HTTPS URL. Use [ngrok](https://ngrok.com/) or a similar tunnel:

```bash
ngrok http 5000
```

Then configure the webhook in Meta Developer Portal:

- **Callback URL:** `https://<your-ngrok-url>/webhook`
- **Verify Token:** the value you set for `WHATSAPP_VERIFY_TOKEN`
- **Subscribe** to the `messages` field.

---

## Project Structure

```
whatsapp_app/
├── __init__.py        # App factory
├── config.py          # Configuration (env vars)
├── models.py          # SQLAlchemy models (User, KeywordRule)
├── auth.py            # Login / Register / Logout
├── dashboard.py       # Keyword rule CRUD
├── webhook.py         # Meta webhook verification & message handler
└── templates/
    ├── base.html       # Shared layout
    ├── login.html
    ├── register.html
    └── dashboard.html
run.py                 # Entry point
.env.example           # Sample env file
```

---

## Legacy Chatbot

The original Streamlit chatbot is still available:

```bash
streamlit run streamlit_app.py
```

---

## License

Apache 2.0 — see [LICENSE](LICENSE).
