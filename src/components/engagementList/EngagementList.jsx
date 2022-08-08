import './engagementList.css';

import FilterableTable from 'react-filterable-table';
import engagementDummyData from '../../data/engagementDummyData';

import { renderFunction }from './utils';
import React, {  useEffect } from 'react';
import Button from '@mui/material/Button';

const fields = [
    { name: "name", displayName: "Name", inputFilterable:true, exactFilterable: true, sortable:true, render: renderFunction.name, tdClassName:"engagementName" },
    { name: "id", displayName: "ID", inputFilterable:true, exactFilterable: true, sortable:true, render: renderFunction.id },
    { name: "status", displayName: "Status", inputFilterable:true, exactFilterable: true, sortable:true, render: renderFunction.status,tdClassName:"engagementStatus"},
    { name: "actual", displayName: "Used hours", inputFilterable:true, exactFilterable: true, sortable:true, render: renderFunction.actual },
    { name: "remain", displayName: "Remaining hours", inputFilterable:true, exactFilterable: true, sortable:true, render: renderFunction.remain },
    { name: "expect", displayName: "Total hours", inputFilterable:true, exactFilterable: true, sortable:true, render: renderFunction.total }
]

const EngagementList = ({engagementItems}) => {

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
                data={engagementDummyData}
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