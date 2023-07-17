import json
  
# Opening JSON file
f = open('data2.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
  
# Iterating through the json list
list_input = []
for i in data:
    for key,value in i.items():
        list_input.append(value)

# Closing file
print(list_input)
f.close()