<template>
    <div id="sentiment-vis-container" ref="sentimentcanvas">
    </div>
</template>

<script>
import * as d3 from 'd3';
// import * as _ from 'underscore';
import d3Tip from 'd3-tip';
import * as echarts from 'echarts';
import PipeService from '../../services/pipe-service';
import DataService from '../../services/data-service';

d3.tip = d3Tip;

export default {
    name: 'SentimentVis',
    mounted() {
        PipeService.$on(PipeService.DATA_CHANGE, () => {
            const data = DataService.getSentimentData();
            this.data = data;
            this.drawCitySentiment();
        });
        PipeService.$on(PipeService.MOUSEENTER_DIV, (id) => {
            this.drawRestaurantSentiment(this.data[id]);
        });
    },
    data() {
        return {
            data: null,
        };
    },
    methods: {
        sumSentiment() {
            // initalization
            const sumSentiment = {};
            sumSentiment.Jan = [0, 0, 0, 0];
            sumSentiment.Feb = [0, 0, 0, 0];
            sumSentiment.Mar = [0, 0, 0, 0];
            sumSentiment.Apr = [0, 0, 0, 0];
            sumSentiment.May = [0, 0, 0, 0];
            sumSentiment.Jun = [0, 0, 0, 0];
            sumSentiment.Jul = [0, 0, 0, 0];
            sumSentiment.Aug = [0, 0, 0, 0];
            sumSentiment.Sep = [0, 0, 0, 0];
            sumSentiment.Oct = [0, 0, 0, 0];
            sumSentiment.Nov = [0, 0, 0, 0];
            sumSentiment.Dec = [0, 0, 0, 0];

            // loop to sum the sentiment count
            Object.keys(this.data).forEach((businessId) => {
                Object.keys(this.data[businessId]).forEach((month) => {
                    switch (month) {
                        case '01':
                            sumSentiment.Jan[0] += this.data[businessId][month][0];
                            sumSentiment.Jan[1] += this.data[businessId][month][1];
                            sumSentiment.Jan[2] += this.data[businessId][month][2];
                            sumSentiment.Jan[3] += this.data[businessId][month][0] +
                            (this.data[businessId][month][1] + this.data[businessId][month][2]);
                            break;
                        case '02':
                            sumSentiment.Feb[0] += this.data[businessId][month][0];
                            sumSentiment.Feb[1] += this.data[businessId][month][1];
                            sumSentiment.Feb[2] += this.data[businessId][month][2];
                            sumSentiment.Feb[3] += this.data[businessId][month][0] +
                            (this.data[businessId][month][1] + this.data[businessId][month][2]);
                            break;
                        case '03':
                            sumSentiment.Mar[0] += this.data[businessId][month][0];
                            sumSentiment.Mar[1] += this.data[businessId][month][1];
                            sumSentiment.Mar[2] += this.data[businessId][month][2];
                            sumSentiment.Mar[3] += this.data[businessId][month][0] +
                            (this.data[businessId][month][1] + this.data[businessId][month][2]);
                            break;
                        case '04':
                            sumSentiment.Apr[0] += this.data[businessId][month][0];
                            sumSentiment.Apr[1] += this.data[businessId][month][1];
                            sumSentiment.Apr[2] += this.data[businessId][month][2];
                            sumSentiment.Apr[3] += this.data[businessId][month][0] +
                            (this.data[businessId][month][1] + this.data[businessId][month][2]);
                            break;
                        case '05':
                            sumSentiment.May[0] += this.data[businessId][month][0];
                            sumSentiment.May[1] += this.data[businessId][month][1];
                            sumSentiment.May[2] += this.data[businessId][month][2];
                            sumSentiment.May[3] += this.data[businessId][month][0] +
                            (this.data[businessId][month][1] + this.data[businessId][month][2]);
                            break;
                        case '06':
                            sumSentiment.Jun[0] += this.data[businessId][month][0];
                            sumSentiment.Jun[1] += this.data[businessId][month][1];
                            sumSentiment.Jun[2] += this.data[businessId][month][2];
                            sumSentiment.Jun[3] += this.data[businessId][month][0] +
                            (this.data[businessId][month][1] + this.data[businessId][month][2]);
                            break;
                        case '07':
                            sumSentiment.Jul[0] += this.data[businessId][month][0];
                            sumSentiment.Jul[1] += this.data[businessId][month][1];
                            sumSentiment.Jul[2] += this.data[businessId][month][2];
                            sumSentiment.Jul[3] += this.data[businessId][month][0] +
                            (this.data[businessId][month][1] + this.data[businessId][month][2]);
                            break;
                        case '08':
                            sumSentiment.Aug[0] += this.data[businessId][month][0];
                            sumSentiment.Aug[1] += this.data[businessId][month][1];
                            sumSentiment.Aug[2] += this.data[businessId][month][2];
                            sumSentiment.Aug[3] += this.data[businessId][month][0] +
                            (this.data[businessId][month][1] + this.data[businessId][month][2]);
                            break;
                        case '09':
                            sumSentiment.Sep[0] += this.data[businessId][month][0];
                            sumSentiment.Sep[1] += this.data[businessId][month][1];
                            sumSentiment.Sep[2] += this.data[businessId][month][2];
                            sumSentiment.Sep[3] += this.data[businessId][month][0] +
                            (this.data[businessId][month][1] + this.data[businessId][month][2]);
                            break;
                        case '10':
                            sumSentiment.Oct[0] += this.data[businessId][month][0];
                            sumSentiment.Oct[1] += this.data[businessId][month][1];
                            sumSentiment.Oct[2] += this.data[businessId][month][2];
                            sumSentiment.Oct[3] += this.data[businessId][month][0] +
                            (this.data[businessId][month][1] + this.data[businessId][month][2]);
                            break;
                        case '11':
                            sumSentiment.Nov[0] += this.data[businessId][month][0];
                            sumSentiment.Nov[1] += this.data[businessId][month][1];
                            sumSentiment.Nov[2] += this.data[businessId][month][2];
                            sumSentiment.Nov[3] += this.data[businessId][month][0] +
                            (this.data[businessId][month][1] + this.data[businessId][month][2]);
                            break;
                        case '12':
                            sumSentiment.Dec[0] += this.data[businessId][month][0];
                            sumSentiment.Dec[1] += this.data[businessId][month][1];
                            sumSentiment.Dec[2] += this.data[businessId][month][2];
                            sumSentiment.Dec[3] += this.data[businessId][month][0] +
                            (this.data[businessId][month][1] + this.data[businessId][month][2]);
                            break;
                        default:
                            break;
                    }
                });
            });

            // return the actual sentiment count
            return sumSentiment;
        },
        drawRestaurantSentiment(rsSentiment) {
            // initalization
            const sumSentiment = {};
            sumSentiment.Jan = [0, 0, 0, 0];
            sumSentiment.Feb = [0, 0, 0, 0];
            sumSentiment.Mar = [0, 0, 0, 0];
            sumSentiment.Apr = [0, 0, 0, 0];
            sumSentiment.May = [0, 0, 0, 0];
            sumSentiment.Jun = [0, 0, 0, 0];
            sumSentiment.Jul = [0, 0, 0, 0];
            sumSentiment.Aug = [0, 0, 0, 0];
            sumSentiment.Sep = [0, 0, 0, 0];
            sumSentiment.Oct = [0, 0, 0, 0];
            sumSentiment.Nov = [0, 0, 0, 0];
            sumSentiment.Dec = [0, 0, 0, 0];

            // loop to sum the sentiment count
            Object.keys(rsSentiment).forEach((month) => {
                switch (month) {
                    case '01':
                        sumSentiment.Jan[0] += rsSentiment[month][0];
                        sumSentiment.Jan[1] += rsSentiment[month][1];
                        sumSentiment.Jan[2] += rsSentiment[month][2];
                        sumSentiment.Jan[3] += rsSentiment[month][0] +
                        (rsSentiment[month][1] + rsSentiment[month][2]);
                        break;
                    case '02':
                        sumSentiment.Feb[0] += rsSentiment[month][0];
                        sumSentiment.Feb[1] += rsSentiment[month][1];
                        sumSentiment.Feb[2] += rsSentiment[month][2];
                        sumSentiment.Feb[3] += rsSentiment[month][0] +
                        (rsSentiment[month][1] + rsSentiment[month][2]);
                        break;
                    case '03':
                        sumSentiment.Mar[0] += rsSentiment[month][0];
                        sumSentiment.Mar[1] += rsSentiment[month][1];
                        sumSentiment.Mar[2] += rsSentiment[month][2];
                        sumSentiment.Mar[3] += rsSentiment[month][0] +
                        (rsSentiment[month][1] + rsSentiment[month][2]);
                        break;
                    case '04':
                        sumSentiment.Apr[0] += rsSentiment[month][0];
                        sumSentiment.Apr[1] += rsSentiment[month][1];
                        sumSentiment.Apr[2] += rsSentiment[month][2];
                        sumSentiment.Apr[3] += rsSentiment[month][0] +
                        (rsSentiment[month][1] + rsSentiment[month][2]);
                        break;
                    case '05':
                        sumSentiment.May[0] += rsSentiment[month][0];
                        sumSentiment.May[1] += rsSentiment[month][1];
                        sumSentiment.May[2] += rsSentiment[month][2];
                        sumSentiment.May[3] += rsSentiment[month][0] +
                        (rsSentiment[month][1] + rsSentiment[month][2]);
                        break;
                    case '06':
                        sumSentiment.Jun[0] += rsSentiment[month][0];
                        sumSentiment.Jun[1] += rsSentiment[month][1];
                        sumSentiment.Jun[2] += rsSentiment[month][2];
                        sumSentiment.Jun[3] += rsSentiment[month][0] +
                        (rsSentiment[month][1] + rsSentiment[month][2]);
                        break;
                    case '07':
                        sumSentiment.Jul[0] += rsSentiment[month][0];
                        sumSentiment.Jul[1] += rsSentiment[month][1];
                        sumSentiment.Jul[2] += rsSentiment[month][2];
                        sumSentiment.Jul[3] += rsSentiment[month][0] +
                        (rsSentiment[month][1] + rsSentiment[month][2]);
                        break;
                    case '08':
                        sumSentiment.Aug[0] += rsSentiment[month][0];
                        sumSentiment.Aug[1] += rsSentiment[month][1];
                        sumSentiment.Aug[2] += rsSentiment[month][2];
                        sumSentiment.Aug[3] += rsSentiment[month][0] +
                        (rsSentiment[1] + rsSentiment[month][2]);
                        break;
                    case '09':
                        sumSentiment.Sep[0] += rsSentiment[month][0];
                        sumSentiment.Sep[1] += rsSentiment[month][1];
                        sumSentiment.Sep[2] += rsSentiment[month][2];
                        sumSentiment.Sep[3] += rsSentiment[month][0] +
                        (rsSentiment[month][1] + rsSentiment[month][2]);
                        break;
                    case '10':
                        sumSentiment.Oct[0] += rsSentiment[month][0];
                        sumSentiment.Oct[1] += rsSentiment[month][1];
                        sumSentiment.Oct[2] += rsSentiment[month][2];
                        sumSentiment.Oct[3] += rsSentiment[month][0] +
                        (rsSentiment[month][1] + rsSentiment[month][2]);
                        break;
                    case '11':
                        sumSentiment.Nov[0] += rsSentiment[month][0];
                        sumSentiment.Nov[1] += rsSentiment[month][1];
                        sumSentiment.Nov[2] += rsSentiment[month][2];
                        sumSentiment.Nov[3] += rsSentiment[month][0] +
                        (rsSentiment[month][1] + rsSentiment[month][2]);
                        break;
                    case '12':
                        sumSentiment.Dec[0] += rsSentiment[month][0];
                        sumSentiment.Dec[1] += rsSentiment[month][1];
                        sumSentiment.Dec[2] += rsSentiment[month][2];
                        sumSentiment.Dec[3] += rsSentiment[month][0] +
                        (rsSentiment[month][1] + rsSentiment[month][2]);
                        break;
                    default:
                        break;
                }
            });

            const positive = [];
            const negative = [];
            const neutral = [];
            Object.keys(sumSentiment).forEach((month) => {
                negative.push(sumSentiment[month][0]);
                neutral.push(sumSentiment[month][1]);
                positive.push(sumSentiment[month][2]);
            });

            this.drawSentiment(positive, negative, neutral);
        },
        drawCitySentiment() {
            const sentiTotal = this.sumSentiment();
            // const color = d3.scaleOrdinal(d3.schemeCategory20);
            const positive = [];
            const negative = [];
            const neutral = [];
            Object.keys(sentiTotal).forEach((month) => {
                negative.push(sentiTotal[month][0]);
                neutral.push(sentiTotal[month][1]);
                positive.push(sentiTotal[month][2]);
            });
            this.drawSentiment(positive, negative, neutral);
        },
        drawSentiment(positive, negative, neutral) {
            const chart = echarts.init(this.$refs.sentimentcanvas);
            chart.setOption({
                tooltip: {
                    trigger: 'axis',
                },
                legend: {
                    data: ['negative', 'neutral', 'positive'],
                },
                calculable: true,
                xAxis: [
                    {
                        type: 'category',
                        boundaryGap: false,
                        data: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
                    },
                ],
                yAxis: [
                    {
                        type: 'value',
                    },
                ],
                series: [
                    {
                        name: 'negative',
                        type: 'line',
                        stack: '总量',
                        itemStyle: { normal: { areaStyle: { type: 'default' } } },
                        data: negative,
                    },
                    {
                        name: 'neutral',
                        type: 'line',
                        stack: '总量',
                        itemStyle: { normal: { areaStyle: { type: 'default' } } },
                        data: neutral,
                    },
                    {
                        name: 'positive',
                        type: 'line',
                        stack: '总量',
                        itemStyle: { normal: { areaStyle: { type: 'default' } } },
                        data: positive,
                    },
                ],
            });
        },
    },
};
</script>