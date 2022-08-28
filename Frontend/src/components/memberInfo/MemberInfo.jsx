import './memberInfo.css';
import { getCurrentPeriod, getAllRates } from '../../utils/seasonCount';

const MemberInfo = ({member}) => {

    const total_remain = member.total_expect - member.total_actual;
    const {startDate, endDate, curDate, curPeriod} = getCurrentPeriod();
    const {allUTRate, allCompleteRate} = getAllRates(startDate, curDate, [member]);

    return (
        <div className="featured">
          <div className="featuredItem">
            <span className="featuredTitle">Personal Info</span>
            <div className="featuredContainer">
              <span className="featuredName">{member.name}</span>
              <span className="featuredRole">{member.role}</span>

            </div>

          </div>
          <div className="featuredItem">
            <span className="featuredTitle">Total Hours</span>
            <div className="featuredMemberContainer">
            <span className="featureActualHour">{member.total_actual}
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
            <span className="featureExpectHour">{member.total_expect}
                <span className="featureText">
                    Expect
                </span>
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

export default MemberInfo;