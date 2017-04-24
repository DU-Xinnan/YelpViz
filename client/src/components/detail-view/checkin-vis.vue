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
            // the first index is maxflow in one day in all restaurants
            // the second index if the max total flow in all days in all restaurant
            let maxFlow = 0;
            let maxtotalFlow = 0;
            // const reg = /(?<=:)[\w+.-]+/;
            Object.keys(this.data).forEach((businessid) => {
                const restTime = [];
                if (this.data[businessid] !== undefined) {
                    this.data[businessid].forEach((time) => {
                        restTime.push(JSON.parse(JSON.stringify(time)));
                    });
                    const restTimeflow = [];
                    restTime.forEach((time) => {
                        restTimeflow.push(parseInt(time.match(/:(.*)/, '')[1], 10));
                    });
                    const restTimemax = _.max(restTimeflow);
                    const restTimeTotalmax = _.reduce(restTimeflow, (memo, num) => memo + num, 0);
                    maxFlow = restTimemax > maxFlow ? restTimemax : maxFlow;
                    maxtotalFlow = restTimeTotalmax > maxtotalFlow ?
                    restTimeTotalmax : maxtotalFlow;
                }
            });
            return [maxFlow, maxtotalFlow];
        },
        // computeRestaurantFlow(timeArr) {
        //     // given a resaurant, compute the total flow
        // },
        // computeRestaurantWeekdayFlow(timeArr) {
        //     // given a time array of a restaurant, return its own weekday flow

        // },
        // // drawRestaurantView(restaurant) {
        // //     WorkingRestaurant = JSON.parse(JSON.stringify(restaurant));
        // },
        initCheckinTime() {
            const timedict = {};
            timedict.Sun = [];
            timedict.Mon = [];
            timedict.Tue = [];
            timedict.Wed = [];
            timedict.Thu = [];
            timedict.Fri = [];
            timedict.Sat = [];
            return timedict;
        },
        reStructureData() {
            const debug = false;
            const checkinTime = {};
            Object.keys(this.data).forEach((businessid) => {
                if (checkinTime[businessid] === undefined) {
                    checkinTime[businessid] = this.initCheckinTime();
                }
                if (this.data[businessid] !== undefined) {
                    this.data[businessid].forEach((time) => {
                        if (time !== undefined) {
                            if (debug) console.log(time);
                            const weekday = time.match(/(.*)-/, '')[1];
                            if (debug) console.log(weekday);
                            const flow = parseInt(time.match(/:(.*)/, '')[1], 10);
                            if (debug) console.log(flow);
                            const hour = parseInt(time.match(/-(.*):/, '')[1], 10);
                            if (debug) console.log(hour);
                            const hourFlow = {};
                            hourFlow[hour] = flow;
                            if (debug) console.log(checkinTime[businessid]);
                            checkinTime[businessid][weekday].push(hourFlow);
                            if (debug) console.log('checkinTime');
                        }
                    });
                }
            });
            return checkinTime;
        },
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
            const checkinTime = this.reStructureData();
            console.log(checkinTime);

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

            const maxFlow = this.computeMaxFlow()[0];
            // console.log(clockRadius);
            console.log(maxFlow);
            // const flowScale = d3.linearScale()
            const flowScale = d3.scaleLinear()
                .domain([1, maxFlow])
                .range([1, maxFlow]);
            console.log(flowScale);
        },
    },
};
</script>