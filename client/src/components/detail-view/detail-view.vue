<template>
    <div id="detail-view-container">
        <h1>Detailed View</h1>
        <div class="container">
            <div class='control-colum'>
                <check-in-vis></check-in-vis>
                <img src='./radarchart.jpg' style="width: 60% ;height: 100%; margin-left: 20%" >
            </div>
            <div class='control-colum'>
                <img src='./wordle.jpg' style="width: 60% ;height: 100%; margin-left: 20%" >
            </div>
             <div class='control-colum'>
                 <img src='./sentiment.png' style="width: 60% ;height: 100%; margin-left: 20%" >
            </div>
             <!-- <div class='control-colum'>
            </div> -->
        </div>
    </div>
</template>

<script>
import CheckInVis from './checkin-vis';

export default {
    name: 'DetailView',
    components: {
        CheckInVis,
    },
    mounted() {
    },
    data() {
        return {
        };
    },
};
</script>

<style lang="stylus" scoped>
#detail-view-container
    width: 100%
    border-bottom: 1px solid rgba(0, 0, 0, 0.4)
h1
    font-size: 1.25em
    margin-bottom: 5px
    text-align: center
.container
    width: 100%
    height: 100%
.row
    height: 100%
.control-colum
    height: 32%
    width: 110%
    border-style: dashed
    border-width: 1px
    border-color: grey
</style>
