import React from 'react';

function Demo(){
    return(
        <body>
            <p>The application requires the identification of </p>
            <form>
                <label for="longitude">Longitude
                    <input type="text" id="longitude" name="longitude"/>
                </label>
                
                <label for="Latitude">Latitude
                    <input type="text" id="latitude" name="latitude"/>
                </label>
                
                <input type="submit" value="Submit"/>
            </form>
        </body> 
        
        
    );
}

export default Demo;