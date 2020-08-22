# Also makes sure JSON is pretty printed    
write_file('metadata.json', json.dumps(objects, indent=4, sort_keys=True))
