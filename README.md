## YelpViz

### Project Description
![Alt text](./client/src/images/SysOverview.png?raw=true "System Overview")

`[strong]YelpViz[strong]`, which is a visuaization system aiming at exploring restaurants locations with differnt health scores in major cities of US. This project of COMP4901F `Data Visualization` @HKUST and also a champion hackthon project for `HealthCare` division of hackUST.

It’s the first time that Yelp dataset provides photos for each restaurant, so we decide to make use of these images and hopefully we can have some new findings in the end. However, images provided by Yelp had no meaning since each image does not associate with its restaurant, thus they were just a mess originally. To deal with this challenge, we decided to crawl all food images in a given city and manually labled each image with a healthy score.

In this project, we used deep learning to predict how “healthy” a food is by analysing its photo as well as the title of the photo. First, after crawling more than 5000 food images of two major cities, `Cleveland` and `Madison`, from Yelp dataset and labling each image with a healthy score, we trained these images as samples with neural network `GoogleNet[https://www.cs.unc.edu/~wliu/papers/GoogLeNet.pdf]`, which achieved 85% accuracy in the end.

> Note that the dataset is almost 2GB.

### Prerequest

`Python 2.7`, `virtualenv`, `node`

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

### Local Http Server
``` bash
#Install http-server
npm install -g http-server
# enter the front end sub-directory
cd ./client/images/
# start the server so we can access images
http-server -p 8888
```