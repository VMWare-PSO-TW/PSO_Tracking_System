import Chart from "../../components/chart/Chart";
import FeaturedInfo from "../../components/featuredInfo/FeaturedInfo";
import "./home.css";
import { userData } from "../../dummyData";
import WidgetSm from "../../components/widgetSm/WidgetSm";
import WidgetLg from "../../components/widgetLg/WidgetLg";
import EngagementList from "../../components/engagementList/EngagementList";
import { fetchAllEngagements } from "../../data/fetchData";

import React, { useState, useEffect, useCallback } from 'react';

export default function Home() {
  const [engagementItems, setEngagementItems] = useState([]);

  const fetchData = useCallback(() => {
    console.log('execute function in useCallBack Home!');

    const fetchingData = async () => {
      const engagements = await fetchAllEngagements();
      setEngagementItems([
        ...engagements,
      ]);
    }
    fetchingData();

  },[]);

  useEffect(() => {
    console.log('execute function in useEffect Home!');
    fetchData();
  }, [fetchData]);


  return (
    <div className="home">
      <FeaturedInfo />
      {/* <Chart data={userData} title="User Analytics" grid dataKey="Active User"/> */}
      <div className="homeWidgets">
        {/* <WidgetSm/> */}
        {/* <WidgetLg engagementItems={engagementItems}/> */}
        <EngagementList engagementItems={engagementItems} />
      </div>
    </div>
  );
}
