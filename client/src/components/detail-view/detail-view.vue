<template>
    <div id="detail-view-container" style="background-color: #343332;">
        <div class="container">
            <h1>Checkin Time</h1>
            <div class='control-colum'>
                <check-in-vis style="width: 100%; height: 100%"></check-in-vis>
            </div>
            <h1>Review Text Wordle</h1>
            <div class='control-colum'>
                <WordCloud style="width: 80% ;height: 100%; margin-left: 10%;  height: 90%; margin-top: 1.5%"></WordCloud>
            </div>
            <h1>Review Sentiment Analysis</h1>
             <div class='control-colum'>
                <sentiment-vis style="width: 100%; height: 100%"></sentiment-vis>
            </div>
             <!-- <div class='control-colum'>
            </div> -->
        </div>
    </div>
</template>

<script>
import CheckInVis from './checkin-vis';
import WordCloud from './word-cloud';
import SentimentVis from './sentiment-vis';

export default {
    name: 'DetailView',
    components: {
        CheckInVis,
        WordCloud,
        SentimentVis,
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
    height: 30%
    width: 110%
    border-style: solid
    border-width: 1px
    border-color: grey
</style>
