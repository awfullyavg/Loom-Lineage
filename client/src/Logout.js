import React from "react";

function Logout ({setUser}) {


    function handleLogout() {
        fetch("/logout", {
            method: "DELETE"
        }).then(setUser(null))
    }


    return (
        <div>
            <div className='logout-container'>
            <button>Logout</button>
            </div>

        </div>
    )
}

export default Logout