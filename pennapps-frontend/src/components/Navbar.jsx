import React from "react";
import{BrowserRouter,Route,Link} from "react-router-dom";
import "../css/Navbar.css";


function Navbar(){
    return(
    <div class="navbar">
        
        <div class="menubutton">
            <nav class="nav">
                <ul>
                    <li>
                        <a href="/">Home</a>
                    </li>
                    <li>
                        <a href="/about">About</a>
                    </li>
                    <li>
                        <a href="/demo">Demo</a>
                    </li>
                </ul>
            </nav>
        </div>
        
    </div>
    


    

    );
}

export default Navbar;