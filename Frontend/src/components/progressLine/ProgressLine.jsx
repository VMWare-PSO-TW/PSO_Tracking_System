import "./progressLine.css";

import { ProgressBar } from 'react-bootstrap';

const ProgressLine = ({ actualPercentage }) => {


   
    return (

                <ProgressBar label={`${actualPercentage}%`} now={actualPercentage} animated/>

       
    )
}

export default ProgressLine;