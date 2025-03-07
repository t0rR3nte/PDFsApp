<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import { useAuthStore } from "@/store/auth";

const authStore = useAuthStore();
const pdfs = ref([]);
const title = ref("");
const file = ref(null);

const fetchPDFs = async () => {
  const response = await axios.get("http://127.0.0.1:8000/api/pdfs/");
  pdfs.value = response.data;
};

const uploadPDF = async () => {
  const formData = new FormData();
  formData.append("title", title.value);
  formData.append("file", file.value);

  await axios.post("http://127.0.0.1:8000/api/pdfs/", formData, {
    headers: { "Content-Type": "multipart/form-data" },
  });

  fetchPDFs();
};

const approvePDF = async (id) => {
  await axios.post(`http://127.0.0.1:8000/api/pdfs/${id}/approve/`);
  fetchPDFs();
};

onMounted(fetchPDFs);
</script>

<template>
  <div>
    <h1>Gestión de PDFs</h1>
    <input v-model="title" placeholder="Título" type="text" />
    <input type="file" @change="(e) => (file = e.target.files[0])" />
    <button @click="uploadPDF">Subir PDF</button>

    <h2>Lista de PDFs</h2>
    <ul>
      <li v-for="pdf in pdfs" :key="pdf.id">
        {{ pdf.title }}
        <a :href="pdf.file" target="_blank">Ver</a>
        <button v-if="!pdf.approved" @click="approvePDF(pdf.id)">Aprobar</button>
      </li>
    </ul>

    <button @click="authStore.logout">Cerrar sesión</button>
  </div>
</template>
