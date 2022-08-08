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
                <GroupsTwoToneIcon style={{marginBottom: '30px'}}/>
                <MemberList members={memberItems}/>
            </div>
        </div>
    )
}

export default EngagementDetail;