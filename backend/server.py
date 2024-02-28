from flask import Flask, request, Response
from flask_cors import CORS
import json, time

app = Flask(__name__)
CORS(app)
datadict = {}

@app.route("/webhook", methods=['GET', 'POST'])
def webhook():
    if request.method == 'POST':
        webhookpayload = json.loads(request.data)
        datadict.update(webhookpayload)
        return {'code': 'post successful'}
    elif request.method == 'GET':
        return {'code': 'Nothing to see here, move along.'}

@app.route("/stream/", methods=['GET'])
def stream():
    def update():
        while True:
            time.sleep(15)
            yield f'data:[{json.dumps( '### INSERT your datadict.get("xxxxx") key here. ###')}]\n\n'
    return Response(update(), mimetype='text/event-stream')

if __name__ == "__main__":
    app.run(debug=False)