<template>
  <div class="card-grid">
    <slot></slot>
  </div>
</template>

<style scoped lang="scss">
@import "../assets/css/colors.scss";

.card-grid {
  display: grid;
  grid-template-columns: 40% 60%;
  width: 100%;
}
</style>
