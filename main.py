import logging
from flask import Flask, redirect, request
import os


app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.before_request
def log_full_request():
    headers = "\n".join(f"{k}: {v}" for k, v in request.headers.items())
    app.logger.info(
        f"Request: {request.method} {request.url}\nHeaders:\n{headers}"
    )

@app.route('/<path:url_path>')
def smart_redirect(url_path):
    user_agent = request.headers.get("User-Agent", "").lower()
    
    # Reconstruct full destination URL, default to https
    destination = "https://www.google.com/"
    if "whatsapp" in user_agent:
        destination = f"https://{url_path}"
        if request.query_string:
            destination += '?' + request.query_string.decode()
    return redirect(destination)

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))


@app.route('/')
def index():
    user_agent = request.headers.get("User-Agent", "").lower()
    if "whatsapp" in user_agent:
        return jsonify({"message": "Hello WhatsApp user! Doing something special."})
    else:
        return jsonify({"message": "Hello regular user!"})
