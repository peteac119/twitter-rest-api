# Twitter Rest Service 
Twitter API client for test

# Project Explanation
I have coded this API client on the assumption that it has Twitter account registered in Twitter Developer site.
Consumer key and consumer secret are required if you are willing to connect to Twitter API. 

This rest client supports only 2 feature: searching tweets by hashtags or by user. It has used the Application-only 
Authentication to call API.

#Requirement
- Python 3.6
- Docker

# Clone the project from GitHub
Please run "git clone https://github.com/peteac119/twitter-rest-api.git" It only has master branch.

# How to run unit test
1. Please go to root folder of the project where "tests" folder located.
2. Run "python3 -m venv ./venv"
3. Run "venv/bin/pip install -r requirements.txt"
4. Run "venv/bin/pytest" --> With this command, it will run all unit tests.

# How to build and run app
1. Before you build and start an app, please make sure that you configure the following variables inside .env file.
- TWITTER_CONSUMER_K={{your consumer key here}}
- TWITTER_CONSUMER_S={{your consumer secret here}}
2. Docker compose can build and start an application by running "docker-compose up --build"

# Available URL of this app
1. http://localhost:5000/hashtags/your_hashtag?limit=20
2. http://localhost:5000/users/your_user?limit=20

Note: 'limit' at query string is optional.
