import React from "react"
import { Link, useNavigate } from "react-router-dom"

function LoginForm({user, setUser}){

    const navigate = useNavigate();

    console.log(user)

    //Basic login functionality. Send them back to the homepage or dashboard
    function handleLogin(e) {
        e.preventDefault();

        let username = e.target.username.value;
        let password = e.target.password.value;

        fetch("/login", {
            method: "POST",
            headers: {
            "Content-Type": "application/json",
            },
            body: JSON.stringify( { username, password } )
        }).then((resp) => {
            if (resp.ok) {
            resp.json().then((user) => {
                setUser(user)
                handleNavigation(user)
            }); // <-------- navigates to the dashboard
        }
        });
}


    //Navigation back to homepage or dashboard

    function handleNavigation(user){
        navigate(`/profile`)
    }

    return(
    <>
<div className="min-h-screen flex items-center justify-center bg-Nyanza">
      <div className=" bg-slate-50 p-8 rounded shadow-md w-96">
        <h1 className="text-2xl font-semibold mb-4">Login Form</h1>
        <form onSubmit={handleLogin}>
          <div className="mb-4">
            <label htmlFor="username" className="block text-sm font-medium text-gray-700">
              Username:
            </label>
            <input
              id="username"
              type="text"
              className="mt-1 p-2 block w-full border rounded focus:ring-indigo-500 focus:border-indigo-500"
            />
          </div>
          <div className="mb-4">
            <label htmlFor="password" className="block text-sm font-medium text-gray-700">
              Password:
            </label>
            <input
              id="password"
              type="password"
              className="mt-1 p-2 block w-full border rounded focus:ring-indigo-500 focus:border-indigo-500"
            />
          </div>
          <button
            type="submit"
            className="w-full bg-indigo-600 text-white py-2 px-4 rounded-md hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
          >
            Login
          </button>
        </form>
      </div>
    </div>
    </>
    )
}

export default LoginForm;