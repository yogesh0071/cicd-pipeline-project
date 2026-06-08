from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>DevOps dev/CI/CD Pipeline - Yogesh Nimje</h1><p>Deployed automatically via Jenkins & Docker</p>"

@app.route('/health')
def health():
    return {"status": "healthy"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)