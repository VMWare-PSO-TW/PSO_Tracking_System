import './memberInfo.css';
import { getCurrentPeriod, getAllRates } from '../../utils/seasonCount';

const MemberInfo = ({ memberItem }) => {
    const total_remain = memberItem.total_expect - memberItem.total_actual;
    const {startDate, endDate, curDate, curPeriod} = getCurrentPeriod();
    const {allUTRate, allCompleteRate} = getAllRates(startDate, curDate, [memberItem]);

    return (
        <div className="featured">
          <div className="featuredItem">
            <span className="featuredTitle">Personal Info</span>
            <div className="featuredMemberInfoContainer">
              <span className="featuredName">{memberItem.member_name}</span>
              <span className="featuredRole">{memberItem.role}</span>

            </div>

          </div>
          <div className="featuredItem">
            <span className="featuredTitle">Total Hours</span>
            <div className="featuredMemberHoursContainer">
            <span className="featureActualHour">{memberItem.total_actual}
                <span className="featureText">
                    Used
                </span>
            </span>
                /
            <span className="featureRemainHour">{total_remain}
                <span className="featureText">
                    Remain
                </span>
            </span>
                /
            <span className="featureExpectHour">{memberItem.total_expect}
                <span className="featureText">
                    Expect
                </span>
            </span>

            

            </div>

          </div>
          <div className="featuredItem">
            <span className="featuredTitle">Total Rates</span>
            <div className="featuredMemberRateContainer">

            <span className="featureUTRate">{`${allUTRate}%`}
                <span className="featureRateText">
                    Utility
                </span>
            </span>
                /
            <span className="featureCompleteRate">{`${allCompleteRate}%`}
                <span className="featureRateText">
                    Complete
                </span>
            </span>
                
            </div>
          </div>
        </div>
      );
}

export default MemberInfo;