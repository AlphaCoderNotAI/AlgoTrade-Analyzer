# AlgoTrade-Analyzer

[![GitHub release](https://img.shields.io/github/release/AlphaCoderNotAI/AlgoTrade-Analyzer.svg)](https://GitHub.com/AlphaCoderNotAI/AlgoTrade-Analyzer/releases/)
[![GitHub license](https://img.shields.io/github/license/AlphaCoderNotAI/AlgoTrade-Analyzer.svg)](https://github.com/AlphaCoderNotAI/AlgoTrade-Analyzer/blob/main/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/AlphaCoderNotAI/AlgoTrade-Analyzer.svg)](https://GitHub.com/AlphaCoderNotAI/AlgoTrade-Analyzer/stargazers/)


AlgoTrade-Analyzer is a powerful, Streamlit-based dashboard for analyzing and visualizing algorithmic trading performance. It provides comprehensive insights into trading strategies, risk metrics, and performance indicators.

## 📊 Dashboard Preview

### 🎥 See AlgoTrade-Analyzer in Action

Watch a quick demo of AlgoTrade-Analyzer to see its powerful features and intuitive interface:

<p align="center">
  <video src="https://github.com/AlphaCoderNotAI/AlgoTrade-Analyzer/assets/173565780/0a4e59de-bcc8-47cb-a7d1-f8af1d0ba482" width="480" height="360" controls>
    Your browser does not support the video tag.
  </video>
</p>

<p align="center">
  <i>Watch the demo video above to see AlgoTrade-Analyzer in action</i>
</p>

## 🚀 Features

- **Multi-Strategy Analysis**: Compare performance across different trading algorithms
- **Interactive Data Filtering**: Select specific date ranges and trading days
- **Comprehensive Performance Metrics**: 
  - Total Profit/Loss
  - Percentage Returns
  - Average Trades per Day
  - Win Rate
- **Advanced Risk Analysis**:
  - Sharpe Ratio
  - Sortino Ratio
  - Maximum Drawdown (amount and duration)
- **Visual Analytics**:
  - Cumulative Profit Over Time
  - Profit Distribution by Weekday
  - Daily Returns Distribution
  - Individual Trade Performance
- **Strategy Insights**: Key parameter overview
- **Data Export**: Download filtered data for further analysis

## 🛠️ Installation

1. Clone the repository:
   ```
   git clone https://github.com/AlphaCoderNotAI/AlgoTrade-Analyzer.git
   cd AlgoTrade-Analyzer
   ```

2. Install required packages:
   ```
   pip install -r requirements.txt
   ```

## 🖥️ Usage

1. Place your CSV files in the `data/` directory.
2. Run the Streamlit app:
   ```
   streamlit run app.py
   ```
3. Open your web browser and go to `http://localhost:8501`
4. Use the sidebar to select strategies and set filters.

## 📁 Data Format

Ensure your CSV files have the following columns:
- Date
- Profit
- Pnl_Percentage
- Trade_Capital
- Index_Distance
- Profit_booking_Morning
- Profit_booking_AfterNoon
- Trailing_Percaentage
- No_of_Trades
- Trade_1, Trade_2, etc. (individual trade returns)

### Sample Data Preview

Here's a preview of what your data should look like:

| Date       | Profit  | Pnl_Percentage | Trade_Capital | Index_Distance | Profit_booking_Morning | Profit_booking_AfterNoon | Trailing_Percaentage | No_of_Trades | Trade_1 | Trade_2 |
|------------|---------|----------------|---------------|----------------|------------------------|---------------------------|----------------------|--------------|---------|---------|
| 2024-06-18 | 100.0   | 0.2            | 50000.0       | 35.0           | 25                     |                           | 30                   | 1            | 0.2     |         |
| 2024-06-19 | 150.0   | 0.3            | 50000.0       | 35.0           | 25                     |                           | 30                   | 1            | 0.3     |         |
| 2024-06-20 | -50.0   | -0.1           | 50000.0       | 35.0           | 25                     |                           | 30                   | 1            | -0.1    |         |

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

Venkateshwar Jambula
- LinkedIn: [https://www.linkedin.com/in/venkateshwar-jambula/](https://www.linkedin.com/in/venkateshwar-jambula/)
- Email: venkateshwar.jambula@gmail.com

Project Link: [https://github.com/AlphaCoderNotAI/AlgoTrade-Analyzer](https://github.com/AlphaCoderNotAI/AlgoTrade-Analyzer)

## 🙏 Acknowledgements

- [Streamlit](https://streamlit.io/)
- [Plotly](https://plotly.com/)
- [Pandas](https://pandas.pydata.org/)
