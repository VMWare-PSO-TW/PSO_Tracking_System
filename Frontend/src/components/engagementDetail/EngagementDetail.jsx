import engagementDummyData from '../../data/engagementDummyData';
import GroupsTwoToneIcon from '@mui/icons-material/GroupsTwoTone';
import './engagementDetail.css'

import MemberList from '../memberList/MemberList';

const EngagementDetail = ({ engagementId, members }) => {


    const engagementItem = engagementDummyData.find((e) => e.id === engagementId);
    const memberItems = members
   

    return (
        <div className="engagementContainer">
            <div className="engagementMember">
                <div className="engagementMemberIconContainer">
                    <GroupsTwoToneIcon style={{marginBottom: '30px'}}/>
                    <span className="engagementMemberIconText">
                        Members
                    </span>
                </div>
                <MemberList members={memberItems}/>
            </div>
        </div>
    )
}

export default EngagementDetail;