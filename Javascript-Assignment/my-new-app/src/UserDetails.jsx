import React from "react";

function UserDetails({ age, email, city}){
return (
    <div style={styles.details}>
    <p>
        <strong>Email:</strong> {email}
    </p>
    <p>
        <strong>City :</strong> {city}
    </p>
    <p>
        <strong>Age:</strong> {age}
    </p>
    </div>
);
};

const styles = {
details: {
    marginTop: "10px",
    fontSize: "14px",
    color: 'darkslategray'
},
};

export default UserDetails;
