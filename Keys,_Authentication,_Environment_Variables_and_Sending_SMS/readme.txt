*** How to authenticate ourselves with an API provider so that we can access more secure and more valuable data from the API providers ??????

    previously all-of-the APIs that we've used were free APIs; they were provided completely free and we can access all parts of it without any
    sort of payment, this is because the data that's contained in those APIs are very simple and nobody is going to be using that data to build a
    very fancy or big commercial application.

    on the other hand there are other types of data that are very valuable. Example: weather data because it takes a lot of energy
    and time to collect all of this data and provide it for you; and in such cases some of these APIs can have a paid tier, so you actually
    have to pay if you really need this data; but luckily most of these APIs provide a free tier that allows you to test out the application
    and if you are somebody who's just learning the ropes then it doesn't make sense to charge you. it only makes sense when your application
    or your service has a lot of users.


*** How to prevent people from abusing this free tier???

    the way websites prevent people from abusing their service is through "API key". Its almost like your personal account
    number and password.

    through this API key the API provider can track how much you're using their API and to authorize your access and deny the access
    once you've gone over the limit.

    different API providers tend to have different ways that you can authenticate yourself with them but most of them involve
    some sort of an API key


*** steps to use API

        1) read documentation (imp)
        2) sign in to have your own API id and grab your own API key
        3) test any of API call
            http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API key}



*** Sending message to the user

        the "twilio" API allows us to send text messages or phone calls or have a virtual phone number in any country.
        You can develop a bunch of amazing apps using twilio such as an ordering system, phone verification, sms notification. etc....
        "https://www.twilio.com/"

        click get started for free > sign up



(Note : if you have huge JSON data and having difficulty to read copy and paste your data to
"http://jsonviewer.stack.hu/", in the viewer section it will nicely format your data and increase the readability. )