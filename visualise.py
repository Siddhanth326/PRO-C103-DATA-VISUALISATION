import pandas as pd 
import plotly.express as px

#scatter plot
df=pd.read_csv("scatter.csv")
fig=px.scatter(df,x="date",y="cases",color="country")
fig.show()