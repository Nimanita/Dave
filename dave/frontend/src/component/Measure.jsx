import axios from 'axios'
import React from 'react';
import {useState } from 'react';

import "./Measure.css";

import WaistDropDown from './WaistDropDown';
function Measure() {
  const [ measure,changedata] = useState({
      height : ' ',
      weight : ' ',
      age : ' ',
      waist : [ ],
      selectedWaistValue : ' '

  })
 
  function submitclick()
  {
    console.log("inside submit")
      getMeasures()
  }
  function addWaistSize()
  {
      for(let i=0 ;i<measure.waist.length;i++)
      {
         if(measure.selectedWaistValue === measure.waist[i])
         {
           console.log("size already existed")
          
           window.alert("Size already exists")
           return
         }
      }
      addMeasures()

  }
  function changeWaist(x)
  {
    changedata(
      {
     ...measure ,
     
     selectedWaistValue : x
      }
  ) ;
   
  }
  function handleChange(e)
  {

      console.log(e.target.value);
    
      if(e.target.id ==='x1')
      {
         changedata(
             {
            ...measure ,
            height : e.target.value,
            waist : []
             }
         ) ;
          

      }
      else if(e.target.id === 'x2')
      {
        changedata(
            {
           ...measure ,
           weight : e.target.value,
           waist : []
            }
        ) ;
      }
      else if(e.target.id === 'x3')
      {
        changedata(
            {
           ...measure ,
           age : e.target.value,
           waist : []
            }
        ) ;
      }
      else if(e.target.id === 'x4')
      {
        changedata(
            {
           ...measure ,
           selectedWaistValue : e.target.value
            }
        ) ;
      }
  }
  function getMeasures() {
    
    console.log("inside getmeasures")
    const waist = []
    var config = {
    method: 'get',
    url: 'http://127.0.0.1:8000/measures',
    params: { height : measure.height,
              weight : measure.weight,
            age : measure.age }};
    console.log(config)
    axios.get("http://127.0.0.1:8000/measures" , config).then((res) => {
      console.log(res)
      console.log(res.data.data.waist)
     
      changedata(
        {
       ...measure ,
       waist : res.data.data.waist
        }
    ) ;
    });
    
 }
 function addMeasures() {
    
  console.log("inside getmeasures")
  const waist = []
  var config = {
  method: 'post',
  url: 'http://127.0.0.1:8000/measures',
  data: { height : measure.height,
            weight : measure.weight,
          age : measure.age ,
          waist : measure.selectedWaistValue}};
  console.log(config)
  axios.post("http://127.0.0.1:8000/measures" , config).then((res) => {
    console.log(res)
    window.alert(res.data["message"])
   
   
  });
  
}
  return (
   
    <div className="container App">
       
        <div class = "loginbox">
       <h1 class="heading">HEALTH PARAMETER</h1>
       <div class = "loginbox2">
       <div class = "row justify-content-center row1">
        <div class="col-lg-3">
          
            <input id="x1"  text="Email" type="text" class="form-control logininputbox" placeholder="Height" aria-label="Username" aria-describedby="basic-addon1"  onChange={handleChange} ></input>
        </div>   
        
       </div>
       <div class = "row justify-content-center row1">
        <div class="col-lg-3">
        
            <input id="x2" text="Email" type="text" class="form-control logininputbox" placeholder="Weight" aria-label="Username" aria-describedby="basic-addon1" onChange={handleChange} />
        </div>   
        </div>
        <div class = "row justify-content-center">
        <div class="col-lg-3">
        
            <input id="x3" text="Email" type="text" class="form-control logininputbox" placeholder="Age" aria-label="Username" aria-describedby="basic-addon1" onChange={handleChange} />
        </div>   
        </div>
        <div class = "row justify-content-center row1">
        <div class="col-lg-3">
        <button type="button" class="btn btn-primary submitbtn" onClick={()=>submitclick()}>GET WAIST SIZE</button>
        </div>
        </div>
        <div class = "row justify-content-center row1">
        <div class="col-lg-3 col-md-3 col-sm-2 waistcol1">
        <input id="x4" text="Email" type="text" class="form-control logininputbox" placeholder={measure.selectedWaistValue} aria-label="Username" aria-describedby="basic-addon1" onChange={handleChange} />
       </div>
        
        <WaistDropDown waist = {measure.waist} changeWaist = {changeWaist}/>
       
        </div>
             </div>

             <div class = "row justify-content-center row1">
             <div class="message">If waist size is not available then please add it</div>
        <div class="col-lg-3">
        
        <button type="button" class="btn btn-primary waistbtn" onClick={()=>addWaistSize()}>ADD SIZE</button>
        </div>
        </div>
        
       </div>
    
    </div>
   
  );
}

export default Measure;
