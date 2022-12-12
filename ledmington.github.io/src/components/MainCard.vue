<template>
  <div class="card">
    <h3>
      <slot name="title"></slot>
    </h3>
    <slot name="content"></slot>
  </div>
</template>

<style scoped lang="scss">
@import "../assets/css/colors.scss";

.card {
  border-radius: 10px;
  background-color: $background_dark_lighter;
  color: $white_text_color;
  border: 2px solid black;
  margin: 10px;
  padding: 5px;
}
</style>
