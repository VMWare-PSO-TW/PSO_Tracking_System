import "./progressInfo.css"
import BusinessCenterTwoToneIcon from '@mui/icons-material/BusinessCenterTwoTone';
import NextPlanTwoToneIcon from '@mui/icons-material/NextPlanTwoTone';
import AccessTimeTwoToneIcon from '@mui/icons-material/AccessTimeTwoTone';


import engagementDummyData from "../../data/engagementDummyData";


const ProgressInfo = ({ phaseItems, engagementId}) => {
    const engagementItem = engagementDummyData.find((e) => e.id === engagementId);

    const getSum = (arr, key) => {
        return arr.reduce((accumulator, current) => accumulator + Number(current[key]), 0)
    }

    

    const getCurrentPhase = (actual) => {
        
        let accum = 0;
        for (let i = 0; i < phaseItems.length; i++){
            
            accum += phaseItems[i].expect
            // console.log(`accum: ${accum}  phase:${i + 1}`)
            if (actual < accum){
                return i + 1
            }
        }
        return phaseItems.length + 1
    }

    const expectHours = getSum(phaseItems, 'expect');
    const actualHours = getSum(phaseItems, 'actual');
    const remainHours = expectHours - 165;
    const currentPercent = (165 / expectHours ).toFixed(2) * 100;
    const currentPhase = getCurrentPhase(165);


    return (
        <div className="progressInfo">
            <div className="infoItemTitle">
                <BusinessCenterTwoToneIcon/>
                <span className="infoName">{engagementItem.name}</span>
                <span className="infoId">{engagementItem.id}</span>
            </div>
            <div className="infoItemStatus">
                <NextPlanTwoToneIcon/>
                {
                    currentPhase < phaseItems.length 
                    ? 
                    (<span className='infoPhase'>
                        {`Phase ${currentPhase}`}
                        <span className="infoPercent">
                            {`has completed ${currentPercent} %`}
                        </span>
                    </span>)
                    :
                    (<span className='infoPhase'>Complete</span>)
                }
            
            </div>
            <div className="infoItemUsage">
                <AccessTimeTwoToneIcon />
                <div className="infoHour">
                    <span className="infoActualHour">{165}
                        <span className="infoActualText">
                            hrs used
                        </span>
                    </span>
                        /
                    <span className="infoRemainHour">{remainHours}
                    <span className="infoRemainText">
                            hrs remaining
                        </span>
                    </span>
                </div>
            </div>
        </div>

    )

}

export default ProgressInfo;