<template>
    <div id="checkin-vis-container" ref="checkincanvas">
    </div>
</template>

<script>
import PipeService from '../../services/pipe-service';
import DataService from '../../services/data-service';

export default {
    name: 'CheckInVis',
    mounted() {
        PipeService.$on(PipeService.DATA_CHANGE, () => {
            const data = DataService.getCheckInTimeData();
            this.data = data;
            this.testData();
        });
    },
    data() {
        return {
            data: null,
        };
    },
    methods: {
        testData() {
            console.log(this.data);
        },
    },
};
</script>