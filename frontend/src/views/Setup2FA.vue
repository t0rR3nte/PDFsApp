<script setup>
import { ref, onMounted } from "vue";
import { useAuthStore } from "@/store/auth";

const authStore = useAuthStore();
const qrCode = ref("");

onMounted(async () => {
  qrCode.value = await authStore.getQRCode();
});
</script>

<template>
  <div>
    <h1>Configurar 2FA</h1>
    <p>Escanea este código con Google Authenticator:</p>
    <img v-if="qrCode" :src="qrCode" alt="Código QR" />
    <p v-else>Cargando QR...</p>
  </div>
</template>
