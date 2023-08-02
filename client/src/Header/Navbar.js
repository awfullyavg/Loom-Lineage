import React from "react";
import ReactDOM  from "react-dom";
import Logo from "./Logo";
import { NavLink } from "react-router-dom";
import { useState } from "react";
import Modal from 'react-modal';

function Navbar () {
    const [open, setOpen] = useState(false);
    const myStyle = {height: '64px'}

    const handleOpen = () => { //Opens Modal when login button clicked
        setOpen(true)
    }

    const handleClose = () => { //Closes Modal when cliked anywhere outside the modal
        setOpen(false)
    }

    return (
        <nav class="relative flex w-full flex-wrap items-center justify-between bg-Ash-Gray py-2 text-neutral-500 shadow-lg hover:text-neutral-700 focus:text-neutral-700 dark:bg-neutral-600 lg:py-4">
        <div class="flex w-full flex-wrap items-center justify-between px-3">
            <div>
            <a class="mx-2 my-1 flex items-center text-neutral-900 hover:text-neutral-900 focus:text-neutral-900 lg:mb-0 lg:mt-0" href="#">
                <img
                class="mr-2"
                src="https://i.imgur.com/32wqxFa.png"
                style={myStyle}
                alt="TE Logo"
                loading="lazy" />
                <span class="font-medium dark:text-neutral-200">Loom Lineage</span>
            </a>
            </div>

            <div>
                <button className="login-button" onClick={handleOpen}>Login</button>
                <Modal isOpen={open} onRequestClose={handleClose} contentLabel="Login" >
                    <h1>Please Login</h1>
                    <div>

                    </div>

                </Modal>
                
            </div>
            
        </div>
        </nav>

        );
      }
export default Navbar