import React from 'react';
import firebase from 'firebase';
import Redirect from 'react-router-dom';

class Home extends React.Component{
    constructor(props){
        super(props);
        console.log(props);
        console.log("AUTH INFO");
        console.log(firebase.auth().currentUser);

        this.state = {
            userLoggedIn: window.localStorage.getItem('userLoggedIn'),
            user: window.localStorage.getItem('userDisplayName')
        }
    }


    render(){
        return(
            <div>
                <h1>Home</h1>
                <p>A user is logged in to Gigz: {this.state.userLoggedIn}</p>
                <p>Welcome: {this.state.user}</p>
            </div>
        )
    }
}

export default Home;