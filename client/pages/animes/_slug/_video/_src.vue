<template lang="pug">
  v-container.anime-video
    v-row
      v-col(cols="12")
        v-breadcrumbs(
          :items="breadcrumbs"
          divider=">"
        )
      v-col(
        cols="12"
        md="8"
        lg="9"
      )
        div.anime-video__container
          iframe.anime-video__frame(
            :src="videoSrc.embed_link"
          )
        v-btn(
          v-if="prevLink"
          color="primary"
          :to="prevLink"
        )
          v-icon mdi-chevron-left
          | {{ prevVideoNumber }} Серия
        v-btn(
          v-if="nextLink"
          color="primary"
          :to="nextLink"
        )
          v-icon mdi-chevron-right
          | {{ nextVideoNumber }} Серия
      v-col.hidden-sm-and-down(
        cols="12"
        md="4"
        lg="3"
      )
        v-img(
          v-if="anime.image"
          :height="450"
          :src="anime.image.link"
        )
</template>

<script>
  export default {
    async asyncData({ params: { slug, video, src }, $axios }) {
      try {
        const [anime, videoData, videoSrc] = await Promise.all([
          $axios.$get(`/catalog/animes/${slug}/`),
          $axios.$get(`/catalog/animes-video/${video}/`),
          $axios.$get(`/catalog/animes-video-src/${src}/`),
        ])
        return {
          anime,
          videoSrc,
          video: videoData,
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
      prevVideoNumber() {
        return this.videoSrc.prev_video?.number
      },
      prevLink() {
        if (this.videoSrc.prev_video) {
          return {
            name: 'animes-slug-video-src',
            params: {
              slug: this.anime.slug,
              video: this.videoSrc.prev_video.video_id,
              src: this.videoSrc.prev_video.id
            }
          }
        }
      },
      nextVideoNumber() {
        return this.videoSrc.next_video?.number
      },
      nextLink() {
        if (this.videoSrc.next_video) {
          return {
            name: 'animes-slug-video-src',
            params: {
              slug: this.anime.slug,
              video: this.videoSrc.next_video.video_id,
              src: this.videoSrc.next_video.id
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
            disabled: false,
            href: `/animes/${this.anime.slug}`
          },
          {
            text: 'Видео',
            disabled: true
          }
        ]
      }
    }
  }
</script>

<style lang="sass">
  .anime-video
    &__container
      position: relative
      background: #000
      width: 100%
      padding-bottom: 62%

    &__frame
      position: absolute
      width: 0
      min-width: 100%
      max-width: 100%
      height: 0
      max-height: 100%
      min-height: 100%
</style>
