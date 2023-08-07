import React from "react";
import { useNavigate } from "react-router-dom";

function Logout ({setUser}) {

    function handleLogout() {
        fetch("/logout", {
            method: "DELETE"
        }).then(setUser(null))
        handleNavigation()
    }

    const navigate = useNavigate();
    //Navigates to home
    function handleNavigation(){
        navigate(`/`)
    }



    return (
        <div>
            <div className='logout-container'>
            <button onClick={handleLogout}>Logout</button>
            </div>

        </div>
    )
}

export default Logout