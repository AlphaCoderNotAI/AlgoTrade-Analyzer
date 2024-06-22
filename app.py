import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import plotly.express as px
import plotly.graph_objects as go
import os
from typing import List, Tuple, Dict

# Constants
BASE_CAPITAL = 50000  # Initial investment amount
DATA_PATH = 'data/'  # Path to data files

def load_data(file_path: str) -> pd.DataFrame:
    """
    Load and preprocess the data from the given file path.
    
    Args:
    file_path (str): Path to the CSV file.
    
    Returns:
    pd.DataFrame: Preprocessed DataFrame.
    """
    try:
        data = pd.read_csv(file_path)
        data['Date'] = pd.to_datetime(data['Date'], format='%Y-%m-%d')
        data['weekday'] = data['Date'].dt.weekday.map({
            0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 
            3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'
        })
        return data
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        return pd.DataFrame()

def plot_stock_area(df: pd.DataFrame, column: str = 'Profit') -> go.Figure:
    """
    Create an area plot for the given dataframe and column.
    
    Args:
    df (pd.DataFrame): DataFrame containing the data.
    column (str): Column name to plot (default is 'Profit').
    
    Returns:
    go.Figure: Plotly figure object.
    """
    fig = go.Figure(go.Scatter(
        x=df.Date, 
        y=df[column].cumsum(), 
        fill='tozeroy', 
        mode='lines', 
        line_color='yellow'
    ))
    fig.update_layout(
        template='plotly_dark',
        title=f"Cumulative {column} over Time",
        xaxis_title="Date",
        yaxis_title=f"Cumulative {column}",
        margin=dict(l=0, r=0, b=0, t=40),
        plot_bgcolor='rgba(0,0,0,0)'
    )
    return fig

def calculate_risk_metrics(df: pd.DataFrame) -> Tuple[float, float]:
    """
    Calculate Sharpe Ratio and Sortino Ratio.
    
    Args:
    df (pd.DataFrame): DataFrame containing the 'Profit' column.
    
    Returns:
    Tuple[float, float]: Sharpe Ratio and Sortino Ratio.
    """
    returns = df['Pnl_Percentage'] / 100  # Convert percentage to decimal
    risk_free_rate = 0.05 / 252  # Assuming 5% annual risk-free rate
    
    excess_returns = returns - risk_free_rate
    sharpe_ratio = excess_returns.mean() / returns.std() * np.sqrt(252)
    sortino_ratio = excess_returns.mean() / returns[returns < 0].std() * np.sqrt(252)
    
    return sharpe_ratio, sortino_ratio

def calculate_max_drawdown(data: pd.DataFrame) -> Tuple[float, float, timedelta]:
    """
    Calculate the maximum drawdown, its percentage, and duration.
    
    Args:
    data (pd.DataFrame): DataFrame with 'Profit' and 'Date' columns.
    
    Returns:
    Tuple[float, float, timedelta]: (max_drawdown, max_drawdown_percentage, max_drawdown_duration)
    """
    cumulative_profit = data['Profit'].cumsum()
    peak = cumulative_profit.cummax()
    drawdown = peak - cumulative_profit
    
    max_drawdown = drawdown.max()
    max_drawdown_idx = drawdown.idxmax()
    peak_value = peak.loc[max_drawdown_idx]
    
    max_drawdown_percentage = (max_drawdown / peak_value) * 100 if peak_value != 0 else 0
    
    # Calculate drawdown duration
    drawdown_start = (peak != cumulative_profit).idxmax()
    drawdown_end = max_drawdown_idx
    max_drawdown_duration = data.loc[drawdown_end, 'Date'] - data.loc[drawdown_start, 'Date']
    
    return max_drawdown, max_drawdown_percentage, max_drawdown_duration

