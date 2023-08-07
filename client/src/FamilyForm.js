import React from "react";
import { useState, useEffect } from "react";
import {useFormik} from "formik";
import { object, string, number} from 'yup';
import {useNavigate} from 'react-router-dom';
import Logout from "./Logout";


function FamilyForm ({user}) {

// const [families, setFamilies] = useState([])
// const [name, setName] = useState('')
// const [mother, setMother] = useState('')
// const [father, setFather] = useState('')
// const [partner, setPartner] = useState('')
// const [children, setChildren] = useState('')

// useEffect(() => {
//     fetch("/families")
//     .then(resp => resp.json())
//     .then(data => setFamilies(data))
// }, [])

// const handleSubmit = () => {
//     // e.preventDefault()

//     const new_family = {
//         name: name,
//         mother: mother,
//         father: father,
//         partner: partner,
//         children: children
//     }

//     fetch('/families', {
//         method: 'POST',
//         headers: {
//         'Accept': 'application/json',
//         'Content-Type': 'application/json'
//         },
//         body : JSON.stringify(new_family)
//     })
//     .then(resp => resp.json())
//     .then(new_family => setFamilies([...families, new_family]))
// }

const [error, setError] = useState() 
const navigate = useNavigate()

const [families, setFamilies] = useState([])

useEffect(() => {
    fetch("/families")
    .then(resp => resp.json())
    .then(data => setFamilies(data))
}, [])

useEffect(() => {
    if (user && user.id){
    formik.setValues({
      user_id: user.id
    })
}
  }, [user])

console.log(user)

const formSchema = object({
    name: string().required('Name must be atleast 2 characters long'),

})

const formik = useFormik({
    initialValues: {
        name: '',
        mother: '',
        father: '',
        partner: '',
        children: '',
        user_id: ''
    },
    validationSchema: formSchema,
    onSubmit: (values) =>{
        fetch('/families' , {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(values)
        })
        .then(res => {
            if (res.ok){
                res.json().then(new_family => {
                    setFamilies([...families, new_family])
                    console.log(new_family)
                })
            } else {
                res.json().then(error => setError(error)) //for backend errors
            }
        })
    }
})


    return (
        <div>
            <div className="loom-form">
            <form onSubmit={formik.handleSubmit}>

<div className="family-name">
    <label> Enter family name</label>
    <input
    type="text"
    name="name"
    value={formik.values.name}
    onChange={formik.handleChange}
    />
</div>

<div className="mother-name">
    <label> Enter mothers name </label>
    <input
    type="text"
    name="mother"
    value={formik.values.mother}
    onChange={formik.handleChange}
    />
</div>

<div className="father-name">
    <label> Enter Fathers name</label>
    <input
    type="text"
    name="father"
    value={formik.values.father}
    onChange={formik.handleChange}
    />
</div>

<div className="partner-name">
    <label> Enter Partners name </label>
    <input
    type="text"
    name="partner"
    value={formik.values.partner}
    onChange={formik.handleChange}
    />
</div>

<div className="children-name">
    <label> Enter Childrens name </label>
    <textarea
    type="text"
    name="children"
    value={formik.values.children}
    onChange={formik.handleChange}
    />
</div>
<button type="submit" className="" > Submit my entry! </button>
</form>
            </div>
        </div>
    )
}

export default FamilyForm