import React, { useState } from "react";
import MaterialTable from '@material-table/core';
import './memberForecast.css';

import { getNextWeekDays } from "../../utils/forecastCount";

import memberForecastDummyData from "../../data/memberForecastDummyData";
const nextWeekDays = getNextWeekDays();

const columns = [
    { title: "", field: "id", editable: false },
    { title: "Name", field: "name", editable: false },
    { title: "ID", field: "eid", editable: false },
    { title: `${nextWeekDays[0]}`, field: "mon" },
    { title: `${nextWeekDays[1]}`, field: "tue" },
    { title: `${nextWeekDays[2]}`, field: "wed" },
    { title: `${nextWeekDays[3]}`, field: "thr" },
    { title: `${nextWeekDays[4]}`, field: "fri" },
]
// const empList = [
//     { id: 0, name: "Neeraj", email: 'neeraj@gmail.com', phone: 9876543210, city: "Bangalore" },
//     { id: 1, name: "Raj", email: 'raj@gmail.com', phone: 9812345678, city: "Chennai" },
//     { id: 2, name: "David", email: 'david342@gmail.com', phone: 7896536289, city: "Jaipur" },
//     { id: 3, name: "Vikas", email: 'vikas75@gmail.com', phone: 9087654321, city: "Hyderabad" },
//   ]

// const columns = [
//     { title: "ID", field: "id", editable: false },
//     { title: "Name", field: "name" },
//     { title: "Email", field: "email" },
//     { title: "Phone Number", field: 'phone', },
//     { title: "City", field: "city", }
//   ]

const MemberForecast = () => {
    const [data, setData] = useState(memberForecastDummyData)
    return (
        <div className="memberForecast">
          {/* <h1 align="center">React-App</h1>
          <h4 align='center'>Material Table with CRUD operation</h4> */}
          <MaterialTable
            title="Engagements"
            data={data}
            columns={columns}
            editable={{

              onRowUpdate:(newData, oldData)=>new Promise((resolve,reject)=>{

                setTimeout(() => {
                  
                    const dataUpdate = [...data];
                    const index = oldData.tableData.id;
                    dataUpdate[index] = newData;
                    setData([...dataUpdate]);
                    resolve();

                }, 2000)
              })
    
            }}
            options={{
              actionsColumnIndex: -1, addRowPosition: "first"
            }}
          />
        </div>
      );
}

export default MemberForecast;