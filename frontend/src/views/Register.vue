<script setup>
import { ref } from "vue";
import axios from "axios";
import { useRouter } from "vue-router";

const email = ref("");
const password = ref("");
const username = ref("");
const router = useRouter();

const register = async () => {
  await axios.post("http://127.0.0.1:8000/api/users/register/", {
    username: username.value,
    email: email.value,
    password: password.value,
  });
  router.push("/setup-2fa"); // Ir a la página de configuración de 2FA
};

</script>

<template>
  <div>
    <h1>Registro</h1>
    <input v-model="username" placeholder="Usuario" type="text" />
    <input v-model="email" placeholder="Email" type="email" />
    <input v-model="password" placeholder="Contraseña" type="password" />
    <button @click="register">Registrarse</button>
  </div>
</template>
