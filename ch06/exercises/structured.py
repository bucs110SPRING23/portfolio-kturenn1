
#json is a string format not a file format
#only types of data - int, float, string, boolean, list, dictionary, None
import json

json_string = json.dumps(data)
print(json_string, type(json_string))

json_data = json.loads(json_string)

for k, v in json_data.items():
    print(k, v)

fptr = open("assets/data.json", "w")
h