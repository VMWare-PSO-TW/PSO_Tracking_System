import "./featuredInfo.css";
import { ArrowDownward, ArrowUpward } from "@material-ui/icons";
import engagementDummyData from "../../data/engagementDummyData";


export default function FeaturedInfo({engagementItems}) {
  const getStatisticInfo = (engagement) => {
    const number = engagement.length;
    let totalExpectHours = 0;
    let totalActualHours = 0;

    engagement.forEach(project => {
      totalExpectHours += project.expect;
      totalActualHours += project.actual;
    })

    let totalRemainHours = totalExpectHours - totalActualHours;
    const status = parseInt(((( totalActualHours / totalExpectHours )) * 100).toFixed(0), 10);

    const object = {
      numberOfProjects: number,
      totalExpectHours: totalExpectHours,
      totalActualHours: totalActualHours,
      totalRemainHours: totalRemainHours,
      status: status
    }
    return object;
  }

  const totalStat = getStatisticInfo(engagementDummyData);



  return (
    <div className="featured">
      <div className="featuredItem">
        <span className="featuredTitle">Number of Engagements</span>
        <div className="featuredContainer">
          <span className="featuredNumber">{totalStat.numberOfProjects}</span>
          {/* <span className="featuredMoneyRate">
            -11.4 <ArrowDownward  className="featuredIcon negative"/>
          </span> */}
        </div>
        {/* <span className="featuredSub">Compared to last month</span> */}
      </div>
      <div className="featuredItem">
        <span className="featuredTitle">Complete Rate</span>
        <div className="featuredContainer">
          <span className="featuredNumber">{`${totalStat.status} %`}</span>
          {/* <span className="featuredMoneyRate">
            -1.4 <ArrowDownward className="featuredIcon negative"/>
          </span> */}
        </div>
        {/* <span className="featuredSub">Compared to last month</span> */}
      </div>
      <div className="featuredItem">
        <span className="featuredTitle">Total Hours</span>
        <div className="featuredContainer">
          
          {/* <span className="featuredMoney">$2,225</span>
          <span className="featuredMoneyRate">
            +2.4 <ArrowUpward className="featuredIcon"/>
          </span> */}
            <span className="featureActualHour">{totalStat.totalActualHours}
                <span className="featureText">
                    Used
                </span>
            </span>
                /
            <span className="featureRemainHour">{totalStat.totalRemainHours}
                <span className="featureText">
                    Remain
                </span>
            </span>
                /
            <span className="featureExpectHour">{totalStat.totalExpectHours}
                <span className="featureText">
                    Expect
                </span>
            </span>
            
        </div>
        {/* <span className="featuredSub">Compared to last month</span> */}
      </div>
    </div>
  );
}