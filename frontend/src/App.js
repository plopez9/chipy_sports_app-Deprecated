import React, { Component } from "react";

import "./App.css";
import  FirstPlot from "./components/Scatter";


class App extends Component {
  render(){
    return(
      <div className="App">
        <FirstPlot />
      </div>
    );
  }
}

export default App
