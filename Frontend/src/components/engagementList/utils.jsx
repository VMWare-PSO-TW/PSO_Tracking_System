import { Link } from "react-router-dom";
import Button from '@mui/material/Button';
import './engagementList.css';

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
        )   
    },

    status: (props) => {
         
        
        
    
        
        
        let statusString = ''

        if (props.value < 60){
            statusString = 'error'
        }else if (props.value >= 60 && props.value <= 99){
            statusString = 'secondary'
        }else{
            statusString = 'success'
        }


        return (
            <Button variant="outlined" color={`${statusString}`} fullWidth={true} >
                {`${props.value}%`}
            </Button>
        )

        
    },

    actual: (props) => {
        return (
            <div className="engagementTr">
                {props.value}
            </div>
        )
    },

    remain: (props) => {
        
        return (
            <div className="engagementTr">
                {props.value}
            </div>
        )
    },

    total: (props) => {
        return (
            <div className="engagementTr">
                {props.value}
            </div>
        )
    }
}


