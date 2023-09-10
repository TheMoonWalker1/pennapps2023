import React from 'react';
import "../css/Home.css";

function Home(){
    return(
        <body>
            <div class="introduction">
                <h1>SnowPast</h1>
                <h4>this is our catchphrase</h4>
                <button type="button" id="try">Try It</button>
            </div>

            <div>
                <p>Snowpacks are a crucial component of our water cycle. They melt seasonally to provide much-needed influxes to streams and rivers, forming a much-needed drinking water source for communities and regional ecosystems alike.</p>
            </div>
        </body>
        
        
    );
}

export default Home;