import React, {useState, useEffect} from 'react';
import './App.css';
import {BrowserRouter, Routes, Route} from "react-router-dom";
import Home from './Home/Home';
import Navbar from './Header/Navbar';

function App() {
  return (
    <div className="main">
      <nav className='navbar-container'>
        <Navbar />
      </nav>

      <div>
        <Routes>
          <Route path='/' element={<Home />} />
        </Routes>
      </div>



    </div>
  );
}

export default App;
