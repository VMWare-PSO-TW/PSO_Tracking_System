// base data
const basePeriod = 3;
const baseStartYear = 2022;
const baseStartMonth = 7;
const baseStartDay = 30;

const baseEndYear = 2022;
const baseEndMonth = 10;
const baseEndDay = 28;




const getNextPeriod = (year, month, day) => {
    const nextDate = new Date(`${year}-${month}-${day}`);
    nextDate.setDate(nextDate.getDate() + 13 * 7);

    const nextYear = nextDate.getFullYear();
    const nextMonth = nextDate.getMonth() + 1;
    const nextDay = nextDate.getDate();

    return [nextYear, nextMonth, nextDay]
}


export const getCurrentPeriod = () => {
    const date = new Date();


    // today's date
    let curPeriod = basePeriod;

    let curDate = new Date();
    let curYear = curDate.getFullYear();
    let curMonth = curDate.getMonth() + 1;
    let curDay = curDate.getDate();
    let curCost = date.getTime();

    // start date
    let startYear = baseStartYear
    let startMonth = baseStartMonth
    let startDay = baseStartDay
    let startCost = new Date(`${startYear}-${startMonth}-${startDay}`)

    // end date
    let endYear = baseEndYear
    let endMonth = baseEndMonth
    let endDay = baseEndDay
    let endCost = new Date(`${endYear}-${endMonth}-${endDay}`)
   


    while ( ((curCost > endCost.getTime()) || (curCost < startCost.getTime()))){
        const startDate = getNextPeriod(startYear, startMonth, startDay)
        startYear = startDate[0]
        startMonth = startDate[1]
        startDay = startDate[2]
        startCost = new Date(`${startYear}-${startMonth}-${startDay}`)

        const endDate = getNextPeriod(endYear, endMonth, endDay)
        endYear = endDate[0]
        endMonth = endDate[1]
        endDay = endDate[2]
        endCost = new Date(`${endYear}-${endMonth}-${endDay}`)

        curPeriod += 1

        if (curPeriod > 4){
            curPeriod = 1
        }

    }
    return ({
        startDate: `${startMonth}-${startDay}-${startYear}`,
        endDate: `${endMonth}-${endDay}-${endYear}`,
        curDate: `${curMonth}-${curDay}-${curYear}`,
        curPeriod: curPeriod
    })

}


export const getAllRates = (startDate, curDate, members) => {
    // console.log('get all rates');
    const [startMonth, startDay, startYear] = startDate.split("-");
    let startDateTime = new Date(`${startYear}-${startMonth}-${startDay}`)

    const [curMonth, curDay, curYear] = curDate.split("-");

    let curDateTime = new Date(`${curYear}-${curMonth}-${curDay}`)

    let diffDays = (curDateTime.getTime() - startDateTime.getTime()) / (1000 * 3600 * 24);

    let upToDateHours =  Math.floor(diffDays / 7) * 40 + ((diffDays % 7) - 1) * 8

    let totalActualHours = 0;
    let totalExpectHours = 0;

    for (let i = 0; i < members.length; i++){
        // console.log(members[i].total_actual)
        // console.log(members[i].total_expect)
        totalActualHours += members[i].total_actual;
        totalExpectHours += members[i].total_expect;
    }

    const allUTRate = parseInt(((totalActualHours / (upToDateHours * members.length)) * 100).toFixed(2), 10);
    const allCompleteRate = parseInt(((totalActualHours / totalExpectHours) * 100).toFixed(2), 10);

    // console.log(allUTRate)
    return(
            { 
                allUTRate: allUTRate, 
                allCompleteRate: allCompleteRate
            }
        );
    
}

