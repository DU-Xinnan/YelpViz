<template>
    <div id="app">
        <navbar></navbar>
        <div class="row" :style="{width: setting.width + 'px', height: setting.height + 'px'}" style="margin: 0">
            <control-panel :setting="setting"></control-panel>
            <overview-left></overview-left>
            <overview-Right></overview-Right>
            <detail-view></detail-view>
        </div>
    </div>
</template>

<script>
import 'bootstrap/dist/css/bootstrap.min.css';
import Navbar from './components/nav-bar';
import ControlPanel from './components//control-panel';
import OverviewLeft from './components/overview-left';
import OverviewRight from './components/overview-right';
import DetailView from './components/detail-view';

export default {
    name: 'App',
    components: {
        Navbar,
        ControlPanel,
        OverviewLeft,
        OverviewRight,
        DetailView,
    },
    data() {
        return {
            setting: {
                width: 0,
                height: 0,
            },
        };
    },
    mounted() {
        this.$nextTick(function foo() {
            this.initialize();
        });
    },
    methods: {
        initialize() {
            this.setting.height = window.innerHeight - document.querySelector('.navbar').clientHeight;
            this.setting.width = window.innerWidth;
            window.addEventListener('resize', () => {
                this.setting.height = window.innerHeight - document.querySelector('.navbar').clientHeight;
                this.setting.width = window.innerWidth;
            });
        },
    },
};
</script>

<style lang="stylus">
#app
    font-family: 'Avenir', Helvetica, Arial, sans-serif
    -webkit-font-smoothing: antialiased
    -moz-osx-font-smoothing: grayscale
    font-size: 0.875em
</style>
