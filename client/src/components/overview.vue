<template>
    <div id="overview">
        <div class="row" style="height: 100%; width: 100%">
            <div id="map-left" class="col-6">
                <gmap-map :center="Pittsburghenter" :zoom="12" class = "map"></gmap-map>
            </div>
            <div id="map-right" class="col-6">
                <gmap-map :center="MadisonCenter" :zoom="11" class = "map"></gmap-map>
            </div>
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
            Pittsburghenter: { lat: 40.440624, lng: -79.995888 },
            MadisonCenter: { lat: 43.087806, lng: -89.430121 },
        };
    },
    methods: {
    },
};
</script>
<style lang='stylus' scoped>
#overview
    width: 100%
    border-style: solid;
    border-width: 1px;
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
