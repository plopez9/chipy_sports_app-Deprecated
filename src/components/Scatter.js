import React, { Component } from "react";
import Plot from "react-plotly.js"

//import axios from "axios";


class FirstPlot extends Component{

  constructor(props){
    super(props);
    this.state={
      items:[],
      isLoaded: "False",
    };
  }

  componentDidMount(){
    fetch("/nba_package/jsonContracts/?format=json")
    .then(res => res.json())
    .then(json => {
      this.setState({
        isLoaded: true,
        items: json,
      })
    });
  }

  render(){
    var {isLoaded, items} = this.state;

    if (!isLoaded){
      return <div> Loading ... </div>
    }

    else{
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
      )
    }


  }
}


export default FirstPlot;
