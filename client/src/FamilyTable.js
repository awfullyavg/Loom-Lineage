import React from "react";
import FamilyTree from "./FamilyTree";
import { Link } from "react-router-dom";
import { useEffect, useState } from "react";



function FamilyTable({ user, setUser }) {
    const [families, setFamilies] = useState([]);
    // const [newFamily, setNewFamily] = useState({id: null,
    // name:null})
    const [isEditFormVisible, setIsEditFormVisible] = useState(false);
    const [isDeleteFormVisible, setIsDeleteFormVisible] = useState(false);


    useEffect(() => {
      fetch("/check_session").then((response) => {
        if (response.ok) {
          response.json().then((user) => setUser(user));
        }
      });
    }, []);
  
    useEffect(() => {
      fetch("/families")
        .then(resp => resp.json())
        .then(data => setFamilies(data));
    }, []);



    const userFamilies = families.filter((family) => family.user_id == user.id);
 




    function handleSubmit (e) {
      e.preventDefault()
      // console.log(e.target.id.value)
      // console.log(e.target.name.value)
      // console.log(e.target.father.value)
      // console.log(e.target.mother.value)
      // console.log(e.target.partner.value)
      // console.log(e.target.children.value)

      const familyId = e.target.id.value

      const newFamily = {
        id: familyId,
        name: e.target.name.value,
        mother: e.target.mother.value,
        father: e.target.father.value,
        partner: e.target.partner.value,
        children: e.target.children.value
      }
      fetch(`/family/${newFamily.id}`, {
        method: "PATCH",
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
      },
      body: JSON.stringify(newFamily)
    })
    .then(resp => resp.json())
    .then((patchedFamily) => newFamily)

    alert('Family has been patched')
  }

  function handleDelete(e) {
    e.preventDefault()
    const familyId = e.target.querySelector('#delete-form').value
    const deletedFamily = {
      id: familyId
    }
 
    fetch(`/family/${deletedFamily.id}`, {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json'
      },
    })
    alert('Family has been deleted :(')
    
  }
  const toggleEditForm = () => {
    setIsEditFormVisible(!isEditFormVisible);
    console.log('clicked')
  };
  const toggleDeleteForm = () => {
    setIsDeleteFormVisible(!isDeleteFormVisible);
    console.log('clicked')
  };


    return (
      <div>
        <FamilyTree userFamilies={userFamilies} />
      <div className="flex flex-col">
        <div className="overflow-x-auto">
          <div className="p-1.5 w-full inline-block align-middle">
            <div className="overflow-hidden border rounded-lg">
              <table className="min-w-full divide-y divide-gray-200">
                <thead className="bg-gray-50">
                  <tr>
                    <th
                      scope="col"
                      className="px-6 py-3 text-xs font-bold text-left text-gray-500 uppercase"
                    >
                      ID
                    </th>
                    <th
                      scope="col"
                      className="px-6 py-3 text-xs font-bold text-left text-gray-500 uppercase"
                    >
                      Name
                    </th>
                    <th
                      scope="col"
                      className="px-6 py-3 text-xs font-bold text-left text-gray-500 uppercase"
                    >
                      Father
                    </th>
                    <th
                      scope="col"
                      className="px-6 py-3 text-xs font-bold text-left text-gray-500 uppercase"
                    >
                      Mother
                    </th>
                    <th
                      scope="col"
                      className="px-6 py-3 text-xs font-bold text-left text-gray-500 uppercase"
                    >
                      Partner
                    </th>
                    <th
                      scope="col"
                      className="px-6 py-3 text-xs font-bold text-left text-gray-500 uppercase"
                    >
                      Children
                    </th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-gray-200">
                  {userFamilies.map((family) => (
                    <tr key={family.id}>
                      <td className="px-6 py-4 text-sm font-medium text-gray-800 whitespace-nowrap">
                        {family.id}
                      </td>
                      <td className="px-6 py-4 text-sm text-gray-800 whitespace-nowrap">
                        {family.name}
                      </td>
                      <td className="px-6 py-4 text-sm text-gray-800 whitespace-nowrap">
                        {family.father}
                      </td>
                      <td className="px-6 py-4 text-sm text-gray-800 whitespace-nowrap">
                        {family.mother}
                      </td>
                      <td className="px-6 py-4 text-sm text-gray-800 whitespace-nowrap">
                        {family.partner}
                      </td>
                      <td className="px-6 py-4 text-sm text-gray-800 whitespace-nowrap">
                        {family.children}
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
            <div>
                <button id='edit-loom-button' onClick={toggleEditForm}>Edit Loom</button>
              </div>
              {isEditFormVisible && (
            <div>
              <form onSubmit={handleSubmit} id='edit-loom'>
                <div>
                  <label>Family ID</label>
                  <input id='id' type="text" /> 
                </div>
                <div>
                  <label>Family Name</label>
                  <input id='name' type="text" />
                </div><br></br>
                <div>
                  <label>Father</label>
                  <input id='father' type="text"  />
                </div><br></br>
                <div>
                  <label>Mother</label>
                  <input id='mother' type="text"  />
                </div><br></br>
                <div>
                  <label>Partner</label>
                  <input id='partner' type="text"  />
                </div><br></br>
                <div>
                  <label>Children</label>
                  <textarea id="children" type="text" />
                </div><br></br>
                <div>
                  <button>Save Changes</button>
                </div>
              </form>
            </div>
              )}
            <div>
                <Link to='/familyform'>Add a family</Link>
            </div>
            <div>
              <button onClick={toggleDeleteForm}>Delete A Family</button>
              {isDeleteFormVisible && (
              <div>
                <form onSubmit={handleDelete}>
                  <label>Enter ID of the row you wish to delete</label>
                  <input type="text" id="delete-form"  />
                  <button>Save Changes</button>
                </form>
              </div>
              )}
            </div>
          </div>
        </div>
      </div>
      </div>
    );
  }
  
  export default FamilyTable;
  