<template>
    <div class="col-2" id="control-panel">
        <h2>Control Panel</h2>
       <div class='control-column'>
            <data-loader></data-loader>
            <attr-list :setting="setting"></attr-list>
       </div>
    </div>
</template>

<script>
import './control-panel.styl';
// import DataLoader from './data-loader';

export default {
    name: 'ControlPanel',
    mounted() {
    },
    data() {
        return {
        };
    },
    components: {
        // DataLoader,
    },
    props: {
        setting: Object,
    },
};
</script>