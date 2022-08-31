import { Link } from "react-router-dom";
import Button from '@mui/material/Button';
import ProgressBar from 'react-bootstrap/ProgressBar';

import './memberEngagementsList.css';

export const renderFunction = {

    name: (props) => {
        return (
            
                <Link to={{ 
                    pathname: `/engagement/${props.record.id}`,
                }} 
                style={{ textDecoration: 'none' ,color: '#696969'}}>
                {props.value}
                </Link>
        )
    },


    id: (props) => {
         
        return (
            <div className="engagementTr">
                {props.value}
            </div>
        );

        
    },

    completeRate: (props) => {
         
        
        return (
            <div className="progressBar">
                <ProgressBar 
                  className="completeRate"
                  now={props.value} label={`${props.value}%`} 
                  animated 
                />
            </div>
        );

        
    },
    
    person_actual: (props) => {
        return (
            <div className="engagementTr">
                {props.value}
            </div>
        )
    },

    person_remain: (props) => {
        
        return (
            <div className="engagementTr">
                {props.value}
            </div>
        )
    },

    person_expect: (props) => {
        return (
            <div className="engagementTr">
                {props.value}
            </div>
        )
    }
}


