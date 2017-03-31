## Healthy Yelp Viz

###Project Description
> Healthy Yelp Viz
> This is a course project of COMP4901F `Data Visualization`@HKUST.

> It’s the first time that yelp dataset provides photos, so we decide to make use of photos and hopefully we can have some new findings.

> In this project, we will use deep learning to predict how “healthy” a food is by analysing its photo as well as the title of the photo.

<hr/ >

### Prerequest

`Python 2.7`, `virtualenv`, `node`
<hr/ >

### Web Server Setup

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
<hr/ >

### Front End Setup

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

