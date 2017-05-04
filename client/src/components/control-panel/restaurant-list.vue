<template>
<div class="container" :id = "`a${this.restaurant.business_id}a`">
    <div class="card">
        <div class="row">
            <div class="col-md-4">
                <!--<img :src = "`../images/${this.city}/${this.restaurant.images[0].image}`">-->
            </div>
            <div class="col-md-8">
                <div class="row res_row">
                    <a :href="this.URL" target="#" style="text-decoration: none; color: black;">{{`${this.index + 1}. ${this.restaurant.name}`}}</a>
                </div>
                <div class="row res_row">
                    <div class="col-md-4 star">
                        <b>{{`${this.restaurant.stars}`}}</b>
                    </div>
                    <div class="col-md-8">
                        <p>{{`${this.restaurant.images.length} imgs`}}</p>
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
// import PipeService from '../../services/pipe-service';
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
.star
    background-color: grey
    border-radius: 5px
</style>