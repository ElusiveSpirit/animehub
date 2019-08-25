<template lang="pug">
  v-app
    v-app-bar(color="primary" dark)
      v-toolbar-title AnimeHub
      v-spacer
      v-toolbar-items(row)
        template(
          v-for="item in menuItems"
        )
          v-btn(v-if="item.external" :href="item.to" target="_blank" :key="item.key" text) {{ item.text }}
          v-btn(v-else :to="item.to" :key="item.key" text) {{ item.text }}
        v-menu(v-if="false" offset-y)
          template(v-slot:activator="{ on }")
            v-btn(text v-on="on") Админ
          v-list
            v-list-item(@click="logout")
              v-list-item-title Выйти
    v-content
      v-container.px-0.py-0(
        fluid
        fill-height
      )
        nuxt
</template>

<script>
  export default {
    data: () => ({
      menuItems: [
        {
          to: '/catalog',
          key: 'catalog',
          text: 'Каталог',
          external: false,
        }
      ]
    }),
    methods: {
      async logout() {
        await this.$store.dispatch('resetVuex')
        await this.$auth.logout()
      }
    }
  }
</script>
