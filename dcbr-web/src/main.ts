import "./plugins/vuetify";
import "./registerServiceWorker";

//import VueKeycloakJs from "@dsb-norge/vue-keycloak-js";
import axios from "axios";
import Vue from "vue";

import App from "./App.vue";
import router from "./router";

Vue.config.productionTip = false;

new Vue({
  router,
  //store,
  render: h => h(App)
}).$mount("#app");
