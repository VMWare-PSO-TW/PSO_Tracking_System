import './engagementList.css';

import FilterableTable from 'react-filterable-table';
import engagementDummyData from '../../data/engagementDummyData';

import { renderFunction }from './utils';
import React, {  useEffect } from 'react';
import Button from '@mui/material/Button';

const fields = [
    { name: "name", displayName: "Name", inputFilterable:true, exactFilterable: true, sortable:true, render: renderFunction.name, tdClassName:"engagementName" , thClassName:"engagementTh"},
    { name: "id", displayName: "ID", inputFilterable:true, exactFilterable: true, sortable:true, render: renderFunction.id , thClassName:"engagementTh"},
    { name: "status", displayName: "Status", inputFilterable:true, exactFilterable: true, sortable:true, render: renderFunction.status,tdClassName:"engagementTdStatus", thClassName:"engagementTh"},
    { name: "actual_hours", displayName: "Used hours", inputFilterable:true, exactFilterable: true, sortable:true, render: renderFunction.actual_hours , thClassName:"engagementTh"},
    { name: "remain_hours", displayName: "Remaining hours", inputFilterable:true, exactFilterable: true, sortable:true, render: renderFunction.remain_hours , thClassName:"engagementTh"},
    { name: "expect_hours", displayName: "Total hours", inputFilterable:true, exactFilterable: true, sortable:true, render: renderFunction.expect_hours , thClassName:"engagementTh"}
]

const EngagementList = ({engagementItems}) => {
    const engagementList = engagementItems.map(project => {
        const status = parseInt((((project.actual_hours / project.expect_hours )) * 100).toFixed(0), 10);
        const remain_hours = project.expect_hours - project.actual_hours;
        // console.log(project);
        return (
            {   
                ...project,
                status: status,
                remain_hours: remain_hours
                
            }
        )
    })
    useEffect(() => {

        

        const filter = document.getElementsByClassName('close clear-filter')[0];
        filter.innerText = 'Clear Filter';


        const placeHolder = document.getElementsByClassName('form-control filter-input')[0];
        placeHolder.placeholder = 'Name / ID'

    }, []);
    

    return (
        <div className="engagementList">
            <FilterableTable
                namespace="Engagements"
                initialSort="name"
                data={engagementList}
                fields={fields}
                noRecordsMessage="There are no engagement to display"
                noFilteredRecordsMessage="No engagement match your filters!"
                autofocusFilter={true}
                headerVisible={true}
                // pagerTitles={{first: '', last: '' }}
         />
        </div>
    )


}

export default EngagementList;