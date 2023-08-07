import React, {useState, useEffect} from 'react';
import Home from './Home/Home';
import Header from './Header/Header';
import Signup from './Header/Signup';
import LoginForm from './Header/LoginForm';
import UserProfile from './UserProfile';
import Loom from './Loom';
import FamilyForm from './FamilyForm';
import {BrowserRouter, Routes, Route} from "react-router-dom";
import './index.css';
import FamilyTree from './FamilyTree';
import FamilyTable from './FamilyTable';


function App() {
  const [user, setUser] = useState(null) //This is an empty user initially

  useEffect(() => {
    fetch("/check_session").then((response) => {
      if (response.ok) {
        response.json().then((user) => setUser(user));
      }
    });
  }, []);

  console.log(user)

  return (
    <div className='main'>
      <div>
        <Header />
      </div>
      <div>
        <Routes>
          <Route path='/' element={<Home />}></Route>
          <Route path='/signup' element={<Signup loginUser={user} setLogin={setUser} />}></Route>
          <Route path='/login' element={<LoginForm user={user} setUser={setUser}/>}/>
          <Route path='/profile' element={<UserProfile user={user} setUser={setUser} />} />
          <Route path='/loom' element={<Loom user={user} setUser={setUser} />} />
          <Route path='/familyform' element={<FamilyForm user={user}/>} />
          {/* <Route path='/familytree' element={<FamilyTree />} /> */}
          <Route path='/familytable' element={<FamilyTable user={user} />} />
        </Routes>
      </div>



    </div>
  );
}

export default App;
