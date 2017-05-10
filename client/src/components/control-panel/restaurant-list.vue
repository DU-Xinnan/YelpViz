<template>
<div class="container" :id="`a${this.restaurant.business_id}a`" v-on:mouseover="mouseOverDiv" v-on:mouseout="mouseOutDiv" v-on:mouseenter="mouseEnterDiv">
  <div class="card" :style="{backgroundColor: getRestaurantColor(restaurant)}">
    <div class="row">
      <div class="col-md-4">
        <img :src="`http://localhost:8888/${this.restaurant.city}/${this.restaurant.images[0].image}`"   style="transform: translateY(10px)">
      </div>
      <div class="col-md-8">
        <div class="row res_row" style="transform: translateX(-10px)">
          <a :href="this.URL" target="#" style="text-decoration: none; color: black; font-weight: bold; font-size: 15px">{{`${this.index + 1}. ${this.restaurant.name}`}}</a>
        </div>
        <canvas width="200" height="60" style="transform: translateX(-5%) translateY(30%); margin-top:-30px; margin-bottom:-20px" v-tooltip.left-middle="tipContent"></canvas>
        <div class="row res_row">
          <div class="col-md-4" style="transform: translateY(38px) translateX(-20px);">
            <div class='star-ratings-sprite'><span :style="{'width': `${this.restaurant.stars * 20}%`}" class='star-ratings-sprite-rating'></span>
            </div>
          </div>
        </div>
        <div class="col-md-8" style="transform: translateX(70%) translateY(10px)">
          <p style="font-weight: bold">{{`${this.restaurant.images.length} imgs`}}</p>
        </div>
      </div>
      <div class="row res_row">
      </div>
    </div>
  </div>
</div>
</template>

<script>
import * as d3 from 'd3';
import PipeService from '../../services/pipe-service';
import DataService from '../../services/data-service';

export default {
    name: 'RestaurantList',
    mounted() {
        this.r(this.restaurant);
    },
    data() {
        return {
            URL: undefined,
            tip: undefined,
            tipContent: '',
            canvasWidth: 200,
            canvasHeight: 60,
            Gap: 2,
        };
    },
    props: {
        restaurant: Object,
        index: Number,
    },
    watch: {
        restaurant: function foo(newValue) {
            this.r(newValue);
        },
    },
    directives: {
    },
    methods: {
        r(restaurant) {
            // console.log('info', restaurant, this.index);
            this.URL = this.getResaurantUrl(restaurant.business_id);
            let tc = '';
            tc = '<div>';
            for (let i = 0; i < restaurant.images.length; i += 1) {
                if (i % 7 === 0 && i !== 0) {
                    tc += '<br />';
                }
                tc += `<img src='http://localhost:8888/${restaurant.city}/${restaurant.images[i].image}' style='width: 50px; height: 50px;'/>`;
            }
            tc += '</div>';
            this.tipContent = tc;
            // const canvasId = 'canvas'.concat(restaurant.business_id);
            const canvas = document.getElementsByTagName('canvas');
            // console.log('canvas', canvasId, canvas);
            this.drawMosaics(canvas[this.index], restaurant.images);
            // console.log('render');
        },
        getColor(number) {
            const colors = ['#67001f', '#b2182b', '#d6604d', '#f4a582', '#ffffff', '#92c5de', '#4393c3', '#2166ac', '#053061'];
            const domain = [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5];
            const colorScale = d3.scaleLinear()
                // .domain([-0.8, -0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8])
                .domain(domain)
                .range(colors);
            return colorScale(number - 0.5);
        },
        processName(name) {
            let result = name.toLowerCase().split(' ').filter(item => item !== ' ');
            result = result.join('-');
            result = result.replace('&', 'and').replace('\'', '').replace(',', '').replace('.', '');
            return result;
        },
        getResaurantUrl(id) {
            const index = DataService.id2index[id];
            const restaurant = DataService.data[index];
            const name = this.processName(restaurant.name);
            const cityName = this.processName(restaurant.city);
            const URL = `https://en.yelp.com.hk/biz_photos/${[name, cityName].join('-')}?tab=food`;
            return URL;
        },
        mouseOverDiv() {
            PipeService.$emit(PipeService.MOUSEON_DIV, this.restaurant.business_id);
        },
        mouseOutDiv() {
            PipeService.$emit(PipeService.MOUSEOUT_DIV, this.restaurant.business_id);
        },
        mouseEnterDiv() {
            PipeService.$emit(PipeService.MOUSEENTER_DIV, this.restaurant.business_id);
        },
        getRestaurantColor() {
            let index = 0;
            this.restaurant.images.forEach((img) => {
                index += img.health_index;
            });
            index /= this.restaurant.images.length;
            return this.getColor(index);
        },
        drawMosaics(canvasElement, images) {
            const imageColors = [];
            images.sort(this.compare);
            images.map((img) => {
                console.log('sort health ind', img.health_index);
                return 0;
            });
            // images.map((img) => {
            //     imageColors.push(this.getColor(img.health_index));
            //     return 0;
            // });
            for (let i = 0; i < images.length; i += 1) {
                imageColors.push(this.getColor(images[i].health_index));
            }
            const ctx = canvasElement.getContext('2d');
            ctx.clearRect(0, 0, 200, 60);
            const rectWidth = (200 / images.length) - 2;
            for (let col = 0; col < images.length; col += 1) {
                ctx.beginPath();
                ctx.fillStyle = imageColors[col];
                ctx.rect(col * (rectWidth + 2),
                    0, rectWidth, 60);
                ctx.fill();
            }
        },
        compare(a, b) {
            if (a.health_index < b.health_index) {
                return 1;
            }
            if (a.health_index > b.health_index) {
                return -1;
            }
            return 0;
        },
    },
};
</script>
<style lang="stylus" scoped>
img
    height: 64px
    width: 64px
.container
    width: 90%
    margin-top: 10px
    height: 96
.res_row
    height: 32px
p
    text-align: center
@import url('http://fonts.googleapis.com/css?family=Open+Sans:400,600,700');
.star-ratings-css
    unicode-bidi bidi-override
    color #c5c5c5
    font-size 25px
    height 25px
    width 100px
    margin 0 auto
    position relative
    padding 0
    text-shadow 0px 1px 0 #a2a2a2

.star-ratings-css-top
    color #e7711b
    padding 0
    position absolute
    z-index 1
    display block
    top 0
    left 0
    overflow hidden

.star-ratings-css-bottom
    padding 0
    display block
    z-index 0

.star-ratings-sprite
    background url("https://s3-us-west-2.amazonaws.com/s.cdpn.io/2605/star-rating-sprite.png") repeat-x
    font-size 0
    height 21px
    line-height 0
    overflow hidden
    text-indent -999em
    width 110px
    margin 0 auto

.star-ratings-sprite-rating
    background url("https://s3-us-west-2.amazonaws.com/s.cdpn.io/2605/star-rating-sprite.png") repeat-x
    background-position 0 100%
    float left
    height 21px
    display block

body
    margin 50px
    text-align center
    font-family 'Open Sans', sans-serif
    background #f2fbff

em
    font-style italic

h1
    font-size 24px
    margin-bottom 25px
    font-weight bold
    text-transform uppercase

h2
    font-size 16px
    margin-bottom 15px
</style>