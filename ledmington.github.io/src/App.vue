<script setup>
import { RouterLink, RouterView } from "vue-router";
import MainTitle from "./components/MainTitle.vue";
</script>

<template>
  <header>
    <img
      alt="Vue logo"
      class="logo"
      src="@/assets/logo.svg"
      width="125"
      height="125"
    />

    <div class="wrapper">
      <MainTitle msg="You did it!" />
    </div>

    <nav>
      <RouterLink to="/">Home</RouterLink>
      <RouterLink to="/about">About</RouterLink>
      <RouterLink to="/cv">CV</RouterLink>
      <RouterLink to="/blog">Blog</RouterLink>
      <RouterLink to="/contact">Contact Me</RouterLink>
    </nav>
  </header>

  <!-- This is the actual content pointed by the router -->
  <RouterView />

  <footer>
    Powered by <a href="https://vuejs.org"><img src="./assets/logo.svg" /></a>.
    Hosted at
    <a href="https://github.com"><img src="./assets/github/github.svg" /></a>.
  </footer>
</template>

<style scoped lang="scss">
@import "colors.scss";

header {
  line-height: 1.5;
  max-height: 100vh;
}

footer > a > img {
  width: 20px;
  height: 20px;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

nav {
  // Fixed top
  width: 100%;
  position: fixed;
  top: 0;

  height: 10%;
  overflow: hidden;
  background-color: $background_dark;
  font-size: 12px;
  text-align: center;

  a {
    float: left;
    display: block;
    padding: 0 1rem;
    color: $text_color;

    // border-left: 1px solid red;

    // :first-of-type {
    //   border: 0;
    // }
  }
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

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}
</style>
