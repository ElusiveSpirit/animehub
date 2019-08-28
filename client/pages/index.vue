<template lang="pug">
  v-container
    v-row
      v-col
        v-container.anime-list(fluid)
          v-row
            v-col(
              v-for="anime in animes"
              :key="anime.id"
              cols="12"
              md="4"
              lg="3"
            )
              anime-card(
                :anime="anime"
              )
</template>

<script>
  import { mapState, mapGetters, mapMutations } from 'vuex'
  import AnimeCard from '../components/Anime/AnimeCard'

  export default {
    components: { AnimeCard },
    async asyncData({ $axios }) {
      try {
        const animes = await $axios.$get('/catalog/animes/')
        return {
          animes
        }
      } catch (e) {
        return {
          animes: []
        }
      }
    }
  }
</script>

<style lang="sass">
  .anime-list
    .v-card__title
      font-size: 1.3rem
</style>
