from flask import Flask, request, send_file
import os

app = Flask(__name__)

# Allowed host for the protected route
ALLOWED_HOST = 'brewith.us'

@app.route('/api/hello/<name>', methods=['GET'])
def protected_hello(name):
    # # Check if the request is coming from the allowed host
    if request.headers.get('Host') == ALLOWED_HOST:
        return f'Hello, {name}!'
    else:
        index_path = os.path.join(app.root_path, 'denied.html')
        return send_file(index_path)

@app.route('/', methods=['GET'])
def unprotected_route():
    index_path = os.path.join(app.root_path, 'index.html')
    return send_file(index_path)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5050,debug=True)