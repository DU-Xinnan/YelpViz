<template>
    <div id="control-panel">
        <h5>Control Panel</h5>
        <img src="../pic/ControlPanel.png">
    </div>
</template>

<script>

export default {
    name: 'ControlPanel',
    mounted() {
    },
    data() {
        return {
        };
    },
    components: {

    },
    props: {
        setting: Object,
    },
};
</script>

<style lang="stylus" scoped>
#control-panel
    border-style: solid;
    border-width: 1px;
    height: 100%
h5
    padding-left: 5%
    padding-top: 10%
img
    padding-left: 5%
    width: 100%
</style>


