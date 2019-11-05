import json

s = '''
{'conversation_uuid': 'CON-4826b182-e712-4e40-bf8f-2ebdd2b9f559',
 'direction': 'inbound',
 'from': '447724161480',
 'network': None,
 'rate': None,
 'start_time': None,
 'status': 'answered',
 'timestamp': '2019-11-05T09:51:24.874Z',
 'to': '447418340545',
 'uuid': 'd99a27f42df634c6551e3dc2b337ed1b'}
'''

t = json.loads(s)



