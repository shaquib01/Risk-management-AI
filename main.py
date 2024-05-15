# MODULE  USING TO 
SCAPE NEWS ARTICLEL
SCARP STOCK DATA
SCARP FACEBOOK PREDICTION DATA


PIP INSTALL DATA IN LOCAL HOST
CREATE CODE.PY (PYTHON FILE)

IMPORT STREAMLIT AS ST
FROM DATTIME IMPORT DATE
IMPORT YFINANCE 
IMPORT FBPROPHET 
FROM FBPROPHET.PLOT
FROM PLOTLY

START= “2015-01-01”
TODAY=date.today().strrfttime(“%Y-%m-%d”)

#Start web App
st.title(“Stock Prediction App”)
stock =(“AAPL”, “GOOG ,”MSFT”)
selected_stocks=st.selectedbox(“Select dataset fro prediction” , stocks )

n_years=st.slider(“Years of prediction” , 1 ,4 )
period =n_years * 365
# cache data afte downloading 

@st.cache
 # load stop data
Def load_data(ticker):
Data =yf.download(ticker, START,TODAY)
Data.reset_index(inplace=True)
Data_load_state=st.text(“Load data…”)
Data = load_data(selected_stock)
Data_load_state.text(“Loading data…done!”)

st:subheader(‘Raw Data’)
st.write(data.tail())
def plot_raw_date();
fig=go.figure()
fig.add_trace(go.Scatter (x=data[‘Date’] ,y=date[‘Open’], name=’stock_open’))
fig.add_trace(go.Scatter (x=data[‘Date’] ,y=date[‘Open’], name=’stock_close’))
fig.layout.update(title_text=”Time Series Data “ , xaxis_rangeslider_visible=True)
st.plotly_chart(fig)

plot_raw_data()


#Forecasting
df_rain= data[[‘Date’ , ‘Close’]]
df_train=df_train.rename=(columns={“Date”: “ds” ,”Close” : “y”})

m=Prophet{}
m.fit(df_train}
future=m.make_future_dataframe{period=period}
forcast =m.predict{future}

st.subheader(‘Forecast data’)
st.write(data.tail())
st.write(‘forecast data’)
fig1=plot_plotly (m , forecast)
st.plotly_chart(fig1)

st.write(‘forecast componets’)
fig2 =m.plot_componets(forecast)
st.write(fig2)





