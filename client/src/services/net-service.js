import axios from 'axios';

const devApiUrl = 'http://localhost:5000/api';
const GET_REQUEST = 'get';
const POST_REQUEST = 'post';

function request(url, params, type, callback) {
    let func;
    if (type === GET_REQUEST) {
        func = axios.get;
    } else if (type === POST_REQUEST) {
        func = axios.post;
    }

    func(url, params).then((response) => {
        if (response.status === 200) {
            callback(response);
        } else {
            console.error(response);
        }
    })
    .catch((error) => {
        console.error(error);
    });
}

function getDataList(callback) {
    const url = `${devApiUrl}/data_list`;
    request(url, {}, GET_REQUEST, callback);
}

function getData(name, callback) {
    const url = `${devApiUrl}/data/${name}`;
    const params = {};
    request(url, params, GET_REQUEST, callback);
}

export default {
    getDataList,
    getData,
};

