<template>
    <div id="data-loader" class="control-section">
        <h3 class="control-panel-label">Load Data: </h3>
        <select class="custom-select skyline-select" id="data-loader-selector" v-model="selectedDataName">
            <option v-for="dataname in dataList" :value="dataname">{{dataname}}</option>
        </select>
    </div>
</template>

<script>
import NetService from '../../services/net-service';
import PipeService from '../../services/pipe-service';
import DataService from '../../services/data-service';

export default {
    name: 'DataLoader',
    mounted() {
        NetService.getDataList((response) => {
            this.dataList = response.data;
        });
    },
    data() {
        return {
            selectedDataName: '',
            dataList: [],
        };
    },
    watch: {
        selectedDataName(newValue) {
            NetService.getCloudData(newValue, (response) => {
                const Data = response.data;
                DataService.setCloudData(Data);
            });

            NetService.getSentimentData(newValue, (response) => {
                const Data = response.data;
                DataService.setSentimentData(Data);
            });

            NetService.getData(newValue, (response) => {
                const Data = response.data;
                DataService.setRawData(Data);
                DataService.setCity(newValue);
                PipeService.$emit(PipeService.DATA_CHANGE, newValue);
            });
        },
    },
};
</script>

<style lang="stylus" scoped>

@import './control-panel.styl'

.skyline-select
    width: 100%
    height: 24px
    font-size: 1em
    padding-top: 1px
h3
    color: #D3D3D3
</style>
