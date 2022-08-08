import { Link } from "react-router-dom";
import Button from '@mui/material/Button';
import './engagementList.css';

export const renderFunction = {

    name: (props) => {
        return (
            
                <Link to={{ 
                    pathname: `/engagement/${props.record.id}`,
                }} 
                style={{ textDecoration: 'none' ,color: '#0000CD'}}>
                {props.value}
                </Link>
        )
    },

    id: (props) => {
        return props.value
    },

    status: (props) => {
         
        
        
        const status = (((props.record.actual / props.record.expect )) * 100).toFixed(0)
    
        
        
        let statusString = ''

        if (status < 60){
            statusString = 'error'
        }else if (status >= 60 && status <= 99){
            statusString = 'secondary'
        }else{
            statusString = 'success'
        }


        return (
            <Button variant="outlined" color={`${statusString}`} fullWidth={true} >
                {`${status}%`}
            </Button>
        )

        
    },

    actual: (props) => {
        return props.value
    },

    remain: (props) => {
        const remainHours = props.record.expect - props.record.actual
        
        return remainHours
    },

    total: (props) => {
        return props.value
    }
}


