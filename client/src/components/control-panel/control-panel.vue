<template>
    <div class="col-2" id="control-panel">
        <h1 style="margin-top: 5%">Control Panel</h1>
       <div class='control-column'>
            <data-loader></data-loader>
       </div>
    </div>
</template>

<script>
import './control-panel.styl';
import DataLoader from './data-loader';

export default {
    name: 'ControlPanel',
    mounted() {
    },
    data() {
        return {
        };
    },
    components: {
        DataLoader,
    },
    props: {
        setting: Object,
    },
};
</script>