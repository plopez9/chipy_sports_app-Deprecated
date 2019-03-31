const proxy = require('http-proxy-middleware');

module.exports = function(app) {
    app.use(proxy('/nba_package', {
        target: 'http://127.0.0.1:8000/',
        changeOrigin: true,
        onProxyReq(proxyReq) {
            if (proxyReq.getHeader("origin")) {
                proxyReq.setHeader("origin", "https://127.0.0.1")
            }
        },
        pathRewrite: { "^/nba_package": "" },
        logLevel: "debug",
    })
)
