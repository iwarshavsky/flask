from flask import Flask, render_template_string
import os

app = Flask(__name__)
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def redirect_all(path):
    return redirect("https://example.com", code=302)  # Change to your desired URL

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
