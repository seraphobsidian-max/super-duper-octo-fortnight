import time
import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/share', methods=['POST'])
def handle_share():
    data = request.json
    token = data.get('token')
    link = data.get('link')
    limit = data.get('limit', 1)
    
    logs = []
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }

    count = 0
    for i in range(limit):
        try:
            url = f"https://graph.facebook.com/me/feed?link={link}&access_token={token}"
            response = requests.post(url, headers=headers)
            
            if response.status_code == 200:
                count += 1
                logs.append(f"[{count}] Shared successfully.")
            else:
                logs.append(f"Failed to share. Status Code: {response.status_code}")
        except Exception as e:
            logs.append(f"Error: {str(e)}")
        
        time.sleep(1)
        
    return jsonify({"status": "done", "logs": logs})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
