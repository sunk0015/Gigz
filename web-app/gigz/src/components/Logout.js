import React from 'react';



class Logout extends React.Component{

    logoutUser(){
        window.localStorage.setItem('userLoggedIn','false');
        window.localStorage.setItem('userDisplayName', null);
        window.localStorage.setItem('userToken', null);
    }
    

    constructor(props){
        super(props);
        this.logoutUser();
        window.location.href = '/';
    }

    
    render(){
        return(
            <h1>You are being logged out.</h1>
        )
    }
}

export default Logout;