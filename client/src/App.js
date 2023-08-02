import React, {useState, useEffect} from 'react';
import Home from './Home/Home';
import Header from './Header/Header';
import Signup from './Header/Signup';
import {BrowserRouter, Routes, Route} from "react-router-dom";
import './index.css';


function App() {
  return (
    <div className='main'>
      <div>
        <Header />
      </div>
      <div>
        <Routes>
          <Route path='/' element={<Home />}></Route>
          <Route path='/signup' element={<Signup />}></Route>
          
        </Routes>
      </div>



    </div>
  );
}

export default App;
