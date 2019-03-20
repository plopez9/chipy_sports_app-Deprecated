import React, { Component } from "react";
import ListsItem from "./ListsItem";
import PropTypes from "prop-types";


class Lists extends Component {
  render(){
    console.log(this.props.lists)
    return this.props.lists.map((item) => (
      <ListsItem key={item.id} lists={item} />
    ));
  }
}

Lists.propTypes = {
  lists: PropTypes.array.isRequired
}

export default Lists;
