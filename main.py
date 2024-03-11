import requests
from twilio.rest import Client


OMW_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "YOUR API FROM OPENWEATHERMAP.ORG"
LAT = 44.426765
LONG = 26.102537

account_sid = 'YOUR ACCOUNT SID FROM TWILIO'
auth_token = 'YOUR ACCOUNT TOKEN FROM TWILIO'


weather_params = {
    "lat": LAT,
    "lon": LONG,
    "appid": api_key,
    "cnt": 4,

}

response = requests.get(OMW_Endpoint, params=weather_params)
response.raise_for_status()

weather_data = response.json()


will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Hei, vezi ca va ploua azi. Nu uita sa iei umbrela cu tine",
        from_='twilio number',
        to='yours number'
    )
    # print(message.status)
