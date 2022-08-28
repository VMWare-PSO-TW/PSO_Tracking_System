
import FeaturedInfo from "../../components/featuredInfo/FeaturedInfo";
import "./home.css";

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
      <FeaturedInfo engagementItems={engagementItems} />
     
      <div className="homeWidgets">
        
        <EngagementList engagementItems={engagementItems} />
      </div>
    </div>
  );
}
