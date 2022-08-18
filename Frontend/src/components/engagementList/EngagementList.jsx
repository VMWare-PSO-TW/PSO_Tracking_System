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
    { name: "actual", displayName: "Used hours", inputFilterable:true, exactFilterable: true, sortable:true, render: renderFunction.actual , thClassName:"engagementTh"},
    { name: "remain", displayName: "Remaining hours", inputFilterable:true, exactFilterable: true, sortable:true, render: renderFunction.remain , thClassName:"engagementTh"},
    { name: "expect", displayName: "Total hours", inputFilterable:true, exactFilterable: true, sortable:true, render: renderFunction.total , thClassName:"engagementTh"}
]

const EngagementList = ({engagementItems}) => {
    const engagementDummyList = engagementDummyData.map(project => {
        const status = parseInt((((project.actual / project.expect )) * 100).toFixed(0), 10);
        const remainHours = project.expect - project.actual;

        return (
            {   
                ...project,
                status: status,
                remain: remainHours
                
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
                data={engagementDummyList}
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

export default EngagementList;