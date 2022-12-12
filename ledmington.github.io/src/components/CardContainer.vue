<template>
  <div class="container">
    <slot></slot>
  </div>
</template>

<style scope lang="scss">
@import "../assets/css/colors.scss";

.container {
  display: grid;
  grid-template-columns: 40% 60%;
}
</style>
