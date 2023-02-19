<script setup lang="ts">
</script>

<template>
  <div class="wrapper">
    <div class="main-window">
      <div class="input-block">
        <input type="text" v-model="city">
        <button><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><!--! Font Awesome Pro 6.3.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path d="M416 208c0 45.9-14.9 88.3-40 122.7L502.6 457.4c12.5 12.5 12.5 32.8 0 45.3s-32.8 12.5-45.3 0L330.7 376c-34.4 25.2-76.8 40-122.7 40C93.1 416 0 322.9 0 208S93.1 0 208 0S416 93.1 416 208zM208 352a144 144 0 1 0 0-288 144 144 0 1 0 0 288z"/></svg></button>
      </div>
      <div class="cards">
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      city: '',
    }
  },
  methods: {
    // http://dataservice.accuweather.com/locations/v1/cities/search?apikey=PTTZWzHKWNQrpEaRn3tgfJKT4TV2xI1k&q=Нью-Йорк&language=ru
    getWeather() {
      let city = this.city
      let cityKey = ''
      fetch(`http://dataservice.accuweather.com/locations/v1/cities/search?apikey=PTTZWzHKWNQrpEaRn3tgfJKT4TV2xI1k&q=${city}&language=ru`).then(resp => { return resp.json() }).then(data => {
        cityKey = data[0].Key
        fetch(`http://dataservice.accuweather.com/currentconditions/v1/${cityKey}?apikey=PTTZWzHKWNQrpEaRn3tgfJKT4TV2xI1k&language=ru`).then(resp => { return resp.json() }).then(data => { console.log(data[0].Temperature.Metric.Value) })
      })
    }
  }
}
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
}

.wrapper {
  width: 100vw;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

.main-window {
  width: 1000px;
  height: 560px;
  border: solid 10px #1b1b1b;
  border-radius: 25px;
  background-color: #EAFBFF;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-around;
}

.input-block{
  width: 700px;
}
.input-block>input {
  width: 100%;
  height: 85px;
  padding-left: 15px;
  border: solid 5px #1b1b1b;
  border-radius: 15px;
  font-size: 36px;
  font-weight: 600;
  font-family: Montserrat, sans-serif;
}

.cards {
  height: 300px;
}</style>
