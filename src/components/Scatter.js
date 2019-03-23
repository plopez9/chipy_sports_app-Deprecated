import React, { Component } from "react";
import Plot from "react-plotly.js"


class FirstPlot extends Component{
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
