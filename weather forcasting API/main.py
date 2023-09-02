import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "a6122abee80c5690aa51517a8709aced"
account_sid= "AC17c1e377008871012cc65605a65ba602"
auth_token = "7f2c786b69cdd61cdd169bd5cf6c1d7d"

weather_params = {
    "lon": 80.946167,
    "lat": 26.846695,
    "appid": api_key,
}
response = requests.get(url=OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slise = weather_data['hourly'][:12]

will_rain = False
for hour_data in weather_slise:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body = "It`s going to rain today. Remember to bring an ☔ ",
        from_ ='+12708133095',
        to='+919389872806'
    )

    print(message.status)