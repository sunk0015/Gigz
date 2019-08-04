import React from 'react';
import './_Navbar.scss';

class Navbar extends React.Component{
    render(){
        return(
            <div className="navbar-container">
                <nav className="navbar navbar-expand-lg bg-info">
                <div className="container">
                    <a className="navbar-brand" href="#">Gigz</a>
                    <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
                    <span className="navbar-toggler-icon"></span>
                    </button>
                    <div className="collapse navbar-collapse" id="navbarNavDropdown">
                    <ul className="navbar-nav">
                        <li className="nav-item active">
                        <a className="nav-link" href="/hire">Hire <span className="sr-only">(current)</span></a>
                        </li>
                        <li className="nav-item">
                        <a className="nav-link" href="/work">Work</a>
                        </li>
                        <li className="nav-item">
                        <a className="nav-link" href="/">Widgets</a>
                        </li>
                        <li className="nav-item">
                        <a className="nav-link" href="/login">Account</a>
                        </li>
                    </ul>
                    </div>
                </div>
                </nav>
            </div>

        )
    }
}

export default Navbar;