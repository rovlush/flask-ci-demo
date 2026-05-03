from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "status": "success",
        "message": "Hello from the automated pipeline!",
        "version": "1.0.0"
    })

@app.route("/health")
def health_check():
    # This endpoint is used by the pipeline to verify the app is live
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    # We use 0.0.0.0 so it's accessible outside the Docker container
    app.run(host="0.0.0.0", port=5000)