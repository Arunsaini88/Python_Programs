import requests
from twilio.rest import Client
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

TWILIO_SID = "AC17c1e377008871012cc65605a65ba602"
TWILIO_AUTH_TOKEN = "7f2c786b69cdd61cdd169bd5cf6c1d7d"

STOCK_API = "https://www.alphavantage.co/query"
STOCK_API_KEY= "40E9EBOSAJVUEHIJ"

NEWS_API = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "6ad43b7ca0964f5480a93c1c3d4e5915"
## STEP 1: Use https://www.alphavantage.co/
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_prams = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}
response = requests.get(STOCK_API, params=stock_prams)
stock_data = response.json()["Time Series (Daily)"]
print(response.json())
stock_data_list = [value for (key, value) in stock_data.items()]
yesterday_data = stock_data_list[0]
yesterday_closing_data = yesterday_data["4. close"]
print(yesterday_closing_data)

day_before_yesterday_data = stock_data_list[1]
day_before_yesterday_closing_data = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_data)
#
different = float(yesterday_closing_data) - float(day_before_yesterday_closing_data)
up_down =None
if different > 0:
    up_down ="🔺"
else:
    up_down= "🔻"

diff_percentage = round(different/float(yesterday_closing_data) * 100)
print(diff_percentage)

if abs(diff_percentage) > 5:
    print("Get News")
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    date_list = [key for (key, value) in stock_data.items()]
    yesterday_date = date_list[0]
    news_prams = {
        "qInTitle":COMPANY_NAME,
        "apikey": NEWS_API_KEY,
    }
    news_response = requests.get(NEWS_API, params=news_prams)
    three_articles = news_response.json()["articles"][:3]
    print(three_articles)
#
## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
    format_articles = [f"{STOCK}:{up_down}{diff_percentage}%\nHeadline: {article['title']}.\nBrief: {article['description']}" for article in three_articles]
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in format_articles:
        message = client.messages.create(
            body=article,
            from ="+12708133095",
            to="+919389872806",
#         )


