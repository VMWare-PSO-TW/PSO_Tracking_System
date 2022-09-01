
import './member.css'
import memberDummyData from '../../data/memberDummyData';
import MemberInfo from '../../components/memberInfo/MemberInfo';
import MemberSwitch from '../../components/memberSwitch/MemberSwitch';
import { useLocation } from 'react-router-dom'
import { fetchMember } from '../../data/fetchData';
import React, { useState, useEffect } from 'react';

const Member = () => {
    const location = useLocation();
    
    const pathName = location.pathname;
    const memberId = pathName.substring(pathName.lastIndexOf('/')+ 1)
    const [memberItem, setMemberItem] = useState({})

    console.log(memberId)

    useEffect(() => {
        console.log('execute function in useEffect Member!');

        const fetchingData = async (memberId) => {
            const member = await fetchMember(memberId);

            setMemberItem(
                member[0]
            );

            
        };
        fetchingData(memberId);
        console.log('memberItem: ',memberItem);
    }, [location.pathname]);

    return (
        <div className="member">
            <MemberInfo memberItem={memberItem}/>
            <MemberSwitch memberItem={memberItem}/>

        </div>
    );
};

export default Member;