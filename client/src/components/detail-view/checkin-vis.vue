<template>
    <div id="checkin-vis-container" ref="checkincanvas">
    </div>
</template>

<script>
import PipeService from '../../services/pipe-service';
import DataService from '../../services/data-service';
import json

export default {
    name: 'CheckInVis',
    mounted() {
        PipeService.$on(PipeService.DATA_CHANGE, () => {
            const data = DataService.getCheckInTimeData();
            this.data = data;
            this.drawCheckInView()
        });
    },
    data() {
        return {
            data: null,
            config: {
                date: {
                    Sun: 0,
                    Mon: 1,
                    Tue: 2,
                    Wed: 3,
                    Thu: 4,
                    Fri: 5,
                    Sat: 6,
                },

            },
        };
    },
    methods: {
        // deepCopy(point) {
        //     return JSON.parse(JSON.stringify(point));
        // },
        testData() {
            console.log(this.data);
        },
        drawRestaurantView(restaurant) {
            WorkingRestaurant = JSON.parse(JSON.stringify(restaurant));
        },
        drawCheckInView() {

        },
    },
};
</script>