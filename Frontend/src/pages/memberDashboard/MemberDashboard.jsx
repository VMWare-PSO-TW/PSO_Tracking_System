
import './memberDashboard.css';

import MemberDashboardInfo from '../../components/memberDashboardInfo/MemberDashboardInfo';
import MemberDashboardList from '../../components/memberDashboardList/MemberDashboardList';

const MemberDashboard = () => {

    return (
        <div className="memberDashboard">
            <MemberDashboardInfo />
            <div className="memberDashboardWidgets">
                <MemberDashboardList />
            </div>
        </div>
    )
};

export default MemberDashboard;