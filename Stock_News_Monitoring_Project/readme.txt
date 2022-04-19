A lot of the people who trade stocks professionally have access to "Bloomberg terminal".

Bloomberg terminal provides a lot of stings such as current stock prices of a particular company, breaking news relevant to those companies (tells reason for stocks went up or down), etc.

nad it also gives the ability to alert you when relevant pieces of news happen that are related to stocks that you're following.

We are going to DIY our own Bloomberg terminal or at least the parts of the functionality that are quite useful i.e.

            * STEP - 1: we will be fetching last 2 day's closing market stock prices and compute the difference between them and cac result in percentage and send
                an alert to the user that weather user should buy stocks today or not based on the market value of yesterday

            * STEP - 2: we will fetch the news also which tells the reason behind the rise and fall for profit in stock

            * STEP - 3: send sms to ourselves telling us what was the big fluctuation that happened and what is the relevant news so that we can decide there and then
                         whether if we want to sell or buy stocks.

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
