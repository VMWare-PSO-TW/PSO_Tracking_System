import './memberDashboardList.css';

import FilterableTable from 'react-filterable-table';
import memberDashboardDummyData from '../../data/memberDashboardDummyData';
import { getCurrentPeriod, getAllRates } from '../../utils/seasonCount';
import React, {  useEffect } from 'react';
import { renderFunction } from './utils';

const fields = [
    { name: "name", displayName: "Name", inputFilterable:true, exactFilterable: true, sortable:true, render: renderFunction.name, tdClassName:"memberName" , thClassName:"memberTh"},
    { name:"utRate", displayName: "Utility Rate",inputFilterable:true, exactFilterable: true, sortable:true, render: renderFunction.utRate, tdClassName:"memberTdStatus", thClassName:"memberTh"},
    { name:"completeRate", displayName: "Complete Rate",inputFilterable:true, exactFilterable: true, sortable:true, render: renderFunction.completeRate, tdClassName:"memberTdStatus", thClassName:"memberTh"},
    { name: "total_actual", displayName: "Used hours", inputFilterable:true, exactFilterable: true, sortable:true, render: renderFunction.total_actual , thClassName:"memberTh",tdClassName:"memberTd"},
    { name: "total_remain", displayName: "Remaining hours", inputFilterable:true, exactFilterable: true, sortable:true, render: renderFunction.total_remain , thClassName:"memberTh",tdClassName:"memberTd"},
    { name: "total_expect", displayName: "Total hours", inputFilterable:true, exactFilterable: true, sortable:true, render: renderFunction.total_expect , thClassName:"memberTh",tdClassName:"memberTd"}
]
const MemberDashboardList = ({ membersItem }) => {
    const memberList = membersItem.map(member => {
        const {startDate, endDate, curDate, curPeriod} = getCurrentPeriod();

        const {allUTRate, allCompleteRate} = getAllRates(startDate, curDate, [member]);
        const remainHours = member.total_expect - member.total_actual;

        return (
            {   
                ...member,
                completeRate: allCompleteRate,
                utRate: allUTRate,
                total_remain: remainHours
            }
        )
    });
    useEffect(() => {

        

        const filter = document.getElementsByClassName('close clear-filter')[0];
        filter.innerText = 'Clear Filter';


        const placeHolder = document.getElementsByClassName('form-control filter-input')[0];
        placeHolder.placeholder = 'Name'

    }, [membersItem]);
    return (
        <div className="memberList">
            <FilterableTable
                namespace="Members"
                initialSort="name"
                data={memberList}
                fields={fields}
                noRecordsMessage="There are no member to display"
                noFilteredRecordsMessage="No member match your filters!"
                autofocusFilter={true}
                headerVisible={true}
                pagerTitles={{first: '', last: '' }}
         />
        </div>
    )
}

export default MemberDashboardList;