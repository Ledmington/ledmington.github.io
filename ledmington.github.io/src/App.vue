<script setup>
import { RouterLink, RouterView } from "vue-router";
import ThemeSwitcher from "./components/ThemeSwitcher.vue";
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

    <ThemeSwitcher />
  </header>

  <!-- This is the actual content pointed by the router -->
  <RouterView />

  <footer>
    Powered by
    <a href="https://vuejs.org">Vue.js</a>. Hosted at
    <a href="https://github.com">GitHub</a>.
  </footer>
</template>

<style scoped lang="scss">
@import "./assets/css/colors.scss";

header {
  // Fixed top
  width: 100%;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  margin: 0;
  overflow: auto;
  z-index: 1030;
  box-shadow: #000 0px 0px 8px;

  height: 8%;
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
}

footer {
  // Fixed bottom
  width: 100%;
  bottom: 0;
  left: 0;
  right: 0;

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
