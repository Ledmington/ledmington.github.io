<template>
  <input
    id="theme-switch"
    @click="themeSwitch"
    type="checkbox"
    name="checkbox"
  />
</template>

<script>
export default {
  data: function () {
    return {
      theme: "dark",
    };
  },
  mounted() {},
  methods: {
    themeSwitch: function () {
      if (this.theme == "light") {
        this.theme = "dark";
      } else if (this.theme == "dark") {
        this.theme = "light";
      }
      console.log("The current theme is " + this.theme);
    },
  },
};
</script>

<style scoped lang="scss">
#theme-switch {
  position: relative;
  width: 80px;
  height: 38px;
  margin: 3px;
  appearance: none;
  -webkit-appearance: none;
  background-image: url("../assets/img/night-sky.png");
  background-size: cover;
  background-repeat: no-repeat;
  border-radius: 25px;
  box-shadow: inset 0px 0px 2px rgba(0, 0, 0, 0.7);
  transition: background-image 0.7s ease-in-out;
  outline: none;
  cursor: pointer;
  overflow: hidden;
}

#theme-switch:checked {
  background-image: url("../assets/img/day-sky.png");
  background-size: cover;
  transition: background-image 1s ease-in-out;
}

#theme-switch:after {
  content: "";
  display: none;
  height: 37px;
  border-radius: 20px;
  background-color: #ffffff;
  position: absolute;
  left: -43px;
  top: 1px;

  transform: translateX(0px);
  animation: off 0.7s forwards cubic-bezier(0.8, 0.5, 0.2, 1.4);
  box-shadow: inset 5px -5px 4px rgba(53, 53, 53, 0.3);
}

@keyframes off {
  0% {
    transform: translateX(80px);
    width: 46px;
  }

  50% {
    width: 75px;
    border-radius: 25px;
  }

  100% {
    transform: translateX(0px);
    width: 46px;
  }
}

#theme-switch:checked:after {
  animation: on 0.7s forwards cubic-bezier(0.8, 0.5, 0.2, 1.4);
  box-shadow: inset -5px -5px 4px rgba(53, 53, 53, 0.3);
}

@keyframes on {
  0% {
    transform: translateX(0px);
    width: 46px;
  }

  50% {
    width: 75px;
    border-radius: 25px;
  }

  100% {
    transform: translateX(80px);
    width: 46px;
  }
}

#theme-switch:checked:before {
  content: "";
  width: 15px;
  height: 15px;
  border-radius: 50%;
  position: absolute;
  left: 15px;
  top: 5px;
  transform-origin: 53px 10px;
  background-color: transparent;
  box-shadow: 5px -1px 0px #fff;
  filter: blur(0px);
  animation: sun 0.7s forwards ease;
}

@keyframes sun {
  0% {
    transform: rotate(170deg);
    background-color: transparent;
    box-shadow: 5px -1px 0px #fff;
    filter: blur(0px);
  }

  50% {
    background-color: transparent;
    box-shadow: 5px -1px 0px #fff;
    filter: blur(0px);
  }

  90% {
    background-color: #f5daaa;
    box-shadow: 0px 0px 10px #f5deb4, 0px 0px 20px #f5deb4, 0px 0px 30px #f5deb4,
      inset 0px 0px 2px #efd3a3;
    filter: blur(1px);
  }

  100% {
    transform: rotate(0deg);
    background-color: #f5daaa;
    box-shadow: 0px 0px 10px #f5deb4, 0px 0px 20px #f5deb4, 0px 0px 30px #f5deb4,
      inset 0px 0px 2px #efd3a3;
    filter: blur(1px);
  }
}

#theme-switch:before {
  content: "";
  width: 15px;
  height: 15px;
  border-radius: 50%;
  position: absolute;
  left: -30px;
  top: 4px;
  filter: blur(1px);
  background-color: #f5daaa;
  box-shadow: 0px 0px 10px #f5deb4, 0px 0px 20px #f5deb4, 0px 0px 30px #f5deb4,
    inset 0px 0px 2px #efd3a3;
  transform-origin: 53px 10px;
  animation: moon 0.7s forwards ease;
}

@keyframes moon {
  0% {
    transform: rotate(0deg);
    filter: blur(1px);
  }

  50% {
    filter: blur(1px);
  }

  90% {
    background-color: transparent;
    box-shadow: 5px -1px 0px #fff;
    filter: blur(0px);
  }

  100% {
    transform: rotate(170deg);
    background-color: transparent;
    box-shadow: 5px -1px 0px #fff;
    filter: blur(0px);
  }
}
</style>
