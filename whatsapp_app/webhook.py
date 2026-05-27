import logging

import requests
from flask import Blueprint, current_app, jsonify, request

from whatsapp_app.models import KeywordRule

logger = logging.getLogger(__name__)

webhook_bp = Blueprint("webhook", __name__)


@webhook_bp.route("/webhook", methods=["GET"])
def verify():
    """Meta webhook verification (hub.challenge handshake)."""
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode == "subscribe" and token == current_app.config["WHATSAPP_VERIFY_TOKEN"]:
        logger.info("Webhook verified successfully.")
        return challenge, 200

    logger.warning("Webhook verification failed.")
    return "Forbidden", 403


@webhook_bp.route("/webhook", methods=["POST"])
def handle_message():
    """Receive incoming WhatsApp messages and send auto-replies."""
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"status": "no data"}), 400

    for entry in data.get("entry", []):
        for change in entry.get("changes", []):
            value = change.get("value", {})
            messages = value.get("messages", [])
            for message in messages:
                if message.get("type") != "text":
                    continue

                incoming_text = message["text"]["body"].strip().lower()
                sender = message["from"]

                rule = KeywordRule.query.filter(
                    KeywordRule.keyword == incoming_text
                ).first()

                if rule:
                    _send_reply(sender, rule.reply)
                    logger.info(
                        "Matched keyword '%s' → replied to %s",
                        incoming_text,
                        sender,
                    )
                else:
                    logger.info(
                        "No matching keyword for '%s' from %s",
                        incoming_text,
                        sender,
                    )

    return jsonify({"status": "ok"}), 200


def _send_reply(to: str, body: str) -> None:
    """Send a text message via the WhatsApp Cloud API."""
    url = (
        f"{current_app.config['WHATSAPP_API_URL']}"
        f"/{current_app.config['WHATSAPP_PHONE_NUMBER_ID']}/messages"
    )
    headers = {
        "Authorization": f"Bearer {current_app.config['WHATSAPP_ACCESS_TOKEN']}",
        "Content-Type": "application/json",
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {"body": body},
    }

    resp = requests.post(url, json=payload, headers=headers, timeout=10)
    if resp.ok:
        logger.info("Reply sent to %s", to)
    else:
        logger.error("Failed to send reply: %s %s", resp.status_code, resp.text)
