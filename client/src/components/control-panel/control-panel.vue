<template>
    <div class="col-2" id="control-panel" style="background-color: #343332;">
        <h1 style="margin-top: 5%">Control Panel</h1>
       <div class='control-column'>
            <data-loader></data-loader>
       </div>
       <div>
           <restaurant-list v-for="(restaurant, index) in this.data" :restaurant="restaurant" :index="index"></restaurant-list>
       </div>
    </div>
</template>

<script>
import './control-panel.styl';
import DataLoader from './data-loader';
import RestaurantList from './restaurant-list';
import DataService from '../../services/data-service';
import PipeService from '../../services/pipe-service';

export default {
    name: 'ControlPanel',
    mounted() {
        PipeService.$on(PipeService.DATA_CHANGE, (newValue) => {
            this.data = DataService.getData();
            this.city = newValue;
        });
    },
    data() {
        return {
            data: undefined,
        };
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