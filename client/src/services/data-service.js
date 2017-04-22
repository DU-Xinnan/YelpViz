let instance = null;

class Service {
    constructor() {
        if (!instance) {
            instance = this;
        }
        this.data = undefined;
        this.rawData = undefined;
        return instance;
    }

    setData(data) {
        this.data = data;
    }

    setRawData(data) {
        this.rawData = data;
        this.setData(data);
    }

    getData() {
        return this.data;
    }

    getRawData() {
        return this.rawData;
    }

}

const DataService = new Service();
export default DataService;