def main():
    st.set_page_config(page_title="Algo Trading Analysis Dashboard", layout="wide")
    st.title("Algorithmic Trading Performance Analysis")

    # Load all CSV files
    files = [f for f in os.listdir(DATA_PATH) if f.endswith('.csv')]
    data_dict = {f: load_data(os.path.join(DATA_PATH, f)) for f in files}

    # Sidebar for user inputs
    with st.sidebar:
        st.header("Data Selection")
        selected_file = st.selectbox("Select a strategy", files)
        
        st.header("Date Range")
        min_date = min(df['Date'].min() for df in data_dict.values())
        max_date = max(df['Date'].max() for df in data_dict.values())
        start_date = st.date_input("Start Date", value=min_date, min_value=min_date, max_value=max_date)
        end_date = st.date_input("End Date", value=max_date, min_value=min_date, max_value=max_date)
        
        st.header("Weekday Filter")
        weekday_options = ["All"] + ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        weekday = st.selectbox("Select Weekday", weekday_options)

    # Filter data based on user selection
    data = data_dict[selected_file]
    data = data[(data['Date'].dt.date >= start_date) & (data['Date'].dt.date <= end_date)]
    if weekday != "All":
        data = data[data['weekday'] == weekday]

    # Calculate metrics
    total_profit = data["Profit"].sum()
    total_pnl_percentage = data["Pnl_Percentage"].sum()
    avg_trades_per_day = data["No_of_Trades"].mean()
    win_rate = (data["Profit"] > 0).mean() * 100

    # Overall Performance Section
    st.header("Overall Performance")
    st.markdown("---")
    
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(label="Total Profit", value=f"${total_profit:.2f}")
    with col2:
        st.metric(label="Total PNL %", value=f"{total_pnl_percentage:.2f}%")
    with col3:
        st.metric(label="Avg Trades/Day", value=f"{avg_trades_per_day:.2f}")
    with col4:
        st.metric(label="Win Rate", value=f"{win_rate:.2f}%")

    # Profit by Weekday
    st.subheader("Profit by Weekday")
    weekday_profit = data.groupby('weekday')['Profit'].sum()
    st.bar_chart(weekday_profit)

    # Risk Metrics Section
    st.header("Risk Metrics")
    st.markdown("---")
    
    sharpe_ratio, sortino_ratio = calculate_risk_metrics(data)
    max_drawdown, max_drawdown_percentage, max_drawdown_duration = calculate_max_drawdown(data)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Sharpe Ratio", value=f"{sharpe_ratio:.2f}")
    with col2:
        st.metric(label="Sortino Ratio", value=f"{sortino_ratio:.2f}")
    with col3:
        st.metric(label="Max Drawdown", value=f"${max_drawdown:.2f} ({max_drawdown_percentage:.2f}%)")
    with col4:
        st.metric(label="Max Drawdown Duration", value=f"{max_drawdown_duration.days} days")

    # Cumulative Profit Section
    st.header("Cumulative Profit over Time")
    st.markdown("---")
    
    cumulative_profit_plot = plot_stock_area(data)
    st.plotly_chart(cumulative_profit_plot, use_container_width=True)

    # Daily Returns Distribution Section
    st.header("Distribution of Daily Returns")
    st.markdown("---")
    
    fig = px.histogram(data, x="Pnl_Percentage", nbins=50, title="Distribution of Daily Returns (%)")
    st.plotly_chart(fig, use_container_width=True)

    # Trade Analysis Section
    st.header("Trade Analysis")
    st.markdown("---")

    trade_cols = [col for col in data.columns if col.startswith('Trade_')]
    if trade_cols:
        trade_data = data[trade_cols].melt(var_name='Trade', value_name='Return')
        trade_data = trade_data[trade_data['Return'] != 0]  # Remove zero returns
        fig = px.box(trade_data, x='Trade', y='Return', title="Trade Returns by Position")
        st.plotly_chart(fig, use_container_width=True)

    # Strategy Parameters Section
    st.header("Strategy Parameters")
    st.markdown("---")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Index Distance", value=f"{data['Index_Distance'].mean():.2f}")
    with col2:
        st.metric(label="Profit Booking Morning", value=f"{data['Profit_booking_Morning'].mean():.2f}")
    with col3:
        st.metric(label="Trailing Percentage", value=f"{data['Trailing_Percaentage'].mean():.2f}%")

    # Data Table Section
    st.header("Detailed Data")
    st.markdown("---")
    
    st.dataframe(data.style.set_table_styles([{'selector': 'table', 'props': [('display', 'block')]}]))

    # Export functionality
    if st.button("Export Data to CSV"):
        csv = data.to_csv(index=False)
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name=f"{selected_file}_filtered.csv",
            mime="text/csv",
        )

if __name__ == "__main__":
    main()
