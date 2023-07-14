# Automated Trading Bot - Testing 3 different ML algorithms on Stock Price Prediction

An ambitious project aimed at developing an automated trading bot leveraging machine learning algorithms for predicting future stock prices. The utilized algorithms include Long Short-Term Memory (LSTM), Support Vector Regression (SVR), and Gradient Boosting Machines (GBM).

## Contributors

- Andrew Shusterman
- Varun Gangadharan

## Description

This project seeks to implement, test, and compare the performance of three different machine learning algorithms (LSTM, SVR, GBM) in the prediction of future stock prices. Utilizing historical stock price data sourced from Yahoo Finance, we train, validate, and apply our models in an automated trading bot environment. 

The bot interfaces with the Alpaca API for paper trading, allowing for the simulation of trades based on the predictions of our models. Our ultimate goal is to deploy a full-stack application, accessible via the web, where users can observe the bot's performance in real-time.

The software technologies and APIs used in this project include:

- **Python** for the main programming language.
- **Yahoo Finance API (yfinance)** for collecting historical stock price data.
- **Alpaca API** for paper trading and testing the bot.
- **Flask/Django** for backend web development.
- **React/Angular** for frontend web development.
- **Heroku/AWS** for deployment of the full-stack web application.

## Roadmap

- **Research (07/13/2023)**: Exploration of the selected machine learning algorithms and literature review of stock price prediction studies.

- **Data Collection/Processing (07/14/2023 - 07/16/2023)**: Fetch and preprocess historical stock data using the Yahoo Finance API.

- **Algorithm Development + Machine Learning Model Training (07/17/2023 - 07/22/2023)**: Develop and train the selected machine learning models using the prepared stock price data.

- **Testing and Refining Model (07/23/2023)**: Test the performance of the trained models, refine and optimize them based on the results.

- **Applying Model on Data (Actually making bot) (07/25/2023)**: Integrate the optimized models into the automated trading bot and simulate trades using the Alpaca API.

- **Front End Development (TBD)**: Build a user-friendly front end for the trading bot.

- **Deployment (TBD)**: Deploy the full-stack web application, ensuring the trading bot functions in real-time and allowing users to monitor the bot's performance.

## Disclaimer

This project serves educational purposes only and is not intended as real investment advice. The stock market is unpredictable and volatile - utilize this trading bot at your own risk.
