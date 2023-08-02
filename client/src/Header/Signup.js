import React from "react";
import { useEffect, useState } from "react";


function Signup () {
    const [user, setUser] = useState([])
    const [fname, setFname] = useState('')
    const [lname, setLname] = useState('')
    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')

    useEffect(() => {
        fetch("/users")
        .then(resp => resp.json())
        .then(data => setUser(data))
    }, [])

    const handleSubmit = () => {
        //e.preventDefault()

        const new_user = {
            fname: fname,
            lname: lname,
            email: email,
            password: password
        }
    }



    return (
        <div className="signup">
            <h1>Start to track your Lineage now!</h1><br></br>
            <form>
                <label>First Name: </label><br></br>
                <input type="text" placeholder="Enter First Name"></input><br></br>
                <label>Last Name: </label><br></br>
                <input type="text" placeholder="Enter Last Name"></input><br></br>
                <label>Email: </label><br></br>
                <input type="text" placeholder="Enter Email"></input><br></br>
                <label>Password: </label><br></br>
                <input type="password" placeholder="Enter Password"></input><br></br>
                <br></br>
                <button className='bg-Chinese-Violet text-white'>Submit</button>
            </form>

        </div>
    )
}

export default Signup