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
        PipeService.$on(PipeService.MOUSEENTER_DIV, (id) => {
            this.initializaRadar();
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
                    .attr('fill', 'gray');

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

            const colorScale = d3.scaleLinear()
                .domain([0, 1, 2, 3, 4, 5, 6])
                .range(['#8dd3c7', '#ffffb3', '#bebada', '#fb8072', '#80b1d3', '#fdb462', '#b3de69']);

            for (let i = 0; i <= 6; i += 1) {
                svg.append('text')
                    .attr('font-size', '10px')
                    .attr('fill', () => colorScale(i))
                    .attr('transform', `translate(${(this.canvasWidth / 2) - (HORIZONTAL_MARGIN * 8)},
                        ${(this.canvasHeight / 5) + (VERTICAL_MARGIN * i)})`)
                    // .attr('x', this.canvasWidth - HORIZONTAL_MARGIN)
                    // .attr('y', this.canvasHeight - (VERTICAL_MARGIN * i))
                    .text(() => {
                        switch (i) {
                            case 1:
                                return 'Mon';
                            case 2:
                                return 'Tue';
                            case 3:
                                return 'Wed';
                            case 4:
                                return 'Thu';
                            case 5:
                                return 'Fri';
                            case 6:
                                return 'Sat';
                            default:
                                break;
                        }
                        return 'Sun';
                    });
            }

            let maxFlow = 0;
            if (this.checkinTime[id] !== undefined) {
                Object.keys(this.checkinTime[id]).forEach((weekday) => {
                    if (this.checkinTime[id][weekday].length !== 0) {
                        this.checkinTime[id][weekday].forEach((hourflow) => {
                            Object.keys(hourflow).forEach((key) => {
                                maxFlow = hourflow[key] > maxFlow ? hourflow[key] : maxFlow;
                                this.radar[key] += hourflow[key];
                            });
                        });
                    }
                });
            }

            let maxhourFlow = 0;
            Object.keys(this.radar).forEach((key) => {
                maxhourFlow = this.radar[key] > maxhourFlow ? this.radar[key] : maxhourFlow;
            });

            console.log(this.checkinTime[id]);
            console.log(maxFlow);

            this.draw_checkinflow(this.checkinTime[id], maxFlow);
            this.draw_radar(this.radar, maxhourFlow);
        });
    },
    data() {
        return {
            data: null,
            maxFlow: null,
            radar: {
                0: 0,
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
                6: 0,
                7: 0,
                8: 0,
                9: 0,
                10: 0,
                11: 0,
                12: 0,
                13: 0,
                14: 0,
                15: 0,
                16: 0,
                17: 0,
                18: 0,
                19: 0,
                20: 0,
                21: 0,
                22: 0,
                23: 0,
            },
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
                            this.radar[hour] += flow;
                            if (debug) console.log(checkinTime[businessid]);
                            checkinTime[businessid][weekday].push(hourFlow);
                            if (debug) console.log('checkinTime');
                        }
                    });
                }
            });
            return checkinTime;
        },
        initializaRadar() {
            Object.keys(this.radar).forEach((key) => {
                this.radar[key] = 0;
            });
        },
        draw_radar(data, maxhourFlow) {
            const svg = d3.select(this.$refs.checkincanvas).select('svg').select('#container');
            const flowScale = d3.scaleLinear()
                .domain([0, maxhourFlow])
                .range([1, this.config.clockRadius - 10]);
            const zeroflow = flowScale(data[0]);
            const xZero = (zeroflow) * Math.cos((0 *
                                ((360 / 24) * (Math.PI / 180))) - (Math.PI / 2));
            const yZero = (zeroflow) * Math.sin((0 *
                                ((360 / 24) * (Math.PI / 180))) - (Math.PI / 2));
            let previousX = xZero;
            let previousY = yZero;
            Object.keys(data).forEach((key) => {
                if (key !== '0') {
                    const flow = flowScale(data[key]);
                    const xCoor = (flow) * Math.cos((parseInt(key, 10) *
                            ((360 / 24) * (Math.PI / 180))) - (Math.PI / 2));
                    const yCoor = (flow) * Math.sin((parseInt(key, 10) *
                            ((360 / 24) * (Math.PI / 180))) - (Math.PI / 2));
                    svg.append('line')
                        .attr('x1', xCoor)
                        .attr('y1', yCoor)
                        .attr('x2', previousX)
                        .attr('y2', previousY)
                        .attr('stroke-width', 1)
                        .attr('stroke-opacity', 1)
                        .attr('stroke', 'orange');
                    previousX = xCoor;
                    previousY = yCoor;
                }
            });
            svg.append('line')
                .attr('x1', xZero)
                .attr('y1', yZero)
                .attr('x2', previousX)
                .attr('y2', previousY)
                .attr('stroke-width', 1)
                .attr('stroke-opacity', 1)
                .attr('stroke', 'orange');
        },
        draw_checkinflow(restCheckinData, maxFlow) {
            const flowScale = d3.scaleLinear()
                .domain([0, maxFlow])
                .range([1, this.config.clockRadius - 10]);
            const svg = d3.select(this.$refs.checkincanvas).select('svg').select('#container');
            Object.keys(restCheckinData).forEach((weekday) => {
                if (restCheckinData[weekday].length !== 0) {
                    restCheckinData[weekday].forEach((timeflow) => {
                        Object.keys(timeflow).forEach((key) => {
                            const flow = flowScale(timeflow[key]);
                            const xCoor = (flow) * Math.cos((parseInt(key, 10) *
                                ((360 / 24) * (Math.PI / 180))) - (Math.PI / 2));
                            const yCoor = (flow) * Math.sin((parseInt(key, 10) *
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

            this.initializaRadar();

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
                    .attr('fill', 'gray');

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

            const colorScale = d3.scaleLinear()
                .domain([0, 1, 2, 3, 4, 5, 6])
                .range(['#8dd3c7', '#ffffb3', '#bebada', '#fb8072', '#80b1d3', '#fdb462', '#b3de69']);

            for (let i = 0; i <= 6; i += 1) {
                svg.append('text')
                    .attr('font-size', '15px')
                    .attr('fill', () => colorScale(i))
                    .attr('transform', `translate(${(this.canvasWidth / 2) - (HORIZONTAL_MARGIN * 8)},
                        ${(this.canvasHeight / 5) + (VERTICAL_MARGIN * i)})`)
                    // .attr('x', this.canvasWidth - HORIZONTAL_MARGIN)
                    // .attr('y', this.canvasHeight - (VERTICAL_MARGIN * i))
                    .text(() => {
                        switch (i) {
                            case 1:
                                return 'Mon';
                            case 2:
                                return 'Tue';
                            case 3:
                                return 'Wed';
                            case 4:
                                return 'Thu';
                            case 5:
                                return 'Fri';
                            case 6:
                                return 'Sat';
                            default:
                                break;
                        }
                        return 'Sun';
                    });
            }

            let maxhourFlow = 0;
            Object.keys(this.radar).forEach((key) => {
                maxhourFlow = this.radar[key] > maxhourFlow ? this.radar[key] : maxhourFlow;
            });

            Object.keys(checkinTime).forEach((key) => {
                this.draw_checkinflow(checkinTime[key], this.maxFlow);
            });

            this.draw_radar(this.radar, maxhourFlow);
        },
    },
};
</script>