const path = require('path')

const rootDir = path.resolve(__dirname) + 'client'

module.exports = {
  resolve: {
    extensions: ['.js', '.json', '.vue', '.ts'],
    root: rootDir,
    alias: {
      '@': rootDir,
      '~': rootDir
    }
  }
}
