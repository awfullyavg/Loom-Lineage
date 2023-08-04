import React, {useState, useEffect} from 'react';
import Home from './Home/Home';
import Header from './Header/Header';
import Signup from './Header/Signup';
import LoginForm from './Header/LoginForm';
import {BrowserRouter, Routes, Route} from "react-router-dom";
import './index.css';


function App() {
  const [user, setUser] = useState(null) //This is an empty user initially

  return (
    <div className='main'>
      <div>
        <Header />
      </div>
      <div>
        <Routes>
          <Route path='/' element={<Home />}></Route>
          <Route path='/signup' element={<Signup user={user} />}></Route>
          <Route path='/login' element={<LoginForm setUser={setUser}/>}/>
        </Routes>
      </div>



    </div>
  );
}

export default App;
