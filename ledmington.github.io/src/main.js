import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import VueWriter from "vue-writer";

import "./assets/css/main.scss";

createApp(App).use(router).use(VueWriter).mount("#app");
