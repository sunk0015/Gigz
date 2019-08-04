import React from 'react';
import {Button} from 'reactstrap';
import {
    BrowserRouter as Router,
    Route,
  } from 'react-router-dom';

import './_Login.scss';
import { TwitterLoginButton, GoogleLoginButton, FacebookLoginButton } from "react-social-login-buttons";
import FirebaseLogin from './FirebaseLogin';

class Login extends React.Component{

    render(){
        return(
            <FirebaseLogin/>

          )
      }
  }

  export default Login;