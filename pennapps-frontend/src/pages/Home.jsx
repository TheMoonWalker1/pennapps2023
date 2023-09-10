import React from 'react';
import "../css/Home.css";

function Home(){
    return(
        <body>

            <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter&display=swap');
            </style>
            <div class="introduction">
                <h1 id="snowpastName">SnowPast</h1>
                <h4 id="tagline"> Predicting natural disasters using historical data</h4>
                <a href = "/demo" id="try">Try It</a>
            </div>

            <div id="questionBox">
                <h2 id="questionToAsk">How can we forecast and help others mitigate the effects of less or more snowpack?</h2>
                <div id="infoBoxes">
                <div id="snowpacksWater">
                <p>Snowpacks are a crucial component of our water cycle. They melt seasonally to provide much-needed influxes to streams and rivers, forming a much-needed drinking water source for communities and regional ecosystems alike.</p>
                </div>
                <div>
                    <p>Climate change is disrupting how snowpacks form and melt. Unprecedented variation in weather patterns threaten wildlife and agricultural industries by severely reducing or increasing the amount of freshwater present in localities.</p>
                </div>
            </div>
            </div>

            
            <div id="solutionBoxes">
                <h2>Introducing SnowPast</h2>
                <div>
                    <p>SnowPast is an XGBoost-powered ML solution that analyses historic data to predict how much water will be produced by melting snowpacks, allowing municipal authorities and nongovernmental organisations to better prepare for outlier events.</p>
                    <p>SnowPast considers variables including precipitation, humidity, vapour pressure, latitude and longitude, and terrain curvature as potential predictors for snowpack melting. Optimal predictive power results from coupling our decision tree model with a dataset of roughly 100,000 data points from 900 sources.</p>
                    <p>We produce an intuitive Snow Water Equivalent (SWE) - the height of the water if all of the snowpack melts, which allows legislators to efficiently make informed and accurate decisions regarding mitigation.</p>

                </div>
          
            </div>
            

            <div>
            </div>
        </body>
        
        
    );
}

export default Home;