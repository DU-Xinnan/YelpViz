<template>
    <div id="detail-view-container">
        <h5>Detailed View</h5>
        <div class="container">
            <div class="row">
                <div class="col-3">
                    <h6>Food Text Wordle</h6>
                    <img src="../pic/foodtext.png">
                </div>
                <div class="col-3">
                    <h6>Clients Flow Chart</h6>
                    <img src="../pic/clock.png">
                </div>
                <div class="col-3">
                    <h6>Sentiment</h6>
                    <img src="../pic/sentiment.png">
                </div>
                <div class="col-3">
                    <h6>Food Category</h6>
                    <img src="../pic/pie.png">
                </div>
            </div>
        </div>
    </div>
</template>

<script>

export default {
    name: 'DetailView',
    data() {
        return {
        };
    },
    mounted() {

    },
};
</script>

<style lang="stylus" scoped>
#detail-view-container
    width: 100%
    border-style: solid
    border-width: 1px
h5
    padding-left: 30px
.container
    width: 95%
    height: 100%
.row
    height: 100%
.col-3
    height: 90%
    border-style: dashed
    border-width: 1px
    border-color: grey
img
    height: 80%
    width: 100%
</style>
