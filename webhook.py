import os
import logging
from flask import Flask, jsonify

log = logging.getLogger("werkzeug")
log.setLevel(logging.ERROR)          # silence Flask request logs

app = Flask(__name__)


@app.route("/")
def root_route_handler():
    return jsonify("BotifyX-Botz - The Bot shall follow my command")


@app.route("/health")
def health_check():
    return jsonify({"status": "OK"})


def start_webhook():
    """
    Start the Flask web server.
    Reads PORT from the environment so Render (and similar platforms)
    can inject their own port. Falls back to 8000 for local use.
    """
    port = int(os.environ.get("PORT", 8000))
    print(f"[Webhook] Flask listening on 0.0.0.0:{port}")
    # use_reloader=False is mandatory inside a daemon thread
    app.run(host="0.0.0.0", port=port, threaded=True, use_reloader=False)
