# Algorithmic Trading Performance Dashboard

This Streamlit application provides a comprehensive dashboard for analyzing the performance of algorithmic trading strategies. It allows users to visualize and analyze trading data, including profit/loss, risk metrics, and various performance indicators across multiple strategies.

## Features

- Multiple strategy analysis
- Data selection and date range filtering
- Overall performance metrics
- Risk metrics (Sharpe Ratio, Sortino Ratio, Max Drawdown)
- Profit analysis by weekday
- Cumulative profit visualization
- Daily returns distribution
- Individual trade analysis
- Strategy parameter overview
- Detailed data table with export functionality

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/algo-trading-dashboard.git
   cd algo-trading-dashboard
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Place your CSV data files in the `data/` directory. Each CSV file should represent a different trading strategy and have the following columns:
   - Date: The date of the trading day (YYYY-MM-DD format)
   - Profit: The profit/loss for each trading day
   - Pnl_Percentage: The profit/loss as a percentage
   - Trade_Capital: The capital used for each trade
   - Index_Distance: Strategy-specific parameter
   - Profit_booking_Morning: Strategy-specific parameter
   - Profit_booking_AfterNoon: Strategy-specific parameter
   - Trailing_Percaentage: Strategy-specific parameter
   - Profit_booking_AfterNoon_apprx: Strategy-specific parameter
   - No_of_Trades: Number of trades executed
   - Trade_1, Trade_2, etc.: Individual trade returns

2. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

3. Open your web browser and go to the URL displayed in the terminal (usually `http://localhost:8501`).

4. Use the sidebar to select your strategy (CSV file), set date ranges, and apply filters.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
