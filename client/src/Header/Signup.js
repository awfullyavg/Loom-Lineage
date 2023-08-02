import React from "react";
import { useEffect, useState } from "react";


function Signup () {
    const [users, setUsers] = useState([])
    const [fname, setFname] = useState('')
    const [lname, setLname] = useState('')
    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')

    useEffect(() => {
        fetch("/users")
        .then(resp => resp.json())
        .then(data => setUsers(data))
    }, [])

    const handleSubmit = () => {
        // e.preventDefault()

        const new_user = {
            fname: fname,
            lname: lname,
            email: email,
            password: password
        }

        fetch('/users', {
            method: 'POST',
            headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
            },
            body : JSON.stringify(new_user)
        })
        .then(resp => resp.json())
        .then(new_user => setUsers([...users, new_user]))


    }



    return (
        <div className="signup">
            <h1>Start to track your Lineage now!</h1><br></br>
            <form onSubmit={handleSubmit}>
                <label>First Name: </label><br></br>
                <input type="text" placeholder="Enter First Name" onChange={(e) => setFname(e.target.value)} value={fname}></input><br></br>
                <label>Last Name: </label><br></br>
                <input type="text" placeholder="Enter Last Name" onChange={(e) => setLname(e.target.value)} value={lname}></input><br></br>
                <label>Email: </label><br></br>
                <input type="text" placeholder="Enter Email" onChange={(e) => setEmail(e.target.value)} value={email}></input><br></br>
                <label>Password: </label><br></br>
                <input type="text" placeholder="Enter Password" onChange={(e) => (e.target.value)} ></input><br></br>
                <br></br>
                <button className='bg-Chinese-Violet text-white'>Submit</button>
            </form>

        </div>
    )
}

export default Signup