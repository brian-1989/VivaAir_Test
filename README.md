# API service and story search

<hr>

![VivaAir](https://myfirstbucketbrian.s3.amazonaws.com/VivaAir.jpg)

<hr>

This test is requested by the company VIVA AIR for the development of an API. It involves querying the hacker-news APIs on the Topstories and item endpoints, which originate the latest real-time POSTs of Hacker News data. The user when querying our API, can filter the number of news he wants to see, and does so with an index i and a maximum number of stories n.

Project carried out using Django, rest framework, redis-server and docker.

<hr>

## How to Run

To run it make sure of the following:

* Clone this repository
* Install the packages contents in the
 ```requierments.txt``` file
* Finally, Finally, run the Djando server with the command: python3 manage.py runserver 5000. If you want to specify the port or by default it is port 8000.

Once you have the server running you should see something like this

```
System check identified no issues (0 silenced).
December 16, 2021 - 21:41:38
Django version 4.0, using settings 'apiviva.settings'
Starting development server at http://127.0.0.1:5000/
Quit the server with CONTROL-C.
```
<hr>

## Description

This is an API designed to filter the information originated by Hacker News APIs. How is it done?. There are two ways to do this:  
1. from a browser the API URL is the following ```http://localhost:5000/api/v1```, at the end of the URL I can put the parameters or the range I want to see the latest Hacker News POSTs. Example:

![Browser](https://myfirstbucketbrian.s3.amazonaws.com/Browser.png)

2. From a tool to do REST API testing, put the URL of the api and in the body I can pass the parameters type Json. Example:

![Thunder Cliente](https://myfirstbucketbrian.s3.amazonaws.com/Thunder_Client.png)

<hr>

## Author
:man_technologist: **Brian Zapata**
* [GitHub](https://github.com/brian-1989)
* [Twitter](https://twitter.com/BrianZa03390210)
