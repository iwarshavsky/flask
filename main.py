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
    
    # Reconstruct full destination URL, default to https
    destination = f"https://{url_path}"
    if request.query_string:
        destination += '?' + request.query_string.decode()
    return redirect(destination)

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
