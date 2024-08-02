import pandas as pd
import plotly.express as px
import streamlit as st

st.markdown('<h1 style="color: yellow; text-align: center; border: dashed white 5px; background-color: grey; margin-bottom: 50px">Dashboard of Weather Forecast</h1>', unsafe_allow_html=True)


st.markdown('Weather forecasting is the science of predicting atmospheric conditions at a specific place and time in the future. It has significantly evolved over the past century, integrating advances in technology, meteorology, and data science to provide increasingly accurate and timely predictions.The Basics of Weather Forecasting Weather forecasts are produced by collecting quantitative data about the current state of the atmosphere, including temperature, humidity, wind speed, and pressure. This data is then input into computer models that simulate atmospheric processes and predict future weather patterns. Forecasts can range from short-term (a few hours ahead) to long-term (several days to weeks).Data CollectionAccurate weather forecasting begins with comprehensive data collection. Weather stations around the world measure atmospheric conditions at ground level, while weather balloons provide data from higher altitudes. Satellites orbiting the Earth offer a global perspective, capturing images and data on cloud cover, sea surface temperatures, and atmospheric moisture. Radar systems track precipitation and storm movements, providing critical information for short-term forecasts.')

st.markdown('Numerical Weather Prediction (NWP)The core of modern weather forecasting is Numerical Weather Prediction (NWP). NWP models use mathematical equations to simulate the behavior of the atmosphere. These models divide the atmosphere into a three-dimensional grid, with each cell representing a specific volume of air. By calculating the changes in atmospheric conditions within each cell over time, NWP models can predict how weather systems will evolve.There are several key NWP models used by meteorologists, including the Global Forecast System (GFS) and the European Centre for Medium-Range Weather Forecasts (ECMWF). These models differ in their resolution, data assimilation techniques, and forecast ranges, but they all rely on the same fundamental principles of physics and mathematics.Ensemble ForecastingOne of the main challenges in weather forecasting is the inherent uncertainty in predicting the future state of the atmosphere. To address this, meteorologists use ensemble forecasting. This approach involves running multiple simulations with slightly different initial conditions to create a range of possible outcomes. By analyzing the spread and likelihood of these outcomes, forecasters can provide probabilistic forecasts, offering a measure of confidence in their predictions.')

st.markdown('Advancements in Technology.Recent advancements in technology have greatly enhanced weather forecasting. High-performance computing allows for more complex and detailed NWP models, leading to improved accuracy. Machine learning and artificial intelligence are increasingly being used to analyze vast amounts of data, identify patterns, and refine forecasts. Additionally, the proliferation of personal weather stations and smartphone apps provides real-time, hyper-local data that can be integrated into forecasting models.')

st.markdown('Communication and Impact.Effective weather forecasting is not just about producing accurate predictions; its also about communicating these predictions to the public in a clear and actionable manner. Meteorologists use a variety of platforms, including television, radio, websites, and mobile apps, to disseminate weather information. Alerts and warnings for severe weather events, such as hurricanes, tornadoes, and blizzards, are crucial for public safety and preparedness.')

st.markdown('Conclusion.Weather forecasting has come a long way from its early days of relying on simple observations and empirical rules. Today, it is a sophisticated science that leverages cutting-edge technology and complex models to provide accurate and timely predictions. As technology continues to advance, weather forecasting will become even more precise, helping societies better prepare for and respond to atmospheric conditions.')


st.image('Assets\image1.jpeg',use_column_width=True)
st.image('Assets\image53.jpeg',use_column_width=True)
st.image('Assets\image52.jpeg',use_column_width=True)


st.markdown('<h1 style ="color: green; border: dashed white 5px;margin-bottom:50px">About the Dataset</h1>',unsafe_allow_html=True)

df=pd.read_csv(r'C:\Users\Tariq\Desktop\weather_dataset\datasets\testset.csv', encoding='latin')
st.dataframe(df)

def format_date(dt):
    parts = list(dt)
    year = "".join(parts[:4])
    month = "".join(parts[4:6])
    day = "".join(parts[6:8])
    date = f"{year}-{month}-{day}"
    time = dt.split('-')[-1]
    fdate = f"{date} {time}"
    return fdate
df['date'] = df['Dates_UTC'].apply(format_date)





