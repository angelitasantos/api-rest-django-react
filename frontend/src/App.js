import './App.css';
import React, { Component } from "react";
import { render } from "react-dom";


class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
    };
  }

  componentDidMount() {
    fetch("contacts")
      .then(response => {
        return response.json();
      })
      .then(data => {
        this.setState(() => {
          return {
            data,
            loaded: true
          };
        });
      });
  }

  render() {
    return (
     <div>
        {this.state.data.map(contacts => {
          return (
            <div>
              <table>
                <thead>
                  <tr>
                    <th scope="col">First Name</th>
                    <th scope="col">Last Name</th>
                    <th scope="col">Phone</th>
                    <th scope="col">Email</th>
                    <th scope="col">State</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>{contacts.first_name}</td>
                    <td>{contacts.last_name}</td>
                    <td>{contacts.phone}</td>
                    <td>{contacts.email}</td>
                    <td>{contacts.state}</td>
                  </tr>
                </tbody>
              </table>
            </div>
          );
        })}
      </div>
    );
  }
}

export default App;

const container = document.getElementById("root");
render(<App />, container);