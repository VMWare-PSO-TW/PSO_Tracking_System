const apiUrl = "http://127.0.0.1:5000/server/api/v1/"




export const fetchAllEngagements = () => {
    
    return (
        fetch(apiUrl.concat('engagement/'),)
        .then(response =>response.json())
        .then(data => {
            // console.log(`length of data ${data.length}`)
            return data;
        })
    );
};

export const fetchAllPhases = (id) => {
    
    return (
        fetch(apiUrl.concat('phase/' + id),)
        .then(response =>response.json())
        .then(data => {
            // console.log(data)
            return data;
        })
    );
};

