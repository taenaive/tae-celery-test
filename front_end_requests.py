import requests

payload = {
  "projectid": 12345,
  "text": "string"
}
# r = requests.get('http://localhost:8000/ner/123')
# print(help(r))
r = requests.post('http://localhost:8000/nerproject', json=payload)
print(r.status_code)
print(r.headers)
print(r.text)
