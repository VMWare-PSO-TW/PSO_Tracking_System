import './memberList.css';
import React, { useState } from 'react';
import { DataGrid } from "@material-ui/data-grid";
// import memberListDummyData from '../../data/memberListDummyData';
import Cols from './Columns';




const MemberList = ({ members }) => {
    
    const memberList = members;

    const colList = Cols;


    
    return (
        <div className="userList">
          <DataGrid

            columns={colList}
            rows={memberList}


            rowHeight='100'

          />
        </div>
      );
    
}

export default MemberList;