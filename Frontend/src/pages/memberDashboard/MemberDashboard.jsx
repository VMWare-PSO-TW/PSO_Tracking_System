
import './memberDashboard.css';

import MemberDashboardInfo from '../../components/memberDashboardInfo/MemberDashboardInfo';
import MemberDashboardList from '../../components/memberDashboardList/MemberDashboardList';
import { fetchAllMembers } from '../../data/fetchData';

import React, { useState, useEffect } from 'react';
const MemberDashboard = () => {

    const [membersItem, setMembersItem] = useState([])

    useEffect(() => {
        console.log('execute function in useEffect Member!');

        const fetchingData = async () => {
            const members = await fetchAllMembers();

            setMembersItem(
                members
            );

        }
        fetchingData();
        // console.log(membersItem)
    }, []);

    return (
        <div className="memberDashboard">
            <MemberDashboardInfo membersItem={membersItem}/>
            <div className="memberDashboardWidgets">
                <MemberDashboardList membersItem={membersItem}/>
            </div>
        </div>
    )
};

export default MemberDashboard;