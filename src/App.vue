<!-- <script setup lang="ts"> -->
<!-- </script> -->

<template>
  <Transition name="bounce">
    <div class="alert" v-if="alert">{{ alert }}</div>
  </Transition>
  <div class="wrapper">
    <div class="main-window">
      <div class="input-block">
        <input type="text" v-model="city">
        <button @click="getWeather(this.city)"><img src="./components/icons/magnifying-glass.png" alt=""></button>
      </div>
      <div class="cards">
        <TransitionGroup name="bounce">
          <div class="card" :class="card.time" v-for="(card, i) in cities" :key="i">
            <button @click="delCard(i)">-</button>
            <img :src="'/src/components/icons/' + card.weatherPicture + '.png'" alt="">
            <span>
              <h1>{{ Math.ceil(card.temp) }} C</h1>
              <h1>{{ card.city }}</h1>
            </span>
          </div>
        </TransitionGroup>
      </div>
    </div>
  </div>
</template>

<script >
// <script  setup lang="ts">
// import { ref, onMounted } from 'vue'

// const city = ref('')
// const cities = ref([])
// const alert = ref('')

// function delCard(i) {
//   cities.value.splice(i, 1)
//   let citiesNames = []
//   for (let i = 0; i < cities.value.length; i++) citiesNames.push(cities.value[i].city)
//   localStorage.setItem('cities', JSON.stringify(citiesNames))
// }
// function getWeather(city) {
//   if (cities.value.length < 3) {
//     let url = `https://api.tomorrow.io/v4/weather/realtime?location=${city}&apikey=X570qK9SKTRbhja3nOfFQbOWZNCLDhdS`
//     fetch(url).then(resp => { return resp.json() }).then(data => {
//       if (cities.value.filter(city => JSON.stringify(city.location) == JSON.stringify(data.location)).length == 0) {
//         cities.value.push({
//           temp: data.data.values.temperature,
//           city: city,
//           weather: {
//             "0": "Unknown",
//             "1000": "Clear, Sunny",
//             "1100": "Mostly Clear",
//             "1101": "Partly Cloudy",
//             "1102": "Mostly Cloudy",
//             "1001": "Cloudy",
//             "2000": "Fog",
//             "2100": "Light Fog",
//             "4000": "Drizzle",
//             "4001": "Rain",
//             "4200": "Light Rain",
//             "4201": "Heavy Rain",
//             "5000": "Snow",
//             "5001": "Flurries",
//             "5100": "Light Snow",
//             "5101": "Heavy Snow",
//             "6000": "Freezing Drizzle",
//             "6001": "Freezing Rain",
//             "6200": "Light Freezing Rain",
//             "6201": "Heavy Freezing Rain",
//             "7000": "Ice Pellets",
//             "7101": "Heavy Ice Pellets",
//             "7102": "Light Ice Pellets",
//             "8000": "Thunderstorm"
//           }[data.data.values.weatherCode],
//           weatherPicture: {
//             "0": "Unknown",
//             "1000": new Date().getHours() < 20 ? "clearDay" : "clearNight",
//             "1100": new Date().getHours() < 20 ? "mostlyClearDay" : "mostlyClearNight",
//             "1101": new Date().getHours() < 20 ? "partlyCloudyDay" : "partlyCloudyNight",
//             "1102": new Date().getHours() < 20 ? "mostlyCloudyDay" : "mostlyCloudyNight",
//             "1001": "cloudy",
//             "2000": "Fog",
//             "2100": "Light Fog",
//             "4000": "Drizzle",
//             "4001": "Rain",
//             "4200": "Light Rain",
//             "4201": "Heavy Rain",
//             "5000": "Snow",
//             "5001": "Flurries",
//             "5100": "Light Snow",
//             "5101": "Heavy Snow",
//             "6000": "Freezing Drizzle",
//             "6001": "Freezing Rain",
//             "6200": "Light Freezing Rain",
//             "6201": "Heavy Freezing Rain",
//             "7000": "Ice Pellets",
//             "7101": "Heavy Ice Pellets",
//             "7102": "Light Ice Pellets",
//             "8000": "Thunderstorm"
//           }[data.data.values.weatherCode],
//           location: data.location,
//           time: new Date().getHours() > 20 || new Date().getHours() < 6 ? 'night' : 'day'
//         })
//         let citiesNames = []
//         for (let i = 0; i < cities.value.length; i++) citiesNames.push(cities.value[i].city)
//         localStorage.setItem('cities', JSON.stringify(citiesNames))
//       }
//       else {
//         alert.value = 'Город уже добавлен!'
//         setTimeout(() => {
//           alert.value = ''
//         }, "3000")
//       }
//     })
//   }
//   else {
//     alert.value = 'Достигнут лимит закрепленных городов!'
//     setTimeout(() => {
//       alert.value = ''
//     }, "3000")
//   }
// }

// onMounted(() => {
//   let citiesNames = JSON.parse(localStorage.getItem('cities'))
//   if (citiesNames != null) {
//     for (let i = 0; i < citiesNames.length; i++) getWeather(citiesNames[i])
//   }
//   else {
//     cities.value = []
//   }
// })

