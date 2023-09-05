import React from "react";
import Navbar from "./Navbar";



function Header ({user}) {

    return (
        <div>
            <div className='navbar-container'>
                <Navbar userCheck={user} />
            </div>

        </div>
    )
}

export default Header