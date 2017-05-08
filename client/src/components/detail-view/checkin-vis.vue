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
        PipeService.$on(PipeService.MOUSEON_DIV, (id) => {
            const el = this.$refs.checkincanvas;
            const VERTICAL_MARGIN = 10;
            const HORIZONTAL_MARGIN = 10;
            const canvas = d3.select(el).select('svg');
            if (!canvas.empty()) {
                canvas.remove();
            }
            const svg = d3.select(el).append('svg')
                .attr('width', this.canvasWidth + (HORIZONTAL_MARGIN * 2))
                .attr('height', this.canvasHeight +
                    (VERTICAL_MARGIN * 2))
                .append('g')
                .attr('id', 'container')
                .attr('transform', `translate(${(this.canvasWidth +
                    (HORIZONTAL_MARGIN * 2)) / 2},
                    ${(this.canvasHeight +
                    (VERTICAL_MARGIN * 2)) / 2})`);

            const degree = 360 / 24;

            let startAngle = 0;

            for (let i = 0; i <= 23; i += 1) {
                const angle = (degree) * (Math.PI / 180);
                const arc = d3.arc()
                    .innerRadius(0)
                    .outerRadius(this.config.clockRadius)
                    .startAngle(startAngle)
                    .endAngle(startAngle + angle);
                svg.append('path')
                    .attr('d', arc)
                    .attr('stroke', 'gray')
                    .attr('stroke-width', '1')
                    .attr('stroke-opacity', '0.3')
                    .attr('fill', 'white');

                const xDot = (this.config.clockRadius) * Math.cos(startAngle - (Math.PI / 2));
                const yDot = (this.config.clockRadius) * Math.sin(startAngle - (Math.PI / 2));
                const xCoor = (this.config.clockRadius + 7) * Math.cos(startAngle - (Math.PI / 2));
                const yCoor = (this.config.clockRadius + 7) * Math.sin(startAngle - (Math.PI / 2));

                svg.append('circle')
                    .attr('r', this.config.dotRadius)
                    .attr('cx', xDot)
                    .attr('cy', yDot)
                    .attr('fill', 'steelblue');
                svg.append('text')
                    .attr('font-size', '10px')
                    .attr('fill', 'white')
                    .attr('x', xCoor)
                    .attr('y', yCoor)
                    .attr('transform', `translate(${-4},${2})`)
                    .text(`${i}`);
                startAngle += angle;
            }

            let maxFlow = 0;
            if (this.checkinTime[id] !== undefined) {
                Object.keys(this.checkinTime[id]).forEach((weekday) => {
                    if (this.checkinTime[id][weekday].length !== 0) {
                        this.checkinTime[id][weekday].forEach((hourflow) => {
                            Object.keys(hourflow).forEach((key) => {
                                maxFlow = hourflow[key] > maxFlow ? hourflow[key] : maxFlow;
                            });
                        });
                    }
                });
            }

            this.draw_checkinflow(this.checkinTime[id], maxFlow);
        });
    },
    data() {
        return {
            data: null,
            maxFlow: null,
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
                clockRadius: 80,
                dotRadius: 2,
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
        getWeekDayColor(weekday) {
            const colorScale = d3.scaleLinear()
                .domain([0, 1, 2, 3, 4, 5, 6])
                .range(['#8dd3c7', '#ffffb3', '#bebada', '#fb8072', '#80b1d3', '#fdb462', '#b3de69']);
            return colorScale(this.config.Date[weekday]);
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
        draw_checkinflow(restCheckinData, maxFlow) {
            const flowScale = d3.scaleLinear()
                .domain([1, maxFlow])
                .range([1, this.config.clockRadius]);
            const svg = d3.select(this.$refs.checkincanvas).select('svg').select('#container');
            Object.keys(restCheckinData).forEach((weekday) => {
                if (restCheckinData[weekday].length !== 0) {
                    restCheckinData[weekday].forEach((timeflow) => {
                        Object.keys(timeflow).forEach((key) => {
                            const flow = flowScale(timeflow[key]);
                            const xCoor = (flow) * Math.cos((key *
                                ((360 / 24) * (Math.PI / 180))) - (Math.PI / 2));
                            const yCoor = (flow) * Math.sin((key *
                                ((360 / 24) * (Math.PI / 180))) - (Math.PI / 2));
                            svg.append('circle')
                            .attr('r', this.config.dotRadius)
                            .attr('cx', xCoor)
                            .attr('cy', yCoor)
                            .attr('fill', () => this.getWeekDayColor(weekday));
                        });
                    });
                }
            });
        },
        drawCheckInView() {
            const VERTICAL_MARGIN = 10;
            const HORIZONTAL_MARGIN = 10;
            const el = this.$refs.checkincanvas;
            this.canvasWidth = document.querySelector('#checkin-vis-container').clientWidth - (HORIZONTAL_MARGIN * 2);
            this.canvasHeight = document.querySelector('#checkin-vis-container').clientHeight - (VERTICAL_MARGIN * 2);

            this.config.clockRadius = this.canvasHeight > this.canvasWidth ?
            (this.canvasWidth / 2) : (this.canvasHeight / 2);

            const canvas = d3.select(el).select('svg');
            if (!canvas.empty()) {
                canvas.remove();
            }

            const checkinTime = this.reStructureData();
            this.checkinTime = checkinTime;

            const svg = d3.select(el).append('svg')
                .attr('width', this.canvasWidth + (HORIZONTAL_MARGIN * 2))
                .attr('height', this.canvasHeight +
                    (VERTICAL_MARGIN * 2))
                .append('g')
                .attr('id', 'container')
                .attr('transform', `translate(${(this.canvasWidth +
                    (HORIZONTAL_MARGIN * 2)) / 2},
                    ${(this.canvasHeight +
                    (VERTICAL_MARGIN * 2)) / 2})`);

            const tip = d3.tip().attr('class', 'd3-tip').html((nd) => {
                if (nd.name !== undefined) {
                    const str = `<div class="d3-tip">name: ${nd.name}`;
                    return str;
                }
                return `<div class="d3-tip">id: ${nd.business_id}`;
            })
            .offset([-40, 0]);

            svg.call(tip);
            // const self = this;
            const degree = 360 / 24;
            const maxFlow = this.computeMaxFlow()[0];
            this.maxFlow = maxFlow;

            let startAngle = 0;

            for (let i = 0; i <= 23; i += 1) {
                const angle = (degree) * (Math.PI / 180);
                const arc = d3.arc()
                    .innerRadius(0)
                    .outerRadius(this.config.clockRadius)
                    .startAngle(startAngle)
                    .endAngle(startAngle + angle);
                svg.append('path')
                    .attr('d', arc)
                    .attr('stroke', 'gray')
                    .attr('stroke-width', '1')
                    .attr('stroke-opacity', '0.3')
                    .attr('fill', 'white');

                const xDot = (this.config.clockRadius) * Math.cos(startAngle - (Math.PI / 2));
                const yDot = (this.config.clockRadius) * Math.sin(startAngle - (Math.PI / 2));
                const xCoor = (this.config.clockRadius + 7) * Math.cos(startAngle - (Math.PI / 2));
                const yCoor = (this.config.clockRadius + 7) * Math.sin(startAngle - (Math.PI / 2));

                svg.append('circle')
                    .attr('r', this.config.dotRadius)
                    .attr('cx', xDot)
                    .attr('cy', yDot)
                    .attr('fill', 'steelblue');
                svg.append('text')
                    .attr('font-size', '10px')
                    .attr('fill', 'white')
                    .attr('x', xCoor)
                    .attr('y', yCoor)
                    .attr('transform', `translate(${-4},${2})`)
                    .text(`${i}`);
                startAngle += angle;
            }

            Object.keys(checkinTime).forEach((key) => {
                this.draw_checkinflow(checkinTime[key], this.maxFlow);
            });
        },
    },
};
</script>