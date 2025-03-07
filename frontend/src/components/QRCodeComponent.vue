<template>
    <div>
      <h2>Escanea este código QR</h2>
      <img v-if="qrCode" :src="qrCode" alt="QR Code">
      <button @click="getQRCode">Generar QR</button>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    data() {
      return {
        qrCode: "",
      };
    },
    methods: {
      async getQRCode() {
        try {
          const response = await axios.get("http://127.0.0.1:8000/api/generate_qr_code/");
          this.qrCode = response.data.qr_code; // 🔹 Guardar la imagen en base64
        } catch (error) {
          console.error("Error al obtener el QR:", error.response);
        }
      },
    },
  };
  </script>
  