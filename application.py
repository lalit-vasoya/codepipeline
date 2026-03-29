from flask import Flask

# IMPORTANT: variable name must be 'application'
application = Flask(__name__)

@application.route("/")
def home():
    return """
    <html>
        <head>
            <title>Beanstalk App</title>
        </head>
        <body>
            <h1>🚀 Hello from AWS Elastic Beanstalk which deployed using CodePipeline</h1>
            <p>Your Flask app is running successfully on port 80!</p>
        </body>
    </html>
    """

@application.route("/health")
def health():
    return {"status": "ok"}, 200


# Only for local testing (Beanstalk ignores this)
if __name__ == "__main__":
    application.run(host="0.0.0.0", port=5000, debug=True)

