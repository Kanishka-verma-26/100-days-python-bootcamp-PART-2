when we browse in the net, we might have realised that there's a lot of websites out there that carry a whole bunch
of data. Such as :
        next week's weather predictions at weather forecast app/ website.
        current market value of various cryptocurrencies at Coinbase website.
        stats about your favourite basket ball player at MBA website.


these websites have their own APIs

what if we wanted to use the data that the websites have? How can we tap into it and use it in our own programs?
Hence that's where API comes into the play

An Application Programming Interface (API) is a set of commands, functions, protocols and objects, that programmers can
use to create software or interact with an external system.

Essentially an API is an interface or rather a sort of barrier between your program and an external system

to pull some piece of data through API we need to follow the API rules to make a request to the external system.
And if you have structured your request according to all of the requirements that this external system has set out in their API,
then they will respond to you appropriately and give you the data that you want; Hence following the rules is important.


** example to understand : Imagine these websites as the sort of restaurant and the data that powers these websites as kitchen ingredients
    behind the scene. we can't really go to a restaurant as a member of the public and just go in to the kitchen and start raiding their cupboards.
    instead in a restaurant we have a menu i.e. a kind of like an interface between us and the restaurant. It's the thing that
    tells you what you can order and what you can't. Essentially an API is exact that. It's the menu, its all of the things that
    you can do to interact with an external system such as a website that carries data.


** API Endpoint : it's the one of the most important aspects of an API, you can imagine it as a location such as
    if you want to get data from a particular external service then we need to know what location that data is stored.
    example: if you want to get money out of a bank you need to know where that bank is.
    an API Endpoint is just an URL.

    now, in addition to knowing the API endpoint, you also have to make a request over the internet. (this API request
    is kind of similar to going to the bank and trying to withdraw some money out from your vault and for that we need to make a
     request to the cashier and here the cashier is acting like an API between you and the bank vault


one of the simplest API website is : "http://open-notify.org/Open-Notify-API/ISS-Location-Now/"
when you click on the link inside this link you will get the data in dictionary format


when we make requestes from a url we get response code instead of data, Response code actually have a very specific meaning,
but the most important thing they tell us is if our request succeeded or failed,
you can summarise these status codes just by looking at the first number :

            * 1XX : Hold On
            * 2XX : Here you go, everything was successful
            * 3XX : Go Away, you dont have permission to access this thing
            * 4XX : You screwed up, thing you are looking for doesn't exist
            * 5XX : Server screwed up, server is down/ other issue


** API Parameters
        API Parameters allows you to give an input when you are making your API request, so that you can get different pieces of data back
        depending on your input (same as function parameters)

        not all APIs have parameters, some are incredibly simple whereas other ones allow you to provide parameters

        "https://sunrise-sunset.org/api" this is a sunrise-sunset api that gives you the time when the sun gonna rise and set based upon your latitude and longitude parameters




