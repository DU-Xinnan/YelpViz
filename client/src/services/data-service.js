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

    genSubspaceData(attrMap) {
        const subspaceData = {};
        subspaceData.attributeTable = this.data.attributeTable.filter(
            attribute => attrMap.has(attribute.name)
        );
        subspaceData.pointTable = this.data.pointTable.map(point =>
            Object.keys(point)
            .filter(key => attrMap.has(key))
            .reduce((obj, key) => {
                const object = obj;
                object[key] = point[key];
                return obj;
            }, {})
        );
        return subspaceData;
    }
}

const DataService = new Service();
export default DataService;
