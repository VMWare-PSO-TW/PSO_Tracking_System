import './memberSwitch.css'
import Button from '@mui/material/Button';

import MemberEngagementsList from "../memberEngagementsList/MemberEngagementsList";
import MemberForecast from "../memberForecast/MemberForecast";
import React, { useState, useEffect, useCallback } from 'react';


const MemberSwitch = () => {
    const [active, setActive] = React.useState(1);
    const SetView = (active) => {
        setActive(active);
    };
    const ActiveView = () => {
        switch (active) {
          case 1:
            return (
                <MemberEngagementsList />
            );
          case 2:
            return <MemberForecast />;
          
        }
      };
    return (
        <div className='test'>
            <div className="featuredSwitch">
                <div className="featuredSwitchItem">
                
                        <Button className="buttonSwitch" onClick={() => SetView(1)}>
                            Engagements List
                        </Button>

                </div>
                <div className="featuredSwitchItem">

                        <Button className="buttonSwitch" onClick={() => SetView(2)}>
                            Forecast Nextweek
                        </Button>

                </div>
                
            </div>
            {ActiveView()}
        </div>
    )
}

export default MemberSwitch;