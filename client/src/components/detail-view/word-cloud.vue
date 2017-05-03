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
                this.onStart();
            });
        },
        data() {
            return {
                data: null,
            };
        },
        methods: {
            onStart() {
                const chart = echarts.init(this.$refs.cloud);

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
                            data: this.data,
                        }],
                });
            },
        },
    };
</script>