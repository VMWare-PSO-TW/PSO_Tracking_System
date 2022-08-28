
import './member.css'
import memberDummyData from '../../data/memberDummyData';
import MemberInfo from '../../components/memberInfo/MemberInfo';
import MemberSwitch from '../../components/memberSwitch/MemberSwitch';

const Member = () => {
    return (
        <div className="member">
            <MemberInfo member={memberDummyData}/>
            <MemberSwitch member={memberDummyData}/>

        </div>
    );
};

export default Member;