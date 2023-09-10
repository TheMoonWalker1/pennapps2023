import React, { useState } from 'react';
import axios from 'axios';

function MyComponent() {
  const [latitude, setLatitude] = useState(0); // Initialize with default values
  const [longitude, setLongitude] = useState(0);

  const sendRequest = () => {
    // Fetch the CSRF token from the Django server by making a GET request
    axios.get('/csrf/').then((response) => {
      // Extract the CSRF token from the response
      const csrfToken = response.data.csrfToken;

      // Include the CSRF token in the request headers
      axios
        .post(
          '/ajax/',
          {
            latitude: latitude,
            longitude: longitude,
          },
          {
            headers: {
              'X-CSRFToken': csrfToken,
            },
          }
        )
        .then((response) => {
          // Handle the response from Django here
          console.log(response.data);
        })
        .catch((error) => {
          // Handle any errors here
          console.error(error);
        });
    });
  };

  return (
    <div>
      <input
        type="text"
        placeholder="Latitude"
        onChange={(e) => setLatitude(e.target.value)}
      />
      <input
        type="text"
        placeholder="Longitude"
        onChange={(e) => setLongitude(e.target.value)}
      />
      <button onClick={sendRequest}>Send Request</button>
    </div>
  );
}

export default MyComponent;
