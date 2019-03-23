import React, { Component } from "react";
import Plot from "react-plotly.js";

import "./App.css";
import  FirstPlot from "./components/Scatter";


class App extends Component {
  constructor(){
    super();
    this.state={
      
    }
  }
  render(){
    return(
      <div className="App">
        <div className="App-header">
          <h2> This is My First Graph </h2>
        </div>
        <FirstPlot />
      </div>
    );
  }
}

export default App
