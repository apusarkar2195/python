import json
with open('/home/apu/Desktop/python/example_2.json','r') as f:   #insert your json file path
	data=json.load(f)

def json_parser(node_ptr):
	for key,val in node_ptr.items():
		if isinstance(val,dict):     
			json_parser(val)
		else:
			print(key," : ",val)

json_parser(data)			
