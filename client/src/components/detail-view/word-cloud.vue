<template>
    <div id='word-cloud' ref="cloud"></div>
</template>

<script>
    import 'echarts-wordcloud';
    import * as echarts from 'echarts';
    import DataService from '../../services/data-service';
    import PipeService from '../../services/pipe-service';

    export default {
        name: 'WordCloud',
        mounted() {
            PipeService.$on(PipeService.DATA_CHANGE, () => {
                const data = DataService.getCloudData();
                this.data = data;
                console.log(data);
                // console.log(`images: ${this.data}`);
                // TODO: map function to change data
                this.drawCloud(this.data);
            });

            PipeService.$on(PipeService.CLICK_POINT, (id) => {
                console.log('id', id);
                const words = this.getRestWordsById(id);
                console.log(words);
                this.drawCloud(words);
            });
        },
        data() {
            return {
                data: null,
            };
        },
        methods: {
            getRestWordsById(id) {
                const rests = DataService.getData();
                const restWords = {};
                const existingTags = new Set();
                const ret = [];
                const restaurant = rests.filter(rest => rest.business_id === id)[0];
                console.log(restaurant.images);
                restaurant.images.forEach((m) => {
                    m.lables.forEach((v) => {
                        if (existingTags.has(v.description)) {
                            restWords[v.description] += v.score;
                        } else {
                            existingTags.add(v.description);
                            restWords[v.description] = v.score;
                        }
                    });
                    // restWords.push(...m.lables);
                });
                Object.keys(restWords).forEach((k, v) => {
                    ret.push({ name: k, value: v });
                });
                return ret;
            },

            add_color(entry) {
                const tmp = entry;
                tmp.textStyle = {};
                tmp.textStyle.normal = {};
                tmp.textStyle.normal.color = `rgb(${Math.round(Math.random() * 160)}, ${Math.round(Math.random() * 160)}, ${Math.round(Math.random() * 160)})`;
            },

            drawCloud(words) {
                const chart = echarts.init(this.$refs.cloud);

                words.forEach(this.add_color);
                console.log(words);

                chart.setOption({
                    series: [
                        {
                            type: 'wordCloud',
                            shape: 'circle',
                            left: 'center',
                            top: 'center',
                            width: '70%',
                            height: '80%',
                            right: null,
                            bottom: null,
                            sizeRange: [12, 60],
                            rotationRange: [-90, 90],
                            rotationStep: 45,
                            gridSize: 8,
                            textStyle: {
                                normal: {
                                    fontFamily: 'sans-serif',
                                    fontWeight: 'bold',
                                    // Color can be a callback function or a color string
                                    color: `rgb(${Math.round(Math.random() * 160)}, ${Math.round(Math.random() * 160)}, ${Math.round(Math.random() * 160)})`,
                                },
                                emphasis: {
                                    shadowBlur: 10,
                                    shadowColor: '#333',
                                },
                            },
                            data: words,
                        }],
                });
            },
        },
    };
</script>