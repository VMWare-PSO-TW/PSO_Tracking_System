import './memberEngagementsList.css'
import FilterableTable from 'react-filterable-table';
import memberDummyData from '../../data/memberDummyData';
import React, {  useEffect } from 'react';
import { renderFunction } from './utils';

const fields = [
    { name: "name", displayName: "Name", inputFilterable:true, exactFilterable: true, sortable:true, render: renderFunction.name, tdClassName:"memberName" , thClassName:"memberTh"},
    { name:"id", displayName: "ID",inputFilterable:true, exactFilterable: true, sortable:true, render: renderFunction.utRate, tdClassName:"memberEngagementTdStatus", thClassName:"memberTh"},
    { name:"completeRate", displayName: "Person Complete Rate",inputFilterable:true, exactFilterable: true, sortable:true, render: renderFunction.completeRate, tdClassName:"memberTdStatus", thClassName:"memberTh"},
    { name: "person_actual", displayName: "Person Used hours", inputFilterable:true, exactFilterable: true, sortable:true, render: renderFunction.person_actual , thClassName:"memberTh",tdClassName:"memberTd"},
    { name: "person_remain", displayName: "Person Remaining hours", inputFilterable:true, exactFilterable: true, sortable:true, render: renderFunction.person_remain , thClassName:"memberTh",tdClassName:"memberTd"},
    { name: "person_expect", displayName: "Person Total hours", inputFilterable:true, exactFilterable: true, sortable:true, render: renderFunction.person_expect , thClassName:"memberTh",tdClassName:"memberTd"}
]
const MemberEngagementsList = () => {
    const memberEngagementsDummyList = memberDummyData.engagements.map((engagement)=>{
        const completeRate = parseInt(((engagement.person_actual / engagement.person_expect) * 100).toFixed(2), 10);
        const remainHours = engagement.person_expect - engagement.person_actual;

        return {
            ...engagement,
            completeRate: completeRate,
            person_remain: remainHours
        }
    })
    // console.log(memberEngagementsDummyList);
    useEffect(() => {

        

        const filter = document.getElementsByClassName('close clear-filter')[0];
        filter.innerText = 'Clear Filter';


        const placeHolder = document.getElementsByClassName('form-control filter-input')[0];
        placeHolder.placeholder = 'Name / ID'

    }, []);
    return (
        <div className="memberEngagementList">
            <FilterableTable
                namespace="MemberEngagements"
                initialSort="name"
                data={memberEngagementsDummyList}
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