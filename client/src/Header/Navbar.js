import React from "react";
import Logo from "./Logo";
import { NavLink } from "react-router-dom";

function Navbar () {

    const myStyle = {height: '64px'}

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
        </div>
        </nav>

        );
      }
export default Navbar