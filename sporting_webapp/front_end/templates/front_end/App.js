import React, { Component } from "react";
import Plot from "react-plotly.js";

import "./App.css";


class App extends Component {
  render(){
    return(
      <div className="App">
        <div className="App-header">
          <button size= "lg" block="True"> This is My First Graph </button>
        </div>
      </div>
    );
  }
}

export default App