export default {
  name: 'App',
  data() {
    return {
      city: '',
      cities: [],
      alert: ''
    }
  },
  created: function () {
    this.$nextTick(function () {
      let citiesNames = JSON.parse(localStorage.getItem('cities'))
      if (citiesNames != null) {
        for (let i = 0; i < citiesNames.length; i++) this.getWeather(citiesNames[i])
      }
      else {
        this.cities = []
      }
    })
  },
  methods: {
    delCard(i) {
      this.cities.splice(i, 1)
      let citiesNames = []
      for (let i = 0; i < this.cities.length; i++) citiesNames.push(this.cities[i].city)
      localStorage.setItem('cities', JSON.stringify(citiesNames))
    },
    getWeather(city) {
      if (this.cities.length < 3) {
        let url = `https://api.tomorrow.io/v4/weather/realtime?location=${city}&apikey=X570qK9SKTRbhja3nOfFQbOWZNCLDhdS`
        fetch(url).then(resp => { return resp.json() }).then(data => {
          if (this.cities.filter(city => JSON.stringify(city.location) == JSON.stringify(data.location)).length == 0) {
            this.cities.push({
              temp: data.data.values.temperature,
              city: city,
              weather: {
                "0": "Unknown",
                "1000": "Clear, Sunny",
                "1100": "Mostly Clear",
                "1101": "Partly Cloudy",
                "1102": "Mostly Cloudy",
                "1001": "Cloudy",
                "2000": "Fog",
                "2100": "Light Fog",
                "4000": "Drizzle",
                "4001": "Rain",
                "4200": "Light Rain",
                "4201": "Heavy Rain",
                "5000": "Snow",
                "5001": "Flurries",
                "5100": "Light Snow",
                "5101": "Heavy Snow",
                "6000": "Freezing Drizzle",
                "6001": "Freezing Rain",
                "6200": "Light Freezing Rain",
                "6201": "Heavy Freezing Rain",
                "7000": "Ice Pellets",
                "7101": "Heavy Ice Pellets",
                "7102": "Light Ice Pellets",
                "8000": "Thunderstorm"
              }[data.data.values.weatherCode],
              weatherPicture: {
                "0": "Unknown",
                "1000": new Date().getHours() < 20 ? "clearDay" : "clearNight",
                "1100": new Date().getHours() < 20 ? "mostlyClearDay" : "mostlyClearNight",
                "1101": new Date().getHours() < 20 ? "partlyCloudyDay" : "partlyCloudyNight",
                "1102": new Date().getHours() < 20 ? "mostlyCloudyDay" : "mostlyCloudyNight",
                "1001": "cloudy",
                "2000": "Fog",
                "2100": "Light Fog",
                "4000": "Drizzle",
                "4001": "Rain",
                "4200": "Light Rain",
                "4201": "Heavy Rain",
                "5000": "Snow",
                "5001": "Flurries",
                "5100": "Light Snow",
                "5101": "Heavy Snow",
                "6000": "Freezing Drizzle",
                "6001": "Freezing Rain",
                "6200": "Light Freezing Rain",
                "6201": "Heavy Freezing Rain",
                "7000": "Ice Pellets",
                "7101": "Heavy Ice Pellets",
                "7102": "Light Ice Pellets",
                "8000": "Thunderstorm"
              }[data.data.values.weatherCode],
              location: data.location,
              time: new Date().getHours() > 20 || new Date().getHours() < 6 ? 'night' : 'day'
            })
            let citiesNames = []
            for (let i = 0; i < this.cities.length; i++) citiesNames.push(this.cities[i].city)
            localStorage.setItem('cities', JSON.stringify(citiesNames))
          }
          else {
            this.alert = 'Город уже добавлен!'
            setTimeout(() => {
              this.alert = ''
            }, "3000")
          }
        })
      }
      else {
        this.alert = 'Достигнут лимит закрепленных городов!'
        setTimeout(() => {
          this.alert = ''
        }, "3000")
      }
    }
  }
}
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
}

.alert {
  position: absolute;
  width: 300px;
  height: 50px;
  border-radius: 15px;
  background-color: #81D4F8;
  border: solid 5px #1b1b1b;
  filter: drop-shadow(0px 0px 10px rgba(0, 0, 0, 0.25));
  margin: 25px;
  right: 0;
  color: rgb(255, 255, 255);
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 16px;
  font-weight: 600;
  font-family: Montserrat, sans-serif;
  padding: 15px;
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
  padding: 0;
  margin: 0;
}

.day {
  background-color: #81D4F8;
}

.night {
  background-color: #283651;
}

.card {
  height: 100%;
  width: 220px;
  border: solid 5px #1b1b1b;
  border-radius: 15px;
  display: flex;
  flex-direction: column;
  align-items: center;
  transition: 0.4s;
  justify-content: space-around;
  position: relative;
}

.card>button {
  position: absolute;
  top: 0;
  right: 0;
  margin-right: 15px;
  background-color: transparent;
  border: none;
  color: white;
  font-weight: 1000;
  font-size: 36px;
  transition: .2s;
  padding: 0;
  font-family: Montserrat, sans-serif;
  box-sizing: content-box;
  padding: 0s;
}

.card>button:hover {
  transform: scale(1.3);
  transition: .2s;
}

.card>img {
  height: 100px;
}

.card {
  text-align: center;
  color: white;
  margin-right: 4px;
}

.bounce-enter-active {
  animation: bounce-in 0.5s;
}

.bounce-leave-active {
  animation: bounce-in 0.5s reverse;
}

@keyframes bounce-in {
  0% {
    transform: scale(0);
  }

  50% {
    transform: scale(1.1);
  }

  100% {
    transform: scale(1);
  }
}
</style>
