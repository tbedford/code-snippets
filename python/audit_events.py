#!/usr/bin/env python3

import requests
from requests.auth import HTTPBasicAuth
from flask import Flask, request, jsonify

NEXMO_API_KEY = ''
NEXMO_API_SECRET = ''

app = Flask(__name__)

template1 = '''
<html>
  <head>
    <title>Audit Event Types</title>
  </head>
  <body>
    <form action='/events' method='get'>
      <select name='event_type'>
        <option value='ALL'>ALL -- All the event types</option>
        {SELECT_OPTIONS}
      </select>
      <input type='submit'>
    </form>
  </body>
</html>
'''

template2 = '''
<html>
  <head>
    <title>Audit Events Listing</title>
  </head>
  <body>
    <table border='1'>
      <tr><th>Audit Event Type</th><th>Date/time of event</th><th>Event source</th><th>Context</th></tr>
        {TABLE_ROWS}
    </table>
  </body>
</html>
'''


@app.route("/")
def root():
    r = requests.options('https://api.nexmo.com/beta/audit/events', auth=HTTPBasicAuth(NEXMO_API_KEY, NEXMO_API_SECRET))
    j = r.json()
    event_types = j['eventTypes']

    select_options = ""
    for evt_t in event_types:
        select_options = select_options + "<option value='" + evt_t['type'] + "'>" + evt_t['type'] + " -- " + evt_t['description'] + "</option>"

    html = template1.format(SELECT_OPTIONS=select_options)
    return (html)

@app.route("/events")
def events():
    params = request.args
    EVT_TYPE = params['event_type']
    
    if EVT_TYPE == 'ALL':
        r = requests.get('https://api.nexmo.com/beta/audit/events', auth=HTTPBasicAuth(NEXMO_API_KEY, NEXMO_API_SECRET))
    else: 
        r = requests.get('https://api.nexmo.com/beta/audit/events?event_type='+EVT_TYPE, auth=HTTPBasicAuth(NEXMO_API_KEY, NEXMO_API_SECRET))

    j = r.json()
    
    if '_embedded' in j:
        events = j['_embedded']['events']
    else:
        return ("No Events Found")

    table_rows = ""
    for evt in events:
        if 'context' in evt:
            event_context = str(evt['context'])
        else:
            event_context = 'None'
        table_rows = table_rows + "<tr><td>" + (evt['event_type'] + "</td><td>" + evt['created_at'] + "</td><td>" + evt['source'] + "</td><td>" + event_context + "</td></tr>")
        
    html = template2.format(TABLE_ROWS=table_rows)
    return(html)
            
if __name__ == '__main__':
    app.run(port=9000)
