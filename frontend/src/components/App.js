import React, {Component} from 'react';
import ReactDOM from 'react-dom';
import Headers from './Headers';
//var Router=require('./Routers');

class App extends Component{
    render(){
        
        return <Headers />
    }
}
ReactDOM.render(<App />, document.getElementById('app') );



