<template>
    <div id="overview">
        <div class="row" style="height: 100%; width: 103%">
            <div id="map-area" class="col">
                <v-map :zoom="zoom" :center="center" keep-alive>
                    <v-tilelayer :url="url" :attribution="attribution" class="tilelayer"></v-tilelayer>
                    <v-marker v-for="marker in markers" :key="marker.businessID" :latLng="marker.latLng" :icon="icon" class="marker" businessID="marker.businessID" @l-click="mClickHandler(marker.businessID)"></v-marker>
                    <v-circle v-for="point in points" :key="point.businessID" :latLng="point.latLng" :radius=1 :stroke=false fillColor="#80FF66" class="point" @l-click="mClickHandler(point.businessID)"></v-circle>
                    <v-polygon :latLngs="polygon" color="#80FF66" class="polygons"></v-polygon>
                </v-map>
            </div>
        </div>
    </div>
</template>

<script>
    import L from 'leaflet';
    import Vue from 'vue';
    import Vue2Leaflet from 'vue2-leaflet';
    // import * as d3 from 'd3';
    import PipeService from '../services/pipe-service';
    import DataService from '../services/data-service';

    Vue.component('v-map', Vue2Leaflet.Map);
    Vue.component('v-tilelayer', Vue2Leaflet.TileLayer);
    Vue.component('v-marker', Vue2Leaflet.Marker);
    Vue.component('v-polygon', Vue2Leaflet.Polygon);
    Vue.component('v-circle', Vue2Leaflet.LCircle);

    const debug = false;

    export default {
        name: 'Overview',
        mounted() {
            // this.appendMarkers();
            // console.log('component overview', this);
            const map = this.$children[0].mapObject;
            // map.panTo([47.413420, -1.219482]);
            if (debug) console.log('this', this);
            this.$children[0].$children.map((child, i) => {
                if (i === 0 || child.$el.className !== 'marker') return 0;
                if (debug) console.log(`child ${i}`, child);
                const popContent = `<b>Marker: ${child.latLng.lat}, ${child.latLng.lng} </b>`;
                child.mapObject.bindPopup(popContent);
                return 0;
            });

            PipeService.$on(PipeService.DATA_CHANGE, () => {
                const tmp = DataService.getRawData();
                if (debug) {
                    console.log('data 2', tmp[1]);
                }
                map.panTo([tmp[0].latitude, tmp[0].longitude]);
                map.setZoom(11);
                const newMarkers = [];
                tmp.map((m) => {
                    newMarkers.push({
                        latLng: L.latLng(m.latitude, m.longitude),
                        businessID: m.business_id,
                    });
                    return 0;
                });
                this.points = newMarkers;
            });

            PipeService.$on(PipeService.CLICK_POINT, (id) => {
                console.log('id', id);
            });
        },
        data() {
            return {
                zoom: 13,
                center: [47.413220, -1.219482],
                url: 'http://{s}.tile.osm.org/{z}/{x}/{y}.png',
                attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
                markers: [{
                    latLng: L.latLng(47.423220, -1.209482),
                    businessID: 1,
                },
                {
                    latLng: L.latLng(47.415320, -1.229482),
                    businessID: 2,
                    id: 2,
                },
                {
                    latLng: L.latLng(47.414420, -1.229482),
                    businessID: 3,
                },
                {
                    latLng: L.latLng(47.410520, -1.219482),
                    businessID: 4,
                },
                {
                    latLng: L.latLng(47.427620, -1.219482),
                    businessID: 5,
                },
                {
                    latLng: L.latLng(47.428720, -1.219482),
                    businessID: 6,
                },
                ],
                icon: L.icon({
                    iconUrl: 'data:image/png;base64,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',
                    iconSize: [30, 40],
                    iconAnchor: [17, 39],
                }),
                polygon: [
                    /* L.latLng(41.8820869817772, -87.60068893432617),
                    L.latLng(41.8820869817772, -87.59571075439453),
                    L.latLng(41.87965863341244, -87.5925350189209),
                    L.latLng(41.877677544029005, -87.59579658508301),
                    L.latLng(41.877677544029005, -87.60051727294922),
                    L.latLng(41.87972253849906, -87.60334968566895),
                    */
                    L.latLng(47.423220, -1.209482),
                    L.latLng(47.429220, -1.209482),
                    L.latLng(47.429220, -1.219482),
                    L.latLng(47.423220, -1.219482),
                ],
                points: [],
            };
        },
        methods: {
            mClickHandler(id) {
                PipeService.$emit(PipeService.CLICK_POINT, id);
            },
            appendMarkers() {
                // const vmap = d3.select('#map');
                // vmap.selectAll('VMarker')
                //     .data(this.markers[0])
                //     .append('VMarker')
                //     .attr('latLng', d => d)
                //     .attr('icon', this.icon);
            },
        },
};
</script>

<style lang='stylus' scoped>
@import "~leaflet/dist/leaflet.css";
#overview
    width: 100%
    border-style: solid;
    border-width: 1px;
#map-area
    height: 100%
    padding-left: 15px
    display: inline-block
</style>
