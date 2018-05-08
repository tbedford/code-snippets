#!/usr/bin/env python3
from flask import Flask, request, jsonify
from pprint import pprint

app = Flask(__name__)

tune_1 = ["https://raw.githubusercontent.com/tbedford/git-testing-repo/master/tunes/Komiku_Sunset_on_the_beach.mp3"]
tune_2 = ["https://raw.githubusercontent.com/tbedford/git-testing-repo/master/tunes/Rushjet1_Azureflux_Remix.mp3"]
tune_3 = ["https://raw.githubusercontent.com/tbedford/git-testing-repo/master/tunes/Kris_Keyser_Only.mp3"]

@app.route("/webhooks/answer")
def answer_call():
    params = request.args
    print("DIAL_A_CHIP_TUNE CALL FROM: >%s<" % params['from'])
#    for param_key, param_value in request.args.items():
#        print("PARAM: {}: {}".format(param_key, param_value))
    input_webhook_url = request.url_root + "webhooks/dtmf"
    ncco = [
        {
            "action": "talk",
            "text": "Welcome to dial a chiptune. Press 1 or 2."
        },
        {
            "action": "input",
            "maxDigits": 1,
            "timeOut": 5,
            "eventUrl": [input_webhook_url]
        } 
    ]
    return jsonify(ncco)

@app.route("/webhooks/dtmf", methods=['POST'])
def dtmf_webhook():
    data = request.get_json()
    #pprint(data)
    selection = data['dtmf']
    print("TUNE SELECTED = %s" % selection)    
    MESSAGE = "Playing tune " + selection
    if selection == "1":
        #print("DEBUG: Selecting tune 1")
        tune_x = tune_1
    elif selection == "2":
        tune_x = tune_2
    else:
        tune_x = tune_3 

    ncco = [
        {
            "action": "talk",
            "text": MESSAGE
        },
        {
            "action": "stream",
            "streamUrl": tune_x
        }    
    ]
    return jsonify(ncco)    


if __name__ == '__main__':
    app.run(host="www.yourdomain.com", port=9000)
