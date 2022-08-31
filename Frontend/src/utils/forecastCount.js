

export const getNextWeekDays = (date = new Date()) => {
    const dateCopy = new Date(date.getTime());

    let nextWeekDays = []

    for (let i = 1; i <= 5; i++){
        let weekday = 
            new Date(
                dateCopy.setDate(
                    dateCopy.getDate() + ((7 - dateCopy.getDay() + i) % 7 || 7)
                )
        )
        
        nextWeekDays.push(weekday.toString().split(' ').slice(0,3).join(' '))
        
    }
    return nextWeekDays;
}