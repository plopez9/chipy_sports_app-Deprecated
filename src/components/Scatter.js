import React, { Component } from "react";
import Plot from "react-plotly.js"


class FirstPlot extends Component{

  constructor(){
    super();
    this.state={
      x_series:[],
      y_series:[],
      pk:[],
    };
  }

  componentDidMount(){
    fetch("http://127.0.0.1:8000/nba_package/jsonSummary/?format=json")
    .then(results => {
      return results.json();
    })
  }

  render(){
    return(
      <Plot
        data={[
          {
            x: [1, 2, 3, 4, 5],
            y: [2, 6, 3, 4, 2],
            type: "bar",
            mode: "markers",
            marker: {color: "blue"},
          }
        ]}
      />
    );
  }
}


export default FirstPlot;
