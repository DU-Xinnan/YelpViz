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
        return instance;
    }

    setData(data) {
        this.data = data;
    }

    setRawData(data) {
        this.rawData = data;
        this.setData(data);
        this.setCheckInTimeData();
        this.setDataWithValidImg();
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
        console.log(this.checkinTime);
        return this.checkinTime;
    }

    setDataWithValidImg() {
        this.dataWithValidImg = [];
        this.data.forEach((restaurant) => {
            if (restaurant.images.length > 0) {
                this.dataWithValidImg.push(restaurant);
            }
        });
    }

    getDataWithValidImg() {
        return this.dataWithValidImg;
    }

}

const DataService = new Service();
export default DataService;
