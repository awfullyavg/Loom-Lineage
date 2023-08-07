import React from "react";
import { useState, useEffect } from "react";
import Loom from "./Loom";
import { Link } from "react-router-dom";
import Logout from "./Logout";


function UserProfile ({user, setUser}) {
// Need to make the following:
// 1. Create a loom (Need a form. GET, POST, DELETE)
// 2. Show Loom created. 
// 3. Able to click the loom and create a family
// 4. Need to make a family componnet and put family form in there

console.log(user)
    return (
        <div>
            
{/* --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- */}
            <div className="loom-container">
                <Loom />
            </div><br></br>

            <div>
                <h1>Family Form</h1>
                <Link to='/familyform'>Add a family</Link>
            </div><br></br>

            <div>
                <Link to='/loom'>Create a loom!</Link>
            </div><br></br>

            <div className='logout-container'>
            <Logout setUser={setUser} />
            </div>

        </div>
    )
}

export default UserProfile