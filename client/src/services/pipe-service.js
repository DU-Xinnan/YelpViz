import Vue from 'vue';

const PipeService = new Vue({
    data: {
        // add event name here like this: SELECT_POINT: select_point
        // SELECT_POINT: select_point,
        CLICK_POINT: 'click_point',
    },
});

export default PipeService;
