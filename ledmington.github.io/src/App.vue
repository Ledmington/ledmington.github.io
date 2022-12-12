<script setup>
import { RouterLink, RouterView } from "vue-router";
// import MainTitle from "./components/MainTitle.vue";
</script>

<template>
  <header>
    <!-- <div class="wrapper">
      <MainTitle msg="You did it!" />
    </div> -->

    <nav>
      <RouterLink to="/">Home</RouterLink>
      <RouterLink to="/about">About</RouterLink>
      <RouterLink to="/cv">CV</RouterLink>
      <RouterLink to="/blog">Blog</RouterLink>
      <RouterLink to="/contact">Contact Me</RouterLink>
    </nav>

    <input
      id="theme-switch"
      @click="themeSwitch"
      type="checkbox"
      name="checkbox"
    />
  </header>

  <!-- This is the actual content pointed by the router -->
  <RouterView />

  <footer>
    Powered by
    <a href="https://vuejs.org">Vue.js</a>. Hosted at
    <a href="https://github.com">GitHub</a>.
  </footer>
</template>

<script>
export default {
  data: () => {},
  mounted() {},
  methods: {
    themeSwitch: function () {
      console.log("Switching theme");
    },
  },
};
</script>

<style scoped lang="scss">
@import "./assets/css/colors.scss";

.logo {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  display: block;
  margin: 0 auto 2rem;
}

header {
  // Fixed top
  width: 100%;
  position: absolute;
  top: 0;

  height: 10%;
  overflow: hidden;
  background-color: $background_dark;
  font-size: 12px;
  text-align: center;

  a {
    float: left;
    display: block;
    border-radius: 5px;
    padding: 0 1rem;

    // border-left: 1px solid red;

    // :first-of-type {
    //   border: 0;
    // }
  }

  input {
    float: right;
    position: relative;
    width: 80px;
    height: 38px;
    border-radius: 25px;
    background-image: url("./assets/img/day-sky.png");
    background-size: cover;
  }
}

footer {
  // Fixed bottom
  width: 100%;
  position: absolute;
  bottom: 0;
  left: 0;

  text-align: center;
  height: 10%;
  background-color: $background_dark;
  color: $white_text_color;
}

// nav a.router-link-exact-active {
//   color: var(--color-text);
// }

// nav a.router-link-exact-active:hover {
//   background-color: transparent;
// }

// nav a {
//   display: inline-block;
//   padding: 0 1rem;
//   border-left: 1px solid var(--color-border);
// }

// nav a:first-of-type {
//   border: 0;
// }

// @media (min-width: 1024px) {
//   header {
//     display: flex;
//     place-items: center;
//     padding-right: calc(var(--section-gap) / 2);
//   }

//   .logo {
//     margin: 0 2rem 0 0;
//   }

//   header .wrapper {
//     display: flex;
//     place-items: flex-start;
//     flex-wrap: wrap;
//   }

//   nav {
//     text-align: left;
//     margin-left: -1rem;
//     font-size: 1rem;

//     padding: 1rem 0;
//     margin-top: 1rem;
//   }
// }
</style>
