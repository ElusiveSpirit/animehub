<template lang="pug">
  v-container
    v-row
      v-col(cols="12")
        v-breadcrumbs(
          :items="breadcrumbs"
          divider=">"
        )
      v-col(
        cols="12"
        md="4"
        lg="3"
      )
        v-img(
          v-if="anime.image"
          :height="450"
          :src="anime.image.link"
        )
      v-col(
        cols="12"
        md="4"
        lg="3"
      )
        div.title {{ anime.title }}
        div.subtitle-1 {{ anime.title_latin }}
        v-btn(
          :to="watchBtn"
          :disabled="!anime.first_video_source"
          color="primary"
        ) Смотреть
</template>

<script>
  export default {
    async asyncData({ params: { slug }, $axios }) {
      try {
        const anime = await $axios.$get(`/catalog/animes/${slug}/`)
        return {
          anime
        }
      } catch (e) {
        return {
          anime: {}
        }
      }
    },
    data: () => ({
      anime: {}
    }),
    computed: {
      firstVideo() {
        return 'video-id'
      },
      watchBtn() {
        if (this.anime.first_video_source) {
          return {
            name: 'animes-slug-video-src',
            params: {
              slug: this.anime.slug,
              video: this.anime.first_video_source.video_id,
              src: this.anime.first_video_source.id
            }
          }
        }
      },
      breadcrumbs() {
        return [
          {
            text: 'Аниме',
            disabled: false,
            href: '/'
          },
          {
            text: this.anime.title,
            disabled: true
          }
        ]
      }
    }
  }
</script>
