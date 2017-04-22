<template>
    <div id="detail-view-container">
        <h2>Detailed View</h2>
        <div class="container">
            <div class='control-colum'>
            </div>
             <div class='control-colum'>
            </div>
             <div class='control-colum'>
            </div>
             <div class='control-colum'>
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
    border-bottom: 1px solid rgba(0, 0, 0, 0.4)
h2
    font-size: 1.05em
    margin-bottom: 5px
    text-align: center
.container
    width: 100%
    height: 100%
.row
    height: 100%
.control-colum
    height: 24%
    width: 110%
    border-style: dashed
    border-width: 1px
    border-color: grey
</style>
