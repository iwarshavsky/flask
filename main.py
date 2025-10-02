from flask import Flask, redirect, request, abort
import os
import urllib.parse

app = Flask(__name__)

@app.route('/', methods=['GET'])
def forward_to_next():
    next_url = request.args.get('next')
    # Optional: Validate the URL (basic check)
    if not next_url or not urllib.parse.urlparse(next_url).scheme:
        abort(400, description="Missing or invalid 'next' parameter")
    return redirect(next_url)

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
