import React, { Component } from "react";
import PropTypes from "prop-types";


class ListsItem extends Component {
  render(){
    return (
      <div>
        <p> {this.props.lists.title} </p>
      </div>
    )
  }
}

ListsItem.propTypes = {
  lists: PropTypes.object.isRequired
}

export default ListsItem;
