<template>
    <div id="overview">
        <div class="row" style="height: 100%; width: 100%">
        </div>
    </div>
</template>
<script>
import * as VueGoogleMaps from 'vue2-google-maps';
import Vue from 'vue';

Vue.use(VueGoogleMaps, {
    load: {
        key: 'AIzaSyAiwR5VKyNt1GM2oiIkCaejvRCUrkrl2FQ',
    },
});

export default {
    name: 'Overview',
    mounted() {
    },
    data() {
        return {
        };
    },
    methods: {
    },
};
</script>
<style lang='stylus' scoped>
#overview
    width: 100%
    border-bottom: 1px solid rgba(0, 0, 0, 0.4);
    border-right: 1px solid rgba(0, 0, 0, 0.4);
#map-left
    height: 100%
    display: inline-block
    padding-left: 50px
#map-right
    height: 100%
    display: inline-block
.map
    width: 100%
    height: 100%
</style>
