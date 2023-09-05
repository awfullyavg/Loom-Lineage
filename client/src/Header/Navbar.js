import React from "react";
import ReactDOM  from "react-dom";
import Logo from "./Logo";
import { Link } from "react-router-dom";
import { useState, useContext } from "react";
import {UserContext} from '../App';
import Modal from 'react-modal';

function Navbar () {
    const myStyle = {height: '64px'}
    const user = useContext(UserContext)

    return (
        <nav class="relative flex w-full flex-wrap items-center justify-between py-2 shadow-lg text-slate-500 hover:text-neutral-700 focus:text-neutral-700 bg-Ash-Gray lg:py-4">
        <div class="flex w-full flex-wrap items-center justify-between px-3">
            <div>
            <a class="mx-2 my-1 flex items-center text-neutral-900 hover:text-neutral-900 focus:text-neutral-900 lg:mb-0 lg:mt-0" href="#">
            <Link to='/' ><img
                class="mr-2"
                src="https://i.imgur.com/32wqxFa.png"
                style={myStyle}
                alt="TE Logo"
                loading="lazy" /></Link>
                <Link to='/' className="font-medium dark:text-neutral-200">Loom Lineage</Link>
            </a>
            </div>

            <div>
                <Link to="/login" className="login">Login</Link><br></br>
                <Link to="/signup" className="sign-up">Signup</Link><br></br>
                <Link to='/profile' className="profile">Profile</Link>
                <div>
                    <h2>{`Welcome back, ${user}!`}</h2>
                </div>
            </div>
        </div>
        </nav>
        );
      }
export default Navbar