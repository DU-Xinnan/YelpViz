<template>
    <div id="checkin-vis-container" ref="checkincanvas">
    </div>
</template>

<script>
import * as d3 from 'd3';
import * as _ from 'underscore';
import d3Tip from 'd3-tip';
import PipeService from '../../services/pipe-service';
import DataService from '../../services/data-service';

d3.tip = d3Tip;

export default {
    name: 'CheckInVis',
    mounted() {
        PipeService.$on(PipeService.DATA_CHANGE, () => {
            const data = DataService.getCheckInTimeData();
            this.data = data;
            this.drawCheckInView();
        });
    },
    data() {
        return {
            data: null,
            config: {
                Date: {
                    Sun: 0,
                    Mon: 1,
                    Tue: 2,
                    Wed: 3,
                    Thu: 4,
                    Fri: 5,
                    Sat: 6,
                },
            },
        };
    },
    methods: {
        // deepCopy(point) {
        //     return JSON.parse(JSON.stringify(point));
        // },
        testData(data) {
            console.log(data);
        },
        computeMaxFlow() {
            let maxFlow = 0;
            // const reg = /(?<=:)[\w+.-]+/;
            Object.keys(this.data).forEach((businessid) => {
                const restTime = JSON.parse(JSON.stringify(this.data[businessid]));
                const restTimeflow = [];
                restTime.forEach((time) => {
                    restTimeflow.push(parseInt(time.match(/:(.*)/, '')[1], 10));
                });
                const restTimemax = _.max(restTimeflow);
                maxFlow = restTimemax > maxFlow ? restTimemax : maxFlow;
            });
            return maxFlow;
        },
        // // drawRestaurantView(restaurant) {
        // //     WorkingRestaurant = JSON.parse(JSON.stringify(restaurant));
        // },
        drawCheckInView() {
            const VERTICAL_MARGIN = 10;
            const HORIZONTAL_MARGIN = 10;
            const el = this.$refs.checkincanvas;
            this.canvasWidth = document.querySelector('#checkin-vis-container').clientWidth - (HORIZONTAL_MARGIN * 2);
            this.canvasHeight = document.querySelector('#checkin-vis-container').clientHeight - (VERTICAL_MARGIN * 2);

            const canvas = d3.select(el).select('svg');
            if (!canvas.empty()) {
                canvas.remove();
            }

            // const svg = d3.select(el).append('svg')
            //     .attr('width', this.canvasWidth + (HORIZONTAL_MARGIN * 2))
            //     .attr('height', this.canvasHeight +
            //         (VERTICAL_MARGIN * 2))
            //     .append('g')
            //     .attr('transform', `translate(${HORIZONTAL_MARGIN}, ${VERTICAL_MARGIN})`);

            // const tip = d3.tip().attr('class', 'd3-tip').html((nd) => {
            //     if (nd.name !== undefined) {
            //         str = `<div class="d3-tip">name: ${nd.name}`;
            //     return str;
            // })
            // .offset([-40, 0]);

            // svg.call(tip);
            // const self = this;
            // const degree = 360 / 24;

            const clockRadius = this.computeMaxFlow();
            console.log(clockRadius);
        },
    },
};
</script>