import React from 'react';
import logo from './logo.svg';
import './_App.scss';
import Page from './components/Page';
import {
  BrowserRouter as Router,
  Route,
  Link,
  Switch,
  Redirect
} from 'react-router-dom';
import firebase from 'firebase';
import firebaseui from 'react-firebaseui';

class App extends React.Component{

  constructor(props){
    super(props);
    // Configure Firebase.
    const config = {
      apiKey: 'AIzaSyA5Izybt2c0ZnTKO5ZgFex3Ch8oC9ab9dQ',
      authDomain: 'gigz-1561698630505.firebaseapp.com',
      // ...
    };
    firebase.initializeApp(config);

  }

  render(){
    return (
      <Router>
        <div className="App">
          <Page/>
        </div>
      </Router>
    )
  }
}

export default App;
