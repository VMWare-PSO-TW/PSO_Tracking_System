import "./widgetLg.css";
import { Link } from "react-router-dom";
import { Redirect } from 'react-router';

export default function WidgetLg({ engagementItems }){
  const Button = ({ type }) => {
    return <button className={"widgetLgButton " + type}>{type}</button>;
  };
  
  

  let engagementList = []

  for (let i = 0; i < engagementItems.length; i++){
    // console.log(engagementItems[i])
    engagementList.push(
      
      <tr className="widgetLgTr" key={i} >
        
            <td className="widgetLgEngagement" >
              <span className="widgetLgName">
                <Link to={{ 
                    pathname: `/engagement/${engagementItems[i].id}`,
                  }} 
                  style={{ textDecoration: 'none' }}>
                  {engagementItems[i].name}
                </Link>

              </span>
            </td>
            <td className="widgetLgId">{engagementItems[i].id}</td>
            <td className="widgetLgActual">{engagementItems[i].actual}</td>
            <td className="widgetLgExpect">{engagementItems[i].expect}</td>

      </tr>
    )
  }

  return (
    <div className="widgetLg">
      <h3 className="widgetLgTitle">All Engagements</h3>
      <table className="widgetLgTable">
        <tbody>
          <tr className="widgetLgTr">
            <th className="widgetLgTh">NAME</th>
            <th className="widgetLgTh">ID</th>
            <th className="widgetLgTh">ACTUAL HOURS</th>
            <th className="widgetLgTh">EXPECTED HOURS</th>
          </tr>
          {engagementList}
        </tbody>
      </table>
    </div>
  );
}