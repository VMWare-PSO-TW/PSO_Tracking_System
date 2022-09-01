import './memberEngagementsList.css'
import FilterableTable from 'react-filterable-table';
import memberDummyData from '../../data/memberDummyData';
import React, {  useEffect,useState } from 'react';
import { renderFunction } from './utils';

import { useLocation } from 'react-router-dom'
import { fetchMember } from '../../data/fetchData';

const fields = [
    { name: "name", displayName: "Name", inputFilterable:true, exactFilterable: true, sortable:true, render: renderFunction.name, tdClassName:"memberName" , thClassName:"memberTh"},
    { name:"id", displayName: "ID",inputFilterable:true, exactFilterable: true, sortable:true, render: renderFunction.utRate, tdClassName:"memberEngagementTdStatus", thClassName:"memberTh"},
    { name:"completeRate", displayName: "Person Complete Rate",inputFilterable:true, exactFilterable: true, sortable:true, render: renderFunction.completeRate, tdClassName:"memberTdStatus", thClassName:"memberTh"},
    { name: "total_actual", displayName: "Person Used hours", inputFilterable:true, exactFilterable: true, sortable:true, render: renderFunction.total_actual , thClassName:"memberTh",tdClassName:"memberTd"},
    { name: "total_remain", displayName: "Person Remaining hours", inputFilterable:true, exactFilterable: true, sortable:true, render: renderFunction.total_remain , thClassName:"memberTh",tdClassName:"memberTd"},
    { name: "total_expect", displayName: "Person Total hours", inputFilterable:true, exactFilterable: true, sortable:true, render: renderFunction.total_expect , thClassName:"memberTh",tdClassName:"memberTd"}
]
const MemberEngagementsList = () => {

    const [engagementList, setEngagementList] = useState([]);

    const location = useLocation();
    
    const pathName = location.pathname;
    const memberId = pathName.substring(pathName.lastIndexOf('/')+ 1)
    
    
    
    useEffect(() => {

        const filter = document.getElementsByClassName('close clear-filter')[0];
        filter.innerText = 'Clear Filter';


        const placeHolder = document.getElementsByClassName('form-control filter-input')[0];
        placeHolder.placeholder = 'Name / ID'

        console.log('execute function in useEffect Member!');

        const fetchingData = async (memberId) => {
            const member = await fetchMember(memberId);

            const memberEngagementsList = member[0].engagements.map((engagement)=>{
                const completeRate = parseInt(((engagement.total_actual / engagement.total_expect) * 100).toFixed(2), 10);
                const remainHours = engagement.total_expect - engagement.total_actual;
        
                return {
                    ...engagement,
                    completeRate: completeRate,
                    total_remain: remainHours
                }
            })
    
            setEngagementList(memberEngagementsList);
 
            console.log('memberEngagementsList ',memberEngagementsList);
            
        };
        fetchingData(memberId);
        

        
    }, []);


    return (
        <div className="memberEngagementList">
            <FilterableTable
                namespace="MemberEngagements"
                initialSort="name"
                data={engagementList}
                fields={fields}
                noRecordsMessage="There are no engagement to display"
                noFilteredRecordsMessage="No engagement match your filters!"
                autofocusFilter={true}
                headerVisible={true}
                pagerTitles={{first: '', last: '' }}
         />
        </div>
    )
}

export default MemberEngagementsList