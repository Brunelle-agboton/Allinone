module.exports = {
  configureWebpack: {
    resolve: {
      alias: {
        'vue$': 'vue/dist/vue.esm-bundler.js'
      }
    }
    },
     devServer: {
    proxy: {
      '/api': {
        target: 'http://back:5000',  
        ws: true,
        changeOrigin: true,
      },
    },
  },
};
