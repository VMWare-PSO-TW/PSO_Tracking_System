import './phase.css';
import { useLocation } from 'react-router-dom'
import React, { useState, useEffect } from 'react';

import ProgressChart from '../../components/progressChart/ProgessChart';
import { fetchAllPhases,fecthAllPhasesInfo } from '../../data/fetchData';


import EngagementDetail from '../../components/engagementDetail/EngagementDetail';

import ProgressInfo from '../../components/progressInfo/ProgressInfo';

const Phase = () =>{
    
    const [phaseItems, setPhaseItems] = useState([]);
    const [memberItems, setMemberItems] = useState([]);



    const location = useLocation()
    const pathName = location.pathname

    const engagementId = pathName.substring(pathName.lastIndexOf('/')+ 1)

    useEffect(() => {
        console.log('execute function in useEffect Phase!');

        const fetchingData = async (engagementId) => {
            const memberInfo = await fetchAllPhases(engagementId);
            const phasesInfo = await fecthAllPhasesInfo(engagementId);
            setPhaseItems(
                phasesInfo
            );

            setMemberItems(
                memberInfo
            );


        }
            fetchingData(engagementId);
    }, [location.pathname]);

    return (
        <div className="phase">
            <ProgressInfo phaseItems={phaseItems} engagementId={engagementId}/>
            <ProgressChart phaseItems={phaseItems}/>
            <EngagementDetail engagementId={engagementId} members={memberItems}/>
        </div>
    )
};

export default Phase;