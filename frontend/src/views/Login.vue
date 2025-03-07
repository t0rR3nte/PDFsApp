<template>
  <div>
    <h2>Iniciar Sesión</h2>
    <form @submit.prevent="login">
      <input type="email" v-model="email" placeholder="Correo electrónico" required />
      <input type="password" v-model="password" placeholder="Contraseña" required />
      <input type="text" v-model="otpToken" placeholder="Código 2FA" required />
      <button type="submit">Iniciar sesión</button>
    </form>
  </div>
</template>

<script>
import { ref } from "vue";
import { useRouter } from "vue-router";
import axios from "axios";

export default {
  setup() {
    const email = ref("");
    const password = ref("");
    const otpToken = ref("");
    const router = useRouter();

    const login = async () => {
      console.log("Datos antes de enviar:", {
        email: email.value,
        password: password.value,
        otp_token: otpToken.value,
      });

      if (!email.value || !password.value || !otpToken.value) {
        console.error("❌ ERROR: Faltan datos");
        return;
      }

      try {
        const response = await axios.post("http://127.0.0.1:8000/api/users/login/", {
          email: email.value,
          password: password.value,
          otp_token: otpToken.value,
        });

        console.log("✅ Login exitoso:", response.data);
        router.push("/dashboard");
      } catch (error) {
        console.error("❌ Error al iniciar sesión:", error.response?.data || error.message);
      }
    };

    return {
      email,
      password,
      otpToken,
      login,
    };
  },
};
</script>
