import { createRouter, createWebHistory } from "vue-router";
import Login from "@/views/Login.vue";
import Register from "@/views/Register.vue";
import Dashboard from "@/views/Dashboard.vue";
import Setup2FA from "@/views/Setup2FA.vue";

const routes = [
  { path: "/", component: Login },
  { path: "/register", component: Register },
  { path: "/setup-2fa", component: Setup2FA },
  { path: "/dashboard", component: Dashboard },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
