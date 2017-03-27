# Healthy Yelp Viz

> Healthy Yelp Viz
## Prerequest

`Python 2.7`, `virtualenv`, `node`

## Web Server Setup

``` bash
# initalize virtual env
virtualenv venv

# activate virtual env
source ./venv/bin/activate

# install python dependencies
pip install -r requirements.txt

# run web server
python run.py
```

## Front End Setup

``` bash
# enter the front end sub-directory
cd ./client

# install front-end dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build
```
