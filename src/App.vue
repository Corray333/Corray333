<script setup lang="ts">
</script>

<template>
  <div class="wrapper">
    <div class="main-window">
      <div class="input-block">
        <input type="text" v-model="city">
        <button @click="getWeather()"><img src="./components/icons/magnifying-glass.png" alt=""></button>
      </div>
      <div class="cards">
        <div class="card" v-for="(card, i) in cities">
          <h1>{{ card.temp }} C</h1>
          <h1>{{ card.city }}</h1>
          <h1>{{ card.weather }}</h1>
        </div>
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
      cities: []
    }
  },
  methods: {
    // http://dataservice.accuweather.com/locations/v1/cities/search?apikey=PTTZWzHKWNQrpEaRn3tgfJKT4TV2xI1k&q=Нью-Йорк&language=ru
    getWeather() {
      let city = this.city
      let cityKey = ''
      fetch(`http://dataservice.accuweather.com/locations/v1/cities/search?apikey=PTTZWzHKWNQrpEaRn3tgfJKT4TV2xI1k&q=${city}&language=ru`).then(resp => { return resp.json() }).then(data => {
        cityKey = data[0].Key
        fetch(`http://dataservice.accuweather.com/currentconditions/v1/${cityKey}?apikey=PTTZWzHKWNQrpEaRn3tgfJKT4TV2xI1k&language=ru`).then(resp => { return resp.json() }).then(data => {
          console.log(data[0])
          this.cities.push({
            temp: data[0].Temperature.Metric.Value,
            city: city,
            weather: data[0].WeatherText
          })
        })
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

.input-block {
  padding: 0;
  margin: 0;
  width: 700px;
  display: flex;
  justify-content: flex-end;
  align-items: center;
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

.input-block>button {
  width: 35px;
  height: 35px;
  border: none;
  background-color: transparent;
  position: absolute;
  display: block;
  transition: 0.3s;
  margin-right: 25px;
}

.input-block>button:hover {
  transform: scale(1.2);
  transition: 0.3ss;
}

.input-block>button>img {
  width: inherit;
  size: inherit;
}

.cards {
  height: 300px;
  width: 700px;
  display: flex;
  justify-content: space-between;
  padding: 0;
  margin: 0;
}

.card {
  height: 100%;
  width: 220px;
  border: solid 5px #1b1b1b;
  border-radius: 15px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-around;
}
</style>
