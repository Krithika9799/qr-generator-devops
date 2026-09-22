from flask import Flask, request, render_template_string
import qrcode
import base64
from io import BytesIO

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>QR Code Generator</title>

    <style>
        body {
            font-family: Arial;
            text-align: center;
            margin-top: 80px;
        }

        input {
            width: 350px;
            padding: 12px;
        }

        button {
            padding: 12px 20px;
            cursor: pointer;
        }

        img {
            margin-top: 20px;
        }
    </style>
</head>

<body>

<h1>QR Code Generator</h1>

<form method="POST">

    <input
        type="url"
        name="url"
        placeholder="Enter URL"
        required
    >

    <button type="submit">
        Generate QR
    </button>

</form>

{% if qr_code %}
    <h3>Scan this QR code</h3>

    <img src="data:image/png;base64,{{ qr_code }}">

{% endif %}

</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def home():

    qr_code = None

    if request.method == "POST":

        url = request.form["url"]

        qr = qrcode.make(url)

        buffer = BytesIO()

        qr.save(buffer, format="PNG")

        qr_code = base64.b64encode(
            buffer.getvalue()
        ).decode()

    return render_template_string(
        HTML,
        qr_code=qr_code
    )


@app.route("/health")
def health():

    return {
        "status": "UP",
        "application": "QR Generator"
    }


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000
    )