<template>
    <div id="app">
        <navbar></navbar>
        <div class="row" :style="{height: (setting.height ) + 'px', width: setting.width + 'px'}" style="position: absolute; background-color: #343332">
            <control-panel :setting="setting" class="col-2"></control-panel>
            <div class="col-7">
                <div class="row" style="height: 100%">
                    <overview></overview>
                </div>
            </div>
            <div class="col-3">
                <div class="row" style="height: 100%">
                    <detail-view></detail-view>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import 'bootstrap/dist/css/bootstrap.min.css';
import 'keen-ui/dist/keen-ui.min.css';
import Navbar from './components/nav-bar';
import ControlPanel from './components/control-panel/control-panel';
import Overview from './components/overview';
import DetailView from './components/detail-view/detail-view';

export default {
    name: 'App',
    components: {
        Navbar,
        ControlPanel,
        Overview,
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
