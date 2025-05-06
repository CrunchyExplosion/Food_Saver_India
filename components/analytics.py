import streamlit as st
import pandas as pd
import numpy as np

@st.cache_data
def create_dummy_data():
    items = [
        'Tomato', 'Potato', 'Onion', 'Carrot', 'Cabbage', 'Spinach', 'Apple', 'Banana', 'Mango', 'Grapes',
        'Cauliflower', 'Broccoli', 'Pumpkin', 'Radish', 'Cucumber', 'Pineapple', 'Lettuce', 'Beans', 'Peas', 'Papaya'
    ]
    locations = ['Delhi', 'Mumbai', 'Bengaluru', 'Chennai', 'Kolkata']

    data = []
    for item in items:
        for loc in locations:
            for month in range(1, 13):
                temp = np.random.uniform(20, 40)
                rain = np.random.uniform(50, 200)
                past_demand = np.random.randint(80, 400)
                future_demand = 0.3 * temp + 0.5 * rain + 0.2 * past_demand + np.random.normal(0, 20)
                data.append([item, loc, month, temp, rain, past_demand, future_demand])
    
    df = pd.DataFrame(data, columns=['Item', 'Location', 'Month', 'Temperature', 'Rainfall', 'Past_Demand', 'Future_Demand'])
    return df

#---------------------------- manual liner regression Machine learnign model ---------------------------------------------------
@st.cache_resource
def train_manual_linear_regression(df):
    # Features: Temperature, Rainfall, Past_Demand
    X = df[['Temperature', 'Rainfall', 'Past_Demand']].values
    y = df['Future_Demand'].values.reshape(-1, 1)

    # Add bias term (intercept)
    ones = np.ones((X.shape[0], 1))
    X_b = np.hstack([ones, X])

    # Normal equation: theta = (X.T * X)^-1 * X.T * y
    theta = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)
    return theta

def manual_predict(X_input, theta):
    ones = np.ones((X_input.shape[0], 1))
    X_b = np.hstack([ones, X_input])
    return X_b.dot(theta)

def show_analytics():
    st.subheader("Predictive Analytics & Insights")

    st.markdown("### AI-Powered Predictions")

    df = create_dummy_data()
    theta = train_manual_linear_regression(df)

    col1, col2 = st.columns(2)
    with col1:
        selected_item = st.selectbox("Select Item", df['Item'].unique())
    with col2:
        selected_location = st.selectbox("Select Location", df['Location'].unique())

    if selected_item and selected_location:
        item_df = df[(df['Item'] == selected_item) & (df['Location'] == selected_location)]
        if not item_df.empty:
            recent = item_df.sample(1).iloc[0]
            X_input = np.array([[recent['Temperature'], recent['Rainfall'], recent['Past_Demand']]])
            prediction = manual_predict(X_input, theta)[0][0]
            st.metric(f"Predicted Optimal Quantity for {selected_item}", f"{prediction:.2f} kg")

    # Demand forecast across months
    st.subheader("Demand Forecast")
    months = range(1, 13)
    demand_forecast = []
    for month in months:
        subset = df[(df['Item'] == selected_item) & (df['Location'] == selected_location) & (df['Month'] == month)]
        if not subset.empty:
            row = subset.sample(1).iloc[0]
            X_input = np.array([[row['Temperature'], row['Rainfall'], row['Past_Demand']]])
            pred = manual_predict(X_input, theta)[0][0]
        else:
            pred = np.nan
        demand_forecast.append(pred)

    forecast_df = pd.DataFrame({
        'Month': pd.date_range(start='2025-01-01', periods=12, freq='ME'),
        'Predicted Demand': demand_forecast
    })
    st.line_chart(forecast_df.set_index('Month'))

    st.markdown("""
    ### AI-Generated Insights
    - Optimal harvest times based on temperature and rainfall patterns
    - Regional demand predictions based on historical data
    - Surplus and shortage alerts for inventory planning
    """)

