import requests
r = requests.get('http://localhost:8000/ner/123')
# print(help(r))

print(r.text)
