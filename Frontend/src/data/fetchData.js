const apiUrl = "http://127.0.0.1:5000/server/api/v1/"




export const fetchAllEngagements = () => {
    
    return (
        fetch(apiUrl.concat('engagement/'),)
        .then(response =>response.json())
        .then(data => {
            // console.log(`length of data ${data.length}`)
            // console.log(data);
            return data;
        })
    );
};

export const fetchEngagement = (id) => {
    return (
        fetch(apiUrl.concat('engagement/' + id),)
        .then(response =>response.json())
        .then(data => {
            // console.log(`length of data ${data.length}`)
            // console.log(data);
            return data;
        })
    );
}

export const fetchAllPhases = (id) => {
    // console.log(id)
    return (
        fetch(apiUrl.concat('phase/' + id),)
        .then(response =>response.json())
        .then(data => {
            // console.log(data)
            return data;
        })
    );
};

export const fetchAllMembers = () => {
    return (
        fetch(apiUrl.concat('member/member_total_hours/'),)
        .then(response =>response.json())
        .then(data => {
            // console.log(data)
            return data;
        })
    );
}

export const fetchMember = (id) => {
    return (
        fetch(apiUrl.concat('member/'+ id),)
        .then(response =>response.json())
        .then(data => {
            // console.log(data)
            return data;
        })
    );
}