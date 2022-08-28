import { Link } from "react-router-dom";
import Button from '@mui/material/Button';
import ProgressBar from 'react-bootstrap/ProgressBar';

import './memberDashboardList.css';

export const renderFunction = {

    name: (props) => {
        return (
            
                <Link to={{ 
                    pathname: `/member/${props.record.id}`,
                }} 
                style={{ textDecoration: 'none' ,color: '#696969'}}>
                {props.value}
                </Link>
        )
    },





    utRate: (props) => {
         
        return (
            <div className="progressBar">
                <ProgressBar 
                  className="utRate"
                  now={props.value} label={`${props.value}%`} 
                  animated 
                />
            </div>
        );

        
    },

    completeRate: (props) => {
         
        
        return (
            <div className="progressBar">
                <ProgressBar 
                //   variant="success"
                  className="completeRate"
                  now={props.value} label={`${props.value}%`} 
                  animated 
                />
            </div>
        );

        
    },
    
    total_actual: (props) => {
        return (
            <div className="engagementTr">
                {props.value}
            </div>
        )
    },

    total_remain: (props) => {
        
        return (
            <div className="engagementTr">
                {props.value}
            </div>
        )
    },

    total_expect: (props) => {
        return (
            <div className="engagementTr">
                {props.value}
            </div>
        )
    }
}


