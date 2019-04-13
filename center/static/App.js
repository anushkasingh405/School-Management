import React, { Component } from 'react';
import './App.css';

class App extends Component {

  render() {
    return (

       <form method="post" >
          <div className="signupform">
              <input name="name" placeholder="Username" />
          </div>
  
   	  <div className="signupform">
              <input  name="Password" placeholder="Password"/>
   	  </div>
  
         <input className="button"  type="submit" value="Submit"/>
      </form>
    
    );
  }
}

export default App;
