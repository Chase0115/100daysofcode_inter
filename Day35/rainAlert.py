import requests
import os
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
account_sid = os.environ['ACbd5f7c2c8d1b47fb20a3bf481473ebb0']
auth_token = os.environ['ab1f749c54f1c3146fb55209d4851a9f']

weather_params = {
    "lat": 19.075983,
    "lon": 72.877655,
    "exclude": "current,minutely,daily",
    "appid": "513f50c84471b09e583dc0e128167560"
}

r = requests.get(OWM_Endpoint, params=weather_params)
r.raise_for_status()

weather_data = r.json()
hourly_data = weather_data['hourly'][:12]

is_rain = False

for hour in hourly_data:
    condition_code = hourly_data['weather'][0]['id']
    if int(condition_code) < 700:
        is_rain = True

if is_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to take umbrella.",
        from_='+12693011560',
        to='+61413405152'
    )
    print(message.status)
