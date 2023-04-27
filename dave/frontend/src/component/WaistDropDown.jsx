import axios from 'axios'
import React from 'react';
import "./Measure.css";
import Dropdown from 'react-bootstrap/Dropdown';
function WaistDropDown(props) {
  
  const waist = props.waist
  console.log("props" , props)
  function clicked(x)
  {
      console.log("clicked",x.data)
      props.changeWaist(x.data)
  }
  return (
   
    <div className="col-lg-2 waistcol2 col-md-2 col-sm-1">
       
        <Dropdown>
        <Dropdown.Toggle variant="success" id="dropdown-basic" class="tooglebtn">
        Waist
      </Dropdown.Toggle>


      <Dropdown.Menu>
      {(waist).map((data,index) => (
        
        <Dropdown.Item href="#/action-1" key={data} onClick={()=>clicked({data})}>{data}</Dropdown.Item>
        ))}

        </Dropdown.Menu>
    </Dropdown>
       
    </div>
  );
}

export default WaistDropDown;
