import React from 'react';
import {Button} from 'reactstrap';
import {
    BrowserRouter as Router,
    Route,
  } from 'react-router-dom';

import Login from './Login.js';
import './_Page.scss';
import Navbar from './Navbar.js';
import Hire from './Hire';
import Work from './Work';
import Home from './Home';
import Logout from './Logout';
class Page extends React.Component{
    render(){
        return(
        <div className="row">
            <div className="navbar-container">
                <Navbar/>
            </div>
            <div className="content-container">
            <Route exact path="/" component={Home} /> 
            <Route exact path="/login" component={Login} />
            <Route exact path="/logout" component={Logout} />
            <Route exact path="/hire" component={Hire} />
            <Route exact path="/work" component={Work} />
            </div>
        </div>
        )
    }
}

class WidgetDiv extends React.Component{
    render(){
        return(
            <div className="container">
                <h1>Gigz</h1>
                <button type="button" class="btn btn-primary">Primary</button>
                <button type="button" class="btn btn-info">Info</button>
                <button type="button" class="btn btn-success">Success</button>
                <button type="button" class="btn btn-danger">Danger</button>
                <button type="button" class="btn btn-warning">Warning</button>
                <button type="button" class="btn btn-default">Default</button>
            
                <h3>
                <small>Default</small>
                </h3>
                <Button className="btn-just-icon" color="twitter">
                <i className="fa fa-twitter"></i>
                </Button>
                <Button className="btn-just-icon" color="facebook">
                <i className="fa fa-facebook"></i>
                </Button>
                <Button className="btn-just-icon" color="google">
                <i className="fa fa-google-plus"></i>
                </Button>
                <Button className="btn-just-icon" color="linkedin">
                <i className="fa fa-linkedin"></i>
                </Button>
                <Button className="btn-just-icon" color="pinterest">
                <i className="fa fa-pinterest-p"></i>
                </Button>
                <Button className="btn-just-icon" color="youtube">
                <i className="fa fa-youtube"></i>
                </Button>
                <Button className="btn-just-icon" color="tumblr">
                <i className="fa fa-tumblr"></i>
                </Button>
                <Button className="btn-just-icon" color="github">
                <i className="fa fa-github-alt"></i>
                </Button>
                <Button className="btn-just-icon" color="dribbble">
                <i className="fa fa-dribbble"></i>
                </Button>
                <Button className="btn-just-icon" color="reddit">
                <i className="fa fa-reddit-alien"></i>
                </Button>
                <Button className="btn-just-icon" color="instagram">
                <i className="fa fa-instagram"></i>
                </Button>
                <h3>
                <small>Bordered</small>
                </h3>
                <Button className="btn-just-icon btn-border" color="twitter">
                <i className="fa fa-twitter"></i>
                </Button>
                <Button className="btn-just-icon btn-border" color="facebook">
                <i className="fa fa-facebook"></i>
                </Button>
                <Button className="btn-just-icon btn-border" color="google">
                <i className="fa fa-google-plus"></i>
                </Button>
                <Button className="btn-just-icon btn-border" color="linkedin">
                <i className="fa fa-linkedin"></i>
                </Button>
                <Button className="btn-just-icon btn-border" color="pinterest">
                <i className="fa fa-pinterest-p"></i>
                </Button>
                <Button className="btn-just-icon btn-border" color="youtube">
                <i className="fa fa-youtube"></i>
                </Button>
                <Button className="btn-just-icon btn-border" color="tumblr">
                <i className="fa fa-tumblr"></i>
                </Button>
                <Button className="btn-just-icon btn-border" color="github">
                <i className="fa fa-github-alt"></i>
                </Button>
                <Button className="btn-just-icon btn-border" color="dribbble">
                <i className="fa fa-dribbble"></i>
                </Button>
                <Button className="btn-just-icon btn-border" color="reddit">
                <i className="fa fa-reddit-alien"></i>
                </Button>
                <Button className="btn-just-icon btn-border" color="instagram">
                <i className="fa fa-instagram"></i>
                </Button>
                <h3>
                <small>Links</small>
                </h3>
                <Button className="btn-just-icon btn-link" color="twitter">
                <i className="fa fa-twitter"></i>
                </Button>
                <Button className="btn-just-icon btn-link" color="facebook">
                <i className="fa fa-facebook"></i>
                </Button>
                <Button className="btn-just-icon btn-link" color="google">
                <i className="fa fa-google-plus"></i>
                </Button>
                <Button className="btn-just-icon btn-link" color="linkedin">
                <i className="fa fa-linkedin"></i>
                </Button>
                <Button className="btn-just-icon btn-link" color="pinterest">
                <i className="fa fa-pinterest-p"></i>
                </Button>
                <Button className="btn-just-icon btn-link" color="youtube">
                <i className="fa fa-youtube"></i>
                </Button>
                <Button className="btn-just-icon btn-link" color="tumblr">
                <i className="fa fa-tumblr"></i>
                </Button>
                <Button className="btn-just-icon btn-link" color="github">
                <i className="fa fa-github-alt"></i>
                </Button>
                <Button className="btn-just-icon btn-link" color="dribbble">
                <i className="fa fa-dribbble"></i>
                </Button>
                <Button className="btn-just-icon btn-link" color="reddit">
                <i className="fa fa-reddit-alien"></i>
                </Button>
                <Button className="btn-just-icon btn-link" color="instagram">
                <i className="fa fa-instagram"></i>
                </Button>
            
            </div>
        )
    }
}

class TwitterSuccess extends React.Component{

    constructor(props){
        console.log("Twitter success");
        alert("Twitter success");
    }
    render(){
        return(
            <div>
                <h1> Twitter successfully authenticated.</h1>
            </div>
        )
    }
}

export default Page;