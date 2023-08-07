import React from "react";
import FamilyForm from "./FamilyForm";
import FamilyTree from "./FamilyTree";
import FamilyTable from "./FamilyTable";
import { useEffect } from "react";
//This is where the d3 family tree would go
function Loom () {
    return (
        <div>
            {/* Want to display the family tree above the table */}
    
            <h1>This is a Loom</h1>

            <FamilyTable />


        </div>
    )
}

export default Loom