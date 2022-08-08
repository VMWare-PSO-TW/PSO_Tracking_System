import React, { useState } from 'react';


import Checkbox, {CheckboxProps} from '@mui/material/Checkbox';
import Box from '@mui/material/Box';



const SUBMIT_FILTER_STROKE_TIME = 500;

export const InputNumberInterval = (props) => {
    const { item, applyValue, focusElementRef = null } = props;
  
    // const filterTimeout = React.useRef();
    const [filterValueState, setFilterValueState] = React.useState(
      item.value ?? [],
    );


    // const [applying, setIsApplying] = React.useState(false);
  
    // React.useEffect(() => {
    //   return () => {
    //     clearTimeout(filterTimeout.current);
    //   };
    // }, []);


  
    React.useEffect(() => {
    //   const itemValue = item.value ?? [undefined, undefined];
      const itemValue = item.value ?? []

      setFilterValueState(itemValue);
      console.log('ItemValue: ', filterValueState);
    }, [item.value]);
  
    // const updateFilterValue = (lowerBound, upperBound) => {
    //   clearTimeout(filterTimeout.current);
    //   setFilterValueState([lowerBound, upperBound]);
  
    //   setIsApplying(true);
    //   filterTimeout.current = setTimeout(() => {
    //     setIsApplying(false);
    //     applyValue({ ...item, value: [lowerBound, upperBound] });
    //   }, SUBMIT_FILTER_STROKE_TIME);
    // };
  
    // const handleUpperFilterChange = (event) => {
    //   const newUpperBound = event.target.value;
    //   updateFilterValue(filterValueState[0], newUpperBound);
    // };
    // const handleLowerFilterChange = (event) => {
    //   const newLowerBound = event.target.value;
    //   updateFilterValue(newLowerBound, filterValueState[1]);
    // };

    const handleCheckBox = (event) => {
        // const checkedItem = event.target.value;
        
        let updatedList = [...filterValueState];
        // console.log('current list ', filterValueState);

        if (event.target.checked) {
            // console.log('check item is ',event.target.value);
            updatedList = [...filterValueState, parseInt(event.target.value, 10)];
        }else{
            // console.log('uncheck item is ',event.target.value);
            updatedList.splice(filterValueState.indexOf(parseInt(event.target.value, 10)), 1)
        }
        setFilterValueState(updatedList);
        applyValue({...item, value: updatedList});
        // console.log(filterValueState);
        // console.log('updatedList: ',updatedList);
        console.log('updated List ', updatedList)
        console.log('filterValueState: ',filterValueState)
    }
    return (
      <Box
        sx={{
          display: 'inline-flex',
          flexDirection: 'row',
          alignItems: 'end',
          height: 48,
          pl: '20px',
        }}
      >
        {/* <TextField
          name="lower-bound-input"
          placeholder="From"
          label="From"
          variant="standard"
          value={Number(filterValueState[0])}
          onChange={handleLowerFilterChange}
          type="number"
          inputRef={focusElementRef}
          sx={{ mr: 2 }}
        />
        <TextField
          name="upper-bound-input"
          placeholder="To"
          label="To"
          variant="standard"
          value={Number(filterValueState[1])}
          onChange={handleUpperFilterChange}
          type="number"
          InputProps={applying ? { endAdornment: <SyncIcon /> } : {}}
        /> */}

        <Checkbox  value={Number(1)} onChange={handleCheckBox}  checked={filterValueState.includes(1)}/>
        <Checkbox  value={Number(2)} onChange={handleCheckBox}  checked={filterValueState.includes(2)}/>
        <Checkbox  value={Number(3)} onChange={handleCheckBox}  checked={filterValueState.includes(3)}/>
        <Checkbox  value={Number(4)} onChange={handleCheckBox}  checked={filterValueState.includes(4)}/>
      </Box>
    );
}



export const phaseOnlyOperators = [
    {
      label: 'CheckBox',
      value: 'between',
      getApplyFilterFn: (filterItem) => {
        console.log('filterItem ', filterItem);
        if (filterItem.value === undefined || filterItem.value.length === 0) {
            // console.log('undefined')
            // return false;
            return ({ value }) => {
                console.log('hello')
                return null
            }
        }


        return ({ value }) => {

        
          const checker = (arr, target) => {

              return arr.some(item => target.includes(item));
          }
          return (

            value !== null && filterItem.value !== undefined &&
            checker(filterItem.value, [...value])

          );
        
        };
      },
      InputComponent: InputNumberInterval,
    },
  ];
  