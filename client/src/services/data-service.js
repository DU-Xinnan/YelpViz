let instance = null;

class Service {
    constructor() {
        if (!instance) {
            instance = this;
        }
        this.data = undefined;
        return instance;
    }

    setData(data) {
        this.data = data;
    }

    getData() {
        return this.data;
    }

}

const DataService = new Service();
export default DataService;
