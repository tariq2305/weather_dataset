import pandas as pd
import plotly.express as px
import streamlit as st

df=pd.read_csv(r'C:\Users\Tariq\Desktop\weather_dataset\datasets\testset.csv', encoding='latin')
st.title('weather forecast dashboard')

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

df['date'] = pd.to_datetime(df.date, format=r"%Y-%m-%d %H:%M", yearfirst=True)

df = df.set_index('date')

st.markdown('Dew Points of Six Months')
result1 = df['Dew_point'].resample('6ME').sum()
fig1 = px.area(result1, result1.index, result1.values)
st.plotly_chart(fig1)

st.markdown('Humidity for Six Year')
result16=df['Humidity'].resample('6YE').sum()
fig2=px.pie(result16,result16.index,result16.values)
st.plotly_chart(fig2)

st.markdown('Humidity for Six Month')
result2 = df['Humidity'].resample('6ME').sum()
fig3=px.area(result2, result2.index, result2.values,title= "Sum of 6 months Humidity")
st.plotly_chart(fig3)

st.markdown('Pressure for Six Year')
result15=df['Pressure'].resample('6YE').mean()
fig4=px.pie(result15,result15.index,result15.values,title='Mean Pressure for 6 year')
st.plotly_chart(fig4)


st.markdown('Pressure for 12 Year')
result4=df['Pressure'].resample('12YE').max()
fig5=px.bar(result4,result4.index,result4.values,title="Max Pressure for 6 year",barmode='relative')
st.plotly_chart(fig5)

st.markdown('Pressure for Six Month')
result6=df['Pressure'].resample('6ME').agg(['min','max'])
fig6=px.bar(result6,result6.index,'min','max',title="Sum of pressure for 6 months(Bar graph)")
st.plotly_chart(fig6)

st.markdown('Pressure for Six Year')
result7=df['Pressure'].resample('6YE').sum()
px.area(result7,result7.index,result7.values,title="Sum of pressure for 6 year(AREA GRAPH) ")
st.plotly_chart(fig5)

st.markdown('Pressure for 12 Month')
result8=df['Pressure'].resample('12ME').agg(['mean','min','max'])
fig6=px.area(result8,result8.index,['mean','min','max'],title="Aggregate Pressure of 12 month ")
st.plotly_chart(fig6)


st.markdown('Temperature for Six Year')
result9=df['Temperature'].resample('6YE').sum()
fig7=px.area(result9,result9.index,result9.values,title="Temperature record for 6 year")
st.plotly_chart(fig7)




st.markdown('Pressure for Six Year')
result10=df['Pressure'].resample('6YE').sum()
fig8=px.line(result10,result10.index,result10.values,title="Temperature record for 6 year(Line Graph)")
st.plotly_chart(fig8)


st.markdown('Temperature for Six Month')
result11=df['Temperature'].resample('6ME').agg(['mean','min','max'])
fig9=px.area(result11,result11.index,['mean','min','max'],title = "Aggregate Temperature for 6 Months(AREA Graph)")
st.plotly_chart(fig9)


st.markdown('Temperature for Year')
result12=df['Temperature'].resample('YE').agg(['mean','min','max'])
fig10=px.bar(result12,result12.index,['mean','max','min'], title="Max Temperature Per Year in Fahrenheit", barmode='group')
st.plotly_chart(fig10)


st.markdown('Temperature for Six Year')
result13=df['Temperature'].resample('6YE').mean()
fig11=px.histogram(result13,result13.index,result13.values,title= "Temperature record for 6 years")
st.plotly_chart(fig11)


st.markdown('Pressure for Year')
result7=df['Pressure'].resample('YE').sum()
fig12=px.histogram(result7,result7.index,result7.values,title = "Pressure for years in the series")
st.plotly_chart(fig12)

st.markdown('Wildpanel for Six Year')
result14=df['Wildpanel'].resample('6YE').sum()
fig13=px.pie(result14,result14.index,result14.values,title="Wildpanel for 6 year in the series")
st.plotly_chart(fig13)

st.markdown('Wildpanel for Six Year')
result17=df['Wildpanel'].resample('6YE').mean()
fig14=px.line(result17,result17.index,result17.values,title =" Aggregate Wildpanel for 6 year")
st.plotly_chart(fig14)

st.markdown('Wildpanel for 12 Year')
result18=df['Wildpanel'].resample('12YE').mean()
fig15=px.histogram(result18,result18.index,title=" Sum of 12Year Wildpanel Records ")
st.plotly_chart(fig15)

