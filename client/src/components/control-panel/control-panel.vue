<template>
    <div class="col-2" id="control-panel" style="background-color: #343332;">
        <h1 style="margin-top: 5%">Control Panel</h1>
       <div class='control-column'>
            <data-loader></data-loader>
       </div>
       <div v-if="this.data.length > 0">
           <ul class="pagination justify-content-center">
                <li class="page-item">
                <a class="page-link" href="#" @click="nextp($event)">Previous</a>
                </li>
                
                <li v-for="item in this.list" :class="['page-item', {'active': isActive(item)}]"><a class="page-link" href="#" @click="next($event)">{{item}}</a></li>

                <li class="page-item">
                <a class="page-link" href="#" @click="next1($event)">Next</a>
                </li>
            </ul>
       </div>
       <div v-if="this.data.length > 0">
            <restaurant-list  v-for="(restaurant, index) in this.data[currentPage].restaurants" :restaurant.sync="restaurant" :index.sync="index" keep-alive></restaurant-list>
       </div>
    </div>
</template>

<script>
// <restaurant-list v-for="(restaurant, index) in this.data[currentPage]
// .restaurants" :restaurant="restaurant" :index="index"></restaurant-list>
import './control-panel.styl';
import DataLoader from './data-loader';
import RestaurantList from './restaurant-list';
import DataService from '../../services/data-service';
import PipeService from '../../services/pipe-service';

export default {
    name: 'ControlPanel',
    mounted() {
        PipeService.$on(PipeService.DATA_CHANGE, (newValue) => {
            const rawData = DataService.getData();
            let groupNum = 0;
            let groupTemp = [];
            this.data = [];
            this.currentPage = 0;
            this.totalPage = 0;
            this.city = newValue;
            this.totalPage = Math.floor(rawData.length / 8);
            rawData.map((restaurant, index) => {
                groupTemp.push(restaurant);
                if (index % 8 === 7) {
                    this.data.push({
                        group_n: groupNum,
                        restaurants: groupTemp,
                    });
                    groupTemp = [];
                    groupNum += 1;
                }
                return 0;
            });
            // console.log('data', this.data);
        });
    },
    data() {
        return {
            data: [],
            currentPage: 0,
            totalPage: 0,
        };
    },
    methods: {
        div() {
            return ('<h>hello world</h>');
        },
        next(event) {
            event.preventDefault();
            const cPage = event.target.innerHTML;
            if (cPage === '...') return;
            // console.log('page ', cPage);
            this.currentPage = cPage - 1;
        },
        next1(event) {
            event.preventDefault();
            if (this.currentPage + 1 === this.totalPage) return;
            this.currentPage += 1;
        },
        nextp(event) {
            event.preventDefault();
            if (this.currentPage === 0) return;
            this.currentPage -= 1;
        },
        isActive(item) {
            return item === this.currentPage + 1;
        },
    },
    computed: {
        list() {
            let list = [];
            if (this.currentPage < 3) {
                list = [1, 2, 3, 4, '...'];
            } else if (this.currentPage > this.totalPage - 2) {
                list = ['...', this.totalPage - 3, this.totalPage - 2, this.totalPage - 1, this.totalPage];
            } else {
                list = ['...', this.currentPage, this.currentPage + 1, this.currentPage + 2, '...'];
            }
            return list;
        },
    },
    components: {
        DataLoader,
        RestaurantList,
    },
    props: {
        setting: Object,
    },
};
</script>

<style lang='stylus' scoped>
// .pagination li.active span
//     background: purple
//     color: #000 !important
//     padding-left: 10px
</style>