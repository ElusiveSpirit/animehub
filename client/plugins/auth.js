export default function({ app, store }) {
  app.$axios.onError(error => {
    const code = parseInt(error.response && error.response.status)

    if ([401, 403].includes(code)) {
      app.$auth.logout();
    }

    return Promise.reject(error);
  })
  app.$auth.onError((error, name, endpoint) => {
    store.dispatch('resetVuex')
  })
}
