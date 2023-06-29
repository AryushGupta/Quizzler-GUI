import requests

url = "https://opentdb.com/api.php?"

# change the playload acc. to your needs!
payload = {
    "amount": 10,
    "type": "boolean"
}

data = requests.get(url, params=payload)
question_data = data.json()["results"]
