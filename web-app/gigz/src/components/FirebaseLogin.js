// Import FirebaseAuth and firebase.
import React from 'react';
import StyledFirebaseAuth from 'react-firebaseui/StyledFirebaseAuth';
import firebase from 'firebase';
import auth from 'firebase/auth';
import Redirect from 'react-router-dom';
import Login from './Login';
import firebaseui from 'react-firebaseui';


class FirebaseLogin extends React.Component {

    constructor(props){
        super(props);
    }

    redirectHome(){
        window.location.href = "/";
    }
    
    loginUser(user){
        window.localStorage.setItem('userLoggedIn','true');
        window.localStorage.setItem('userDisplayName', user.displayName);
        window.localStorage.setItem('userToken', user.token);
    }

    logoutUser(){
        window.localStorage.setItem('userLoggedIn','false');
        window.localStorage.setItem('userDisplayName', null);
        window.localStorage.setItem('userToken', null);
    }
    
  render() {

        // Configure FirebaseUI.
        const uiConfig = {
            // Popup signin flow rather than redirect flow.
            signInFlow: 'popup',
            // Redirect to /signedIn after sign in is successful. Alternatively you can provide a callbacks.signInSuccess function.
            signInSuccessUrl: '/home',
            // We will display Google and Facebook as auth providers.
            signInOptions: [
            firebase.auth.GoogleAuthProvider.PROVIDER_ID,
            firebase.auth.TwitterAuthProvider.PROVIDER_ID,
            firebase.auth.EmailAuthProvider.PROVIDER_ID,
            ],
            callbacks : {
            signInSuccessWithAuthResult: (authResult, redirectUrl) => {
                console.log('signInSuccessWithAuthResult', authResult, redirectUrl);
                var user = {
                    displayName : authResult.user.displayName,
                    token : null,
                }
                this.loginUser(user);
                this.redirectHome();
                }
            },
            signInFailure(error){
                console.log("Some shit went wrong");
                console.log(error);
            }
        };
    return (
      <div>
        <h1>Gigz</h1>
        <p>Please login:</p>
        <StyledFirebaseAuth uiConfig={uiConfig} firebaseAuth={firebase.auth()}/>
      </div>
    );
  }
}

export default FirebaseLogin;