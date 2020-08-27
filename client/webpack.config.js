var path = require('path');

module.exports = {
    entry: './client.js',
    devServer: {
        compress: true,
        port: 80,
        index: './index.html'
    }
};