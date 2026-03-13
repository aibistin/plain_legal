<template>
  <v-app>
    <v-app-bar color="primary" elevation="2">
      <NuxtLink to="/" class="text-decoration-none">
        <v-app-bar-title class="text-white font-weight-bold">
          <v-icon icon="mdi-scale-balance" class="mr-2" />
          Plain Legal
        </v-app-bar-title>
      </NuxtLink>
    </v-app-bar>

    <v-main>
      <NuxtPage />
    </v-main>

    <v-footer color="secondary" class="text-white text-caption pa-3">
      <v-container>
        <span>Plain Legal &mdash; Legal document templates under </span>
        <a
          href="https://creativecommons.org/licenses/by/4.0/"
          target="_blank"
          class="text-white"
        >CC BY 4.0</a>
        <span> via CommonPaper</span>
      </v-container>
    </v-footer>
  </v-app>
</template>
