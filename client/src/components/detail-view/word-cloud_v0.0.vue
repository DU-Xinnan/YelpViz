<template>
    <div id='word-cloud'></div>
</template>

<script>
    import * as d3 from 'd3';
    import * as cloud from 'd3-v4-cloud';
    import DataService from '../../services/data-service';
    import PipeService from '../../services/pipe-service';

    export default {
        name: 'WordCloud',
        mounted() {
            PipeService.$on(PipeService.DATA_CHANGE, () => {
                const data = DataService.getDataWithValidImg();
                this.data = data;
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
                const layout = cloud.cloud()
                    .size([150, 150])
                    .words([{ text: 'Hello', size: 10 + (Math.random() * 90) },
                        { text: 'world', size: 10 + (Math.random() * 90) },
                        { text: 'normally', size: 10 + (Math.random() * 90) },
                        { text: 'you', size: 10 + (Math.random() * 90) },
                        { text: 'want', size: 10 + (Math.random() * 90) },
                        { text: 'more', size: 10 + (Math.random() * 90) },
                        { text: 'words', size: 10 + (Math.random() * 90) },
                        { text: 'than', size: 10 + (Math.random() * 90) },
                        { text: 'this', size: 10 + (Math.random() * 90) }]
                    )
                    .padding(0)
                    // .rotate(function() { return ~~(Math.random() * 2) * 90; })
                    .font('Impact')
                    .fontSize(d => d.size)
                    .on('end', this.drawCloud());
                layout.start();
            },
            drawCloud() {
                const words = [{ font: 'Impact', hasText: true, height: 190, padding: 0, rotate: 0, size: 95, style: 'normal', text: 'than', weight: 'normal', width: 256, x: -22, x0: -128, x1: 128, xoff: 352, y: -18, y0: -77, y1: 94, yoff: 0 }];
                const fill = d3.scaleOrdinal(d3.schemeCategory20);
                console.log('words: ');
                console.log(words);
                console.log(`normal size: ${10 + (Math.random() * 90)}`);
                d3.selectAll('#word-cloud').append('svg')
                    .attr('width', 150)
                    .attr('height', 150)
                    .append('g')
                    .attr('transform', 'translate(300, 300)')
                    .selectAll('text')
                    .data(words)
                    .enter()
                    .append('text')
                    .style('font-size', d => `${d.size}px`)
                    .style('font-family', 'Impact')
                    .style('fill', (d, i) => fill(i))
                    .attr('text-anchor', 'middle')
//                    .attr('transform', function(d) {
//                        return 'translate(' + [d.x, d.y] + ')rotate(' + d.rotate + ')';
//                    })
                    .text(d => d.text);
            },
        },
    };
</script>