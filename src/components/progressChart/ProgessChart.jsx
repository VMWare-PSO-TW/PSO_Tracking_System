
import "./progressChart.css";
import "react-step-progress-bar/styles.css";
import InsightsTwoToneIcon from '@mui/icons-material/InsightsTwoTone';
import React, { useState, useEffect } from 'react';

import { ProgressBar, Step } from "react-step-progress-bar";

import ProgressLine from "../progressLine/ProgressLine";

const ProgressChart = ({ phaseItems }) => {

    const [progressBarItems, setProgressBarItems] = useState([])

    const getSum = (arr, key) => {
        return arr.reduce((accumulator, current) => accumulator + Number(current[key]), 0)
    }

    const getChartStep = (expectHours) => {
        let chartStepPercent = [0];
        let chartStepList = [
            <Step key={0}>
                    {() => (
                    <div
                        className={"indexedStep accomplished"}
                    >
                        {`${0}%`}
                    </div>
                    )}
                </Step>
        ];
        let accum = 0
        

        for (let i = 0; i < phaseItems.length; i++){
            accum += phaseItems[i].expect

            chartStepPercent.push(
                ((accum / expectHours).toFixed(2)*100)

            )

            chartStepList.push(
                <Step key={i + 1}>
                    {({ accomplished, index, position}) => (
                    <div className="wrapper">
                        <div
                            className={`fix indexedStep ${accomplished ? `accomplished` : `unaccomplished`}`}
                        >
                            {`${position}%`}
                            
                        </div>
                    
                        <div className="vertical-line"></div>
    
                        <div className="circle">
                            <h5 className="phase">Phase</h5>
                            <h5 className="index">{index}</h5>
                        </div>
                    </div>
                    )}
                </Step>
            )
        }
        return [chartStepPercent, chartStepList]
    }

    useEffect(() => {
        const expectHours = getSum(phaseItems, 'expect');
        const actualHours = getSum(phaseItems, 'actual');
        const [progressChartPercent, progressChartStep] = getChartStep(expectHours);
        
        const actualPercentage = ((actualHours / expectHours).toFixed(2) * 100);


        setProgressBarItems({
            percentage: actualPercentage,
            progress: progressChartPercent,
            steps: progressChartStep
            
        })

    },[phaseItems])
   
    return (
        <div className="progressChart">
            <InsightsTwoToneIcon style={{marginBottom: '30px'}}/>
            <ProgressBar 
                className="progress"
                stepPositions={progressBarItems.progress} 
                // percent={progressBarItems.percentage}
                percent={100}
                filledBackground="linear-gradient(to right, #B0C4DE, #4169E1)"
                height={40}
            >
                {progressBarItems.steps}
            </ProgressBar>
            <ProgressLine actualPercentage={progressBarItems.percentage}/>

        </div>
       
    )
}

export default ProgressChart;