import requests
from decouple import config         # accessing env variables
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API = config('STOCK_API_KEY')
NEWS_API = config('NEWS_API_KEY')
twilio_sid = config('TWILIO_SID')
twilio_auth_token = config('TWILIO_AUTH_TOKEN')

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API,      #config('MY_API')

}


response = requests.get(url=STOCK_ENDPOINT,params=stock_params)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [val for (key,val) in data.items()]
yesterday_closing_price = data_list[0]["4. close"]                     # yesterday's closing price

#TODO 2. - Get the day before yesterday's closing stock price

day_before_yesterday_closing_price = data_list[1]["4. close"]

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

pos_diff = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if pos_diff > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

diff_percentage = round((pos_diff / float(yesterday_closing_price))*100)
print(diff_percentage)

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.


    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

news_params = {
    "q" : COMPANY_NAME,
    "sortBy" : "publishedAt",
    "apikey" : NEWS_API
}


if abs(diff_percentage) < 5:
    print("Get News")
    response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    response.raise_for_status()
    data = response.json()
    # print(data)

    articles = data['articles']
    # print(articles)


#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

    three_articles = articles[:3]
    # print(three_articles)


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    # formatted_articles = []
    # for article in three_articles:
    #     formatted_articles.append(f"Headline: {article['title']}. \nBrief: {article['description']}")
    # print(formatted_articles)

    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percentage}% \nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
    print(formatted_articles)

#TODO 9. - Send each article as a separate message via Twilio.

    client = Client(twilio_sid, twilio_auth_token)
    for article in formatted_articles:
        print(article)
        message = client.messages \
            .create(
                body=article,
                from_='+15716006490',
                to='+159890237728'
            )

        print(message.status)



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

