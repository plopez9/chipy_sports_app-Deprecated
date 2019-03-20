import React, { Component } from "react";
import Lists from "./components/Lists";

import "./App.css";

class App extends Component {
  state={
    lists: [
      {
        id: 1,
        title: "Player Profiles"
      },
      {
        id: 2,
        title: "Contracts"
      },
      {
        id: 3,
        title: "Summary Stats"
      }
    ]
  }
  render(){
    console.log(this.state.lists)
    return (
      <div className="App">
        < Lists lists={this.state.lists} />
      </div>
    );
  }
}

export default App;
