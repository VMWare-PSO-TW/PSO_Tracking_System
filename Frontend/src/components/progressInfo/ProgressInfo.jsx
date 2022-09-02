import "./progressInfo.css"
import BusinessCenterTwoToneIcon from '@mui/icons-material/BusinessCenterTwoTone';
import NextPlanTwoToneIcon from '@mui/icons-material/NextPlanTwoTone';
import AccessTimeTwoToneIcon from '@mui/icons-material/AccessTimeTwoTone';

import React, { useState, useEffect } from 'react';
import engagementDummyData from "../../data/engagementDummyData";

import { fetchEngagement } from "../../data/fetchData";

const ProgressInfo = ({ phaseItems, engagementId}) => {

    const [engagementItem, setEngagementItem] = useState({})
    useEffect(() => {
        console.log('execute function in useEffect Phase!');
        const fetchingData = async (engagementId) => {
            const engagement = await fetchEngagement(engagementId);

            setEngagementItem(
                engagement
            );

 
        }
        fetchingData(engagementId);
    }, []);


    const getSum = (arr, key) => {
        return arr.reduce((accumulator, current) => accumulator + Number(current[key]), 0)
    }

    

    const getCurrentPhase = (actual) => {
        
        let accum = 0;
        for (let i = 0; i < phaseItems.length; i++){
            
            accum += phaseItems[i].expect_hours
            
            if (actual < accum){
                return i + 1
            }
        }
        return phaseItems.length + 1
    }

    const expectHours = getSum(phaseItems, 'expect_hours');
    const actualHours = getSum(phaseItems, 'actual_hours');
    const remainHours = expectHours - actualHours;
    const currentPercent = parseInt((actualHours / expectHours ).toFixed(2) * 100, 10);
    const currentPhase = getCurrentPhase(actualHours);

    const displayPhase = () => {

        if (actualHours == 0){
            return (<span className='infoPhase'>Not Started</span>)
        }
        if (phaseItems.length == 1){
            if (currentPhase == 1){
                return (
                    <div className="diplayPhase">
                        <span className='infoPhase'>
                            One Phase Only
                        </span>
                        <span className="infoPercent">
                        {`Current Progress: ${currentPercent} %`}
                        </span>
                    </div>
                )
            }
            else{
                return (
                    <div className="diplayPhase">
                        <span className='infoPhase'>
                            One Phase Only
                        </span>
                        <span className='infoPhase'>Complete</span>
                    </div>
                )
            }
        }
        
        if (currentPhase < phaseItems.length){
            return (
                <div className="displayPhase">
                    <span className='infoPhase'>
                        {`Phase ${currentPhase}`}
                    </span>
                    <span className="infoPercent">
                    {`Current Progress: ${currentPercent} %`}
                    </span>
                </div>
                )
        }else{
            
            return (<span className='infoPhase'>Complete</span>)
        }

    }

    return (
        <div className="progressInfo">
            <div className="infoItemTitle">
                <div className="infoIconContainer">
                    <BusinessCenterTwoToneIcon/>
                    <span className="infoIconText">
                        Engagement Name
                    </span>
                </div>
                <span className="infoName">{engagementItem.name}</span>
                <span className="infoId">{engagementItem.id}</span>
            </div>
            <div className="infoItemStatus">
                <div className="infoIconContainer">
                    <NextPlanTwoToneIcon/>
                    <span className="infoIconText">
                        Current Phase
                    </span>
                </div>
                {
                    
                    
                    displayPhase()
                }
            
            </div>
            <div className="infoItemUsage">
                <div className="infoIconContainer">
                    <AccessTimeTwoToneIcon />
                    <span className="infoIconText">
                        Hours
                    </span>
                </div>
                <div className="infoHour">
                    <span className="infoActualHour">{actualHours}
                        <span className="infoActualText">
                            Used
                        </span>
                    </span>
                        /
                    <span className="infoRemainHour">{remainHours}
                    <span className="infoRemainText">
                            Remain
                        </span>
                    </span>
                </div>
            </div>
        </div>

    )

}

export default ProgressInfo;