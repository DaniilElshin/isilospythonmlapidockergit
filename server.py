#coding: utf-8

import os, json

from flask import Flask, request, jsonify

from siloRefill import siloRefill

port = int(os.getenv("PORT", 8080)) #8080 is value by default
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def root():
    if request.method == 'POST':
        return process_request(request, siloRefill.getWebResponse)
    else:
        return jsonify(
                status=200,
                response={
                    'message': 'GET successfull',
                    'request': str(request)
                }
            )

def process_request(request, clientApiMethod):
    request_payload = json.loads(request.get_data().decode('utf-8'))
    return clientApiMethod(request_payload, request)

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=port)
