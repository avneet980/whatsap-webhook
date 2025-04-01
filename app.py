from flask import Flask, request, jsonify

app = Flask(name)

@app.route("/", methods=["GET"])
def verify():
    challenge = request.args.get("hub.challenge")
    return challenge if challenge else "Webhook Running!"

@app.route("/", methods=["POST"])
def webhook():
    data = request.json
    print("Received:", data)
    return jsonify({"status": "received"}), 200

if name == "main":
    app.run(host="0.0.0.0", port=5000)
