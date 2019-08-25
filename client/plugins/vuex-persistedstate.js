import createPersistedState from 'vuex-persistedstate'

export default ({ store }) => {
  createPersistedState({
    key: 'animehub-persist',
    paths: []
  })(store)
}
