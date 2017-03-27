// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
// import VueMaterial from 'vue-material';
import Vue from 'vue';
import App from './app';

/* eslint-disable no-new */
// Vue.use(VueMaterial);
new Vue({
    el: '#app',
    template: '<App/>',
    components: { App },
});
