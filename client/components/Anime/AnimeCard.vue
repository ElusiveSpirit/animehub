<template lang="pug">
  v-card(:height="500")
    nuxt-link(
      :to="link"
    )
      v-img(
        :height="350"
        :src="anime.image.link"
      )
      v-card-title {{ anime.title }}
</template>

<script>
  export default {
    props: {
      anime: {
        type: Object,
        required: true
      }
    },
    computed: {
      link() {
        return { name: 'animes-slug', params: { slug: this.anime.slug } }
      }
    }
  }
</script>
