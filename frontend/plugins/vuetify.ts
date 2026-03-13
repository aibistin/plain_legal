import 'vuetify/styles'
import { createVuetify } from 'vuetify'

export default defineNuxtPlugin((app) => {
  const vuetify = createVuetify({
    theme: {
      defaultTheme: 'light',
      themes: {
        light: {
          colors: {
            primary: '#1565C0',
            secondary: '#37474F',
            accent: '#0288D1',
            error: '#C62828',
            warning: '#EF6C00',
            info: '#0277BD',
            success: '#2E7D32',
          },
        },
      },
    },
  })
  app.vueApp.use(vuetify)
})
