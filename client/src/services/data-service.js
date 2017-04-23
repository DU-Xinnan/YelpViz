let instance = null;

class Service {
    constructor() {
        if (!instance) {
            instance = this;
        }
        this.data = undefined;
        this.rawData = undefined;
        this.checkinTime = undefined;
        return instance;
    }

    setData(data) {
        this.data = data;
    }

    setRawData(data) {
        this.rawData = data;
        this.setData(data);
        this.setCheckInTimeData();
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

}

const DataService = new Service();
export default DataService;
