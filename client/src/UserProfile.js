import React from "react";
import { useState, useEffect } from "react";
import Logout from "./Logout";


function UserProfile ({user, setUser}) {
// Need to make the following:
// 1. Create a loom (Need a form. GET, POST, DELETE)
// 2. Show Loom created. 
// 3. Able to click the loom and create a family
//
const [families, setFamilies] = useState([])
const [name, setName] = useState('')
const [mother, setMother] = useState('')
const [father, setFather] = useState('')
const [partner, setPartner] = useState('')
const [children, setChildren] = useState('')

useEffect(() => {
    fetch("/families")
    .then(resp => resp.json())
    .then(data => setFamilies(data))
}, [])

const handleSubmit = () => {
    // e.preventDefault()

    const new_family = {
        name: name,
        mother: mother,
        father: father,
        partner: partner,
        children: children
    }

    fetch('/families', {
        method: 'POST',
        headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
        },
        body : JSON.stringify(new_family)
    })
    .then(resp => resp.json())
    .then(new_family => setFamilies([...families, new_family]))
}


    return (
        <div>
            <div className="loom-form">
                <form onSubmit={handleSubmit}>
                <label>Enter your family's last name: </label><br></br>
                <input type="text" placeholder="What do we call your family?" onChange={(e) => setName(e.target.value)} value={name}></input><br></br>
                <label>Enter your Mother's name: </label><br></br>
                <input type="text" placeholder="Mother's Name" onChange={(e) => setMother(e.target.value)} value={mother}></input><br></br>
                <label>Enter your Father's name: </label><br></br>
                <input type="text" placeholder="Father's Name" onChange={(e) => setFather(e.target.value)} value={father}></input><br></br>
                <label>Enter your Partner's name: </label><br></br>
                <input type="text" placeholder="Partner's Name" onChange={(e) => setPartner(e.target.value)} value={partner}></input><br></br>
                <label>Child's name </label><br></br>
                <input type="text" onChange={(e) => setChildren(e.target.value)} value={children} /><br></br>
                <button className='bg-Chinese-Violet text-white'>Submit</button>
                </form>
            </div>

            <div className='logout-container'>
            <Logout />
            </div>

        </div>
    )
}

export default UserProfile