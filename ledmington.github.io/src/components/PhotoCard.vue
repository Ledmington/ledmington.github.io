<script setup>
import GithubIcon from "./icons/GithubIcon.vue";
import LinkedinIcon from "./icons/LinkedinIcon.vue";
import StackOverflowIcon from "./icons/StackOverflowIcon.vue";
import LocationIcon from "./icons/LocationIcon.vue";
import MailIcon from "./icons/MailIcon.vue";
import HyperlinkIcon from "./icons/HyperlinkIcon.vue";
</script>

<template>
  <div class="card">
    <h3>
      <slot name="title"></slot>
    </h3>
    <p class="profile-links">
      <a href="https://github.com/Ledmington"><GithubIcon /></a
      ><a href="https://www.linkedin.com/in/filippo-barbari-bb2b55181/"
        ><LinkedinIcon /></a
      ><a href="https://stackoverflow.com/users/18851577/filippo-barbari"
        ><StackOverflowIcon
      /></a>
    </p>
    <h6><LocationIcon /><slot name="location"></slot></h6>
    <h6><MailIcon /><slot name="email"></slot></h6>
    <h6><HyperlinkIcon /><slot name="url"></slot></h6>
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
