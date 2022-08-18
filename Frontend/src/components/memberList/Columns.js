import ProgressBar from 'react-bootstrap/ProgressBar';
import Button from '@mui/material/Button';
import './memberList.css'

const Cols =  [
    { 
        field: "name", 
        headerName: "Name",
        width: 150 ,
        sortable: false,
        filterable: false,
        renderCell: (params) => {
            return (
              <div className="userListUser">
                {params.row.name}
              </div>
            );
        },
    },
    { 
        field: "role", 
        headerName: "Role", 
        width: 200,
        sortable: false,
        filterable: false,
        renderCell: (params) => {
            return (
              <div className="userListUser">
                {params.row.role}
              </div>
            );
        },
  
    },
    {
        field: "phase", 
        headerName: "Phase",
        width: 250,
        sortable: false,
        filterable: false,
        
        
        valueGetter: (params) => {
          const personalPhaseInfo = params.row.phases;
  
          let steps = []
  
          for (let i = 0; i < personalPhaseInfo.length; i++){
            steps.push(
              personalPhaseInfo[i].step
            )
          }

          return steps;
        },
        renderCell: (params) => {
            const personalPhaseInfo = params.row.phases;
  
            let personalDisplay = []
  
            for (let i = 0; i < personalPhaseInfo.length; i++){
              personalDisplay.push(
                <Button variant="outlined" className="button" key={i}>
                  {`Phase ${personalPhaseInfo[i].step}`}
                </Button>
              )
            }
  
            return (
              <div className="phases">
                {personalDisplay}
              </div>
            );
        },
    },
    {
        field: "progress", 
        headerName: "Progress Bar", 
        width: 300,
        sortable: false,
        filterable: false,
        renderCell: (params) => {
            const completePercent = (((params.row.actual / params.row.expect)) * 100).toFixed(0)
  
            return (
              <div className="progressBar">
                  <ProgressBar 
                    variant="success" 
                    now={completePercent} label={`${completePercent}%`} 
                    animated 
                  />
              </div>
            );
        },
    },
    {
        field: "used", 
        headerName: "Used Hours", 
        width: 200,
        sortable: false,
        filterable: false,
        renderCell: (params) => {
            const actualHours = params.row.actual;
    
            return (
                <div className="userListUser">
                {actualHours}
                </div>
            );
        },
    },
    {
        field: "remaining", 
        headerName: "Remaining Hours", 
        width: 200,
        sortable: false,
        filterable: false,
        renderCell: (params) => {
            const remainHours = params.row.expect - params.row.actual;
                return (
                <div className="userListUser">
                    {remainHours}
                </div>
                );
        },
    },
    {
        field: "total", 
        headerName: "Total Expect Hours", 
        width: 200,
        sortable: false,
        filterable: false,
        renderCell: (params) => {
            const expectHours = params.row.expect;
                return (
                <div className="userListUser">
                    {expectHours}
                </div>
                );
        },

    }
  
  ];

  export default Cols;