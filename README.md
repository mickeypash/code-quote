# code-quote

[![build-status-image]][travis]
[![coverage-status-image]][codecov]
[![pypi-version]][pypi]


```
┌────────────────────┐
│   code-quote-cli   │
│                    │
└────────────────────┘
┌───────────────────────────────────────────────────┐
│                        CDN                        │
└───────────────────────────────────────────────────┘
┌───────────────────────┐   ┌───────────────────────┐
│                       │   │                       │
│         redis         │   │    code-quote-www     │
│                       │   │                       │
└───────────────────────┘   └───────────────────────┘
┌───────────────────────┐   ┌───────────────────────┐
│                       │   │                       │
│        mongodb        │   │    code-quote-nlp     │
│                       │   │                       │
└───────────────────────┘   └───────────────────────┘
┌───────────────────────┐   ┌───────────────────────┐
│                       │   │                       │
│code-quote-web-scraper │   │    code-quote-ocr     │
│                       │   │                       │
└───────────────────────┘   └───────────────────────┘

```

# List of dependencies

- NLTK + TextBlob - natural language processing (ML for extacting quotes)
- PyOCR - reading books from which to extract quotes
- Scapy - for scrapping web sources (blogs, websites)
- Pattern - for web mining (Google, Twitter, Wiki API)

# Currently installed this
- Elasticsearch - search engine
- Django - web framework
- Django Rest Framework - restful api

# Considering 
- Eve - rest config, security, auth, redis, elasticsearch, mongodb (built in)

A barebones Python app, which can easily be deployed to Heroku.

This application supports the [Getting Started with Python on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python) article - check it out.

## Running Locally

Make sure you have Python [installed properly](http://install.python-guide.org).  Also, install the [Heroku Toolbelt](https://toolbelt.heroku.com/) and [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```sh
$ git clone git@github.com:heroku/python-getting-started.git
$ cd python-getting-started

$ pip install -r requirements.txt

$ createdb python_getting_started

$ python manage.py migrate
$ python manage.py collectstatic

$ heroku local
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master

$ heroku run python manage.py migrate
$ heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)
- [What makes a good quote](http://journalism.about.com/od/reporting/a/goodquotes.htm)