import requests

parameters = {
    'amount': 10,
    'type': 'boolean',
    "category": 18
}

r = requests.get(url='https://opentdb.com/api.php', params=parameters)
r.raise_for_status()
data = r.json()
question_data = data['results']
