const path = require('path');

const config = {
  entry: [
    './src/index.js',
  ],
  optimization: {
      minimize: true
  },
  module: {
    rules: [
      {
          test: /\.css$/,
          use: ['style-loader', 'css-loader']
      },
      {
        test: /\.jsx?$/,
        loaders: [
          'babel-loader',
        ],
        exclude: /node_modules/,
      },
    ],
  },
};

module.exports = config;
