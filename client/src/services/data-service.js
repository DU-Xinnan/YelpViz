let instance = null;

class Service {
    constructor() {
        if (!instance) {
            instance = this;
        }
        this.data = undefined;
        this.rawData = undefined;
        this.checkinTime = undefined;
        this.dataWithValidImg = undefined;
        this.businessID2Img = undefined;
        this.id2index = undefined;
        this.city = undefined;
        this.cloudData = undefined;
        this.sentimentData = undefined;
        return instance;
    }

    setData(data) {
        this.data = data;
    }

    setCity(city) {
        this.city = city;
    }
    getCity() {
        return this.city;
    }
    setCloudData(data) {
        this.cloudData = data;
    }

    getCloudData() {
        return this.cloudData;
    }
    setRawData(data) {
        this.rawData = data;
        this.setData(data);
        this.setCheckInTimeData();
        this.setDataWithValidImg();
        this.setBusinessPhotoMatch();
        this.setIdToIndex();
    }

    getData() {
        return this.data;
    }

    getRawData() {
        return this.rawData;
    }

    setCheckInTimeData() {
        this.checkinTime = {};
        this.data.forEach((restaurant) => {
            // console.log(restaurant);
            this.checkinTime[restaurant.business_id] = restaurant.checkin.time;
        });
        // console.log(this.checkinTime);
    }

    getCheckInTimeData() {
        // console.log(this.checkinTime);
        return this.checkinTime;
    }

    setSentimentData(data) {
        this.sentimentData = data[0];
    }

    getSentimentData() {
        return this.sentimentData;
    }

    setDataWithValidImg() {
        this.dataWithValidImg = [];
        this.data.forEach((restaurant) => {
            if (restaurant.images.length > 0) {
                this.dataWithValidImg.push(restaurant);
            }
        });
        this.data = this.dataWithValidImg;
    }

    getDataWithValidImg() {
        return this.dataWithValidImg;
    }

    setBusinessPhotoMatch() {
        this.businessID2Img = {};
        this.data.forEach((restaurant) => {
            this.businessID2Img[restaurant.business_id] = restaurant.images;
        });
    }

    getImgArrayByBusinessID(businessID) {
        return this.businessID2Img[businessID];
    }

    setIdToIndex() {
        let count = 0;
        this.id2index = {};
        this.data.forEach((restaurant) => {
            this.id2index[restaurant.business_id] = count;
            count += 1;
        });
    }
}

const DataService = new Service();
export default DataService;
