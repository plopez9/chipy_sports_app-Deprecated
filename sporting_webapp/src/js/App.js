import React, { Component } from "react";

import "./App.css";
import  FirstPlot from "./components/Scatter";


class App extends Component {
  render(){
    return(
      <div className="App">
        <div className="App-header">
          <button size= "lg" block="True"> This is My First Graph </button>
        </div>
        <FirstPlot />
      </div>
    );
  }
}

export default App
