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

        click get started for free > sign up > Dashboard > get a trial number > DOCS > Quickstarts >
            programmable SMS Quickstart > select your language (you will get your example code )
             > download twilio library (pip install twilio) > get your 'account_sid' and 'auth_token'
             from console > create your client at the point where we want to send ourselves a SMS message >
             edit from and to variable > and send messages.


        --> example code to send SMS from twilio

                    """
                    import os
                    from twilio.rest import Client


                    # Find your Account SID and Auth Token at twilio.com/console
                    # and set the environment variables. See http://twil.io/secure
                    account_sid = 'TWILIO_ACCOUNT_SID'
                    auth_token = 'TWILIO_AUTH_TOKEN'
                    client = Client(account_sid, auth_token)

                    message = client.messages \
                                    .create(
                                         body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                                         from_='+15017122661',
                                         to='+15558675310'
                                     )

                    print(message.sid) """

*** run your script daily

        * go to python anywhere > signup on 'pythonanywhere.com' >
        * files > upload files > consoles > Bash > Type 'python3 rain_alert.py' >
        * you will get an exception and a connection error, if we use pythonanywhere paid version we won't get any error but
         as we are using pythonanywhere as free account i.e. a proxy server the twilio API client needs to be told how to connect
         to the proxy server that free accounts use to access the external internet.

                we need to make changes in your code at pythonanywhere to run daily:
                    """
                        import os
                        from twilio.rest import Client
                        from twilio.http.http_client import TwilioHttpClient

                        proxy_client = TwilioHttpClient()
                        proxy_client.session.proxies = {'https': os.environ['https_proxy']}

                        account_sid = 'your account id here'
                        auth_token = 'your twilio token here'

                        client = Client(account_sid, auth_token, http_client=proxy_client)

                        # twilio api calls will now work from behind the proxy:
                        message = client.messages.create(to="...", from_='...', body='...')
                        """

        *** ( Note: do not aopply above changes in your python script else it wont run in your console, to maintain running running of code on both platforms, make changes in your python anywhere code only. )

         * save code > rerun Type 'python3 rain_alert.py'
         * (now schedule a task to run it everyday) Tasks > schedule your time according to UTC and type same command (python3 rain_alert.py) at UTC section



    (now schedule a task to run it everyday) Tasks > schedule your time according to UTC and type same command (python3 rain_alert.py)
    at UTC section """




(Note : if you have huge JSON data and having difficulty to read copy and paste your data to
"http://jsonviewer.stack.hu/", in the viewer section it will nicely format your data and increase the readability. )



*** Environment Variables

        * go to terminal > type "env"
                we can see a whole bunch of variables, we got a key and a value; these are the different variables that are set in the environment in which
                your code is running

                these variables have values which are strings that can be used in our applications or our code

        * Environment Variables used for
                1) Convenience : normally when you deploy a large application, the process is quite complicated. and once you've done it; you don't want to mess
                                around with the code base and update the code files. Instead you have these environment variables, which you can change.

                                eg : if you have an application that was sending you emails out to your clients, then your client base emails might change day to day.
                                        so certain variables that being used in your code base could be set as environment variables and you can modify those variables
                                        without having to touch the code.

                2) Security : when you're developing software, you might be uploading your code based somewhere such as store it online or to a service like PythonAnywhere.
                                and it's usually not a good idea to have things like your authentication keys or your API keys to be stored in the same place as the rest of your code.


        * Environment Variables essentially allow us to separate out where we store our keys, our secret stuff, and various other variables away from where our code base is located.

        (Note : always secure your API key and Auth Token )

        * create temporary Environment Variable till shell runs

                "export <variable_name>=<variable_value>"      # no space and quotation

        * create Permanent ENV Variable Key

                -> pip install python-decouple
                -> touch .env   # create a new .env file
                -> nano .env    # open the .env file in the nano text editor
                -> add your environment variables like this:
                        USER=alex
                        KEY=hfy92kadHgkk29fahjsu3j922v9sjwaucahf
                        (Then save (WriteOut) the file and exit nano. Your environment variables are now stored in your .env file.)

                -> access env variables in your python code like:
                        from decouple import config

                        API_USERNAME = config('USER')
                        API_KEY = config('KEY')




        * fetch Environment Variable

                 os.environ.get('<variable_you_want_to_fetch>') or os.getenv('<variable_you_want_to_fetch>') in python anywhere
                                    and
                 config('<variable_you_want_to_fetch>') in pycharm