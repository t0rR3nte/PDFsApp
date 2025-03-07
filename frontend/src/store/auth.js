import { defineStore } from "pinia";
import axios from "axios";

export const useAuthStore = defineStore("auth", {
  state: () => ({
    user: null,
    token: localStorage.getItem("token") || null,
  }),

  actions: {
    async login(email, password, code) {
      try {
        const response = await axios.post("http://127.0.0.1:8000/api/users/login/", {
          email,
          password,
          code,
        });

        this.token = response.data.access;
        localStorage.setItem("token", this.token);
        axios.defaults.headers.common["Authorization"] = `Bearer ${this.token}`;
        return true;
      } catch (error) {
        console.error("Error en login", error);
        return false;
      }
    },
    async getQRCode() {
        try {
          const response = await axios.get("http://127.0.0.1:8000/api/users/qr-code/", {
            headers: { Authorization: `Bearer ${this.token}` },
          });
          return response.data.qr_code; // Devuelve la imagen en base64
        } catch (error) {
          console.error("Error obteniendo el código QR", error);
          return null;
        }
      },
      

    logout() {
      this.user = null;
      this.token = null;
      localStorage.removeItem("token");
      delete axios.defaults.headers.common["Authorization"];
    },
  },
});
