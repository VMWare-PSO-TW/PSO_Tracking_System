import "./progressLine.css";

import { ProgressBar } from 'react-bootstrap';

const ProgressLine = ({ actualPercentage }) => {


   
    return (

                <ProgressBar label={`${70}%`} now={70} animated/>

       
    )
}

export default ProgressLine;