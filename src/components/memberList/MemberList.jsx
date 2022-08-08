import './memberList.css';
import React, { useState } from 'react';
import { DataGrid } from "@material-ui/data-grid";
import memberListDummyData from '../../data/memberListDummyData';
import Cols from './Columns';
import { phaseOnlyOperators } from './Utils';



const MemberList = ({ members }) => {
    
    const memberList = memberListDummyData;

    const colList = Cols;

    // const [filterModel, setFilterModel] = React.useState({
    //   items: [
    //     {
    //       id: 1,
    //       columnField: 'phase',
    //       value: [1, 2, 3, 4],
    //       operatorValue: 'between',
    //     },
    //   ],
    // });

    // const columns = React.useMemo(() => {
    //   const newColumns = [...colList];

      
  
    //   if (newColumns.length > 0) {
    //     const index = newColumns.findIndex((col) => col.field === 'phase');
    //     const phaseColumn = newColumns[index];
  
        

    //     newColumns[index] = {
    //       ...phaseColumn,
    //       filterOperators: phaseOnlyOperators,
    //     };
    //   }
  
    //   return newColumns;
    // }, [colList]);

    // const test = (data) => {
    //   console.log('data',data)

      
    // }
    // const newColumns = [...colList];
    
    return (
        <div className="userList">
          <DataGrid

            columns={colList}
            rows={memberList}

            // disableSelectionOnClick
            

            rowHeight='80'

            // columns={columns}
            // filterModel={filterModel}
            // onFilterModelChange={(model) => setFilterModel(model)}


          />
        </div>
      );
    
}

export default MemberList;