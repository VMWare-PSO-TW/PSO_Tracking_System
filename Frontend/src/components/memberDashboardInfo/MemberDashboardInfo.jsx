import memberDashboardDummyData from "../../data/memberDashboardDummyData";
import './memberDashboardInfo.css';
import { getAllRates, getCurrentPeriod } from "../../utils/seasonCount";
const MemberDashboardInfo = () => {

 

    const {startDate, endDate, curDate, curPeriod} = getCurrentPeriod();

    const {allUTRate, allCompleteRate} = getAllRates(startDate, curDate, memberDashboardDummyData);
    
    return (
        <div className="featured">
          <div className="featuredItem">
            <span className="featuredTitle">Current Period</span>
            <div className="featuredContainer">
              <span className="featuredNumber">{curPeriod}</span>

            </div>

          </div>
          <div className="featuredItem">
            <span className="featuredTitle">Season Span</span>
            <div className="featuredContainer">
            <span className="featureStartDate">
                <span className="featureText">
                    Start Date
                </span>
                {startDate}

            </span>

            <span className="featureEndDate"> 
                <span className="featureText">
                    End Date
                </span>
                {endDate}

            </span>

            

            </div>

          </div>
          <div className="featuredItem">
            <span className="featuredTitle">Total Rates</span>
            <div className="featuredRateContainer">

            <span className="featureUTRate">{`${allUTRate}%`}
                <span className="featureRateText">
                    UT Rate
                </span>
            </span>
                /
            <span className="featureCompleteRate">{`${allCompleteRate}%`}
                <span className="featureRateText">
                    Complete Rate
                </span>
            </span>
                
            </div>
          </div>
        </div>
      );
}

export default MemberDashboardInfo;