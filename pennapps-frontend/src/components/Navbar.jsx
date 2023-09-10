import React from "react";
import{BrowserRouter,Route,Link} from "react-router-dom";
import "../css/Navbar.css";
import "../css/Home.css";


function Navbar(){
    return(
    <div class="navbar">

        <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter&display=swap');
        </style>
        
        <div class="menubutton">
            <nav class="navMenu">
                <ul class = "navUL">
                    <li>
                        <a href="/">Home</a>
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