from flask import Flask, render_template_string
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta property="og:title" content="Demo WhatsApp Thumbnail" />
        <meta property="og:description" content="Test WhatsApp Business API link preview with thumbnail"/>
        <meta property="og:image" content="https://fastly.picsum.photos/id/431/200/200.jpg" /> <!-- Replace with your image URL -->
        <meta property="og:url" content="{{ request.url }}" />
        <meta name="twitter:card" content="summary_large_image" />
        <title>Test WhatsApp Thumbnail</title>
    </head>
    <body>
        <h1>WhatsApp Business API Thumbnail Demo</h1>
        <p>If you share this link on WhatsApp, a preview with the above image will be generated.</p>
    </body>
    </html>
    ''')

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
