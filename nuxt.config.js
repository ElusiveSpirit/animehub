import pkg from './package'
import ru from 'vuetify/lib/locale/ru'

module.exports = {
  mode: 'universal',

  /*
  ** Headers of the page
  */
  head: {
    title: 'Animehub',
    titleTemplate: '%s - Animehub',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: pkg.description },
      { name: 'yandex-verification', content: '777ebcfdb118d1c2' }
    ],
    link: [{ rel: 'icon', type: 'image/x-icon', href: '/logo.png' }]
  },

  /*
  ** Customize the progress-bar color
  */
  loading: { color: '#3B8070' },

  /*
  ** Global CSS
  */
  css: [
    '@/assets/css/styles.sass',
    '@/assets/css/animation.scss',
  ],

  /*
  ** Plugins to load before mounting the App
  */
  plugins: [
    '@/plugins/vue-lazyload',
    // { src: '@/plugins/vuex-persistedstate', ssr: false },
  ],
  auth: {
    strategies: {
      local: {
        endpoints: {
          login: { url: '/api/token/auth/', method: 'post', propertyName: 'token' },
          logout: { url: '/api/rest-auth/logout/', method: 'post' },
          user: { url: '/api/rest-auth/user/', method: 'get', propertyName: false }
        },
        tokenRequired: true,
        tokenType: 'Bearer',
      },
    },
    redirect: {
      login: '/login',
      logout: '/login',
      callback: '/login',
      home: '/',
    },
    plugins: [
      '@/plugins/auth',
    ],
  },
  /*
  ** Nuxt.js modules
  */
  modules: [
    // Doc: https://github.com/nuxt-community/axios-module#usage
    '@nuxtjs/axios',
    'yandex-metrika-module',
  ],
  buildModules: [
    '@nuxtjs/vuetify',
  ],
  /*
  ** Axios module configuration
  */
  axios: {
    prefix: '/server-api',
    proxy: true
  },
  proxy: {
    '/server-api/': {
      target: process.env.PROXY_API_URL || 'http://127.0.0.1:8000/',
      pathRewrite: {'^/server-api/': '/api/v1/'}
    }
  },
  pageTransition: 'fade',

  /*
   * Analytics
   */
  'yandex-metrika': {
    id: '50847077',
    options: {
      clickmap:true,
      trackLinks:true,
      accurateTrackBounce:true,
      webvisor: true
    }
  },

  vuetify: {
    icons: {
      iconfont: 'mdi',
    },
    lang: {
      locales: { ru },
      current: 'ru'
    },
    theme: {
      themes: {
        light: {
          primary: '#393e4a',
          secondary: '#eaeaea',
          accent: '#1da57a',
          error: '#FF5252',
          info: '#2196F3',
          success: '#4CAF50',
          warning: '#FFC107',
        },
      }
    }
  },
  /*
  ** Build configuration
  */
  srcDir: 'client/',
  build: {
    babel: {
      plugins: ['@babel/plugin-proposal-optional-chaining']
    },
    /*
    ** You can extend webpack config here
    */
    extend(config, ctx) {
      // Run ESLint on save
      if (ctx.isDev && ctx.isClient) {
        config.module.rules.push({
          enforce: 'pre',
          test: /\.(js|vue)$/,
          loader: 'eslint-loader',
          exclude: /(node_modules)/
        })
      }
    }
  }
}
