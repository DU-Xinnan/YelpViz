<template>
<div class="container" :id = "`a${this.restaurant.business_id}a`" >
    <div class="card">
        <div class="row">
            <div class="col-md-4">
                <img :src = "`http://localhost:8888/${this.city}/${this.restaurant.images[0].image}`" v-on:mouseover="mouseOverDiv" v-on:mouseout = "mouseOutDiv">
            </div>
            <div class="col-md-8">
                <div class="row res_row" style="transform: translateX(-10px)">
                    <a :href="this.URL" target="#" style="text-decoration: none; color: black; font-weight: bold; font-size: 15px">{{`${this.index + 1}. ${this.restaurant.name}`}}</a>
                </div>
                    <div class="row res_row">
                        <div class="col-md-4" style="transform: translateY(38px) translateX(-20px);">
                            <div class='star-ratings-sprite'><span
                            :style="{'width': `${this.stars}%`}"
                            class='star-ratings-sprite-rating'></span>
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
</div>
</template>

<script>
import * as d3 from 'd3';
import PipeService from '../../services/pipe-service';
import DataService from '../../services/data-service';

export default {
    name: 'RestaurantList',
    mounted() {
        const index = this.getAvgHealthIndex();
        const color = this.getColor(index);
        d3.select(`#a${this.restaurant.business_id}a`).select('.card').style('background-color', color);
        this.city = DataService.getCity();
        this.URL = this.getResaurantUrl(this.restaurant.business_id);
        // this.background = this.getColor(this.getAvgHealthIndex());
    },
    data() {
        return {
            background: undefined,
            city: undefined,
            URL: undefined,
            stars: this.restaurant.stars * 20,
        };
    },
    props: {
        restaurant: Object,
        index: Number,
    },
    watch: {
    },
    methods: {
        getAvgHealthIndex() {
            let index = 0;
            this.restaurant.images.forEach((img) => {
                index += img.health_index;
            });
            return index / this.restaurant.images.length;
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
            const cityName = this.processName(this.city);
            const URL = `https://en.yelp.com.hk/biz_photos/${[name, cityName].join('-')}?tab=food`;
            return URL;
        },
        mouseOverDiv() {
            PipeService.$emit(PipeService.MOUSEON_DIV, this.restaurant.business_id);
        },
        mouseOutDiv() {
            PipeService.$emit(PipeService.MOUSEOUT_DIV, this.restaurant.business_id);
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