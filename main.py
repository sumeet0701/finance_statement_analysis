import streamlit as st 
import yfinance as yf

def ticker_building(ticker_name):
    stock = yf.Ticker(ticker_name)
    return stock

def display_balance_sheet(company_name, period):
    if period == "Yearly":
        balance_sheet = company_name.balance_sheet
        st.subheader("Yearly Balance Sheet")
        st.write(balance_sheet)
    else:
        balance_sheet = company_name.quarterly_balance_sheet
        st.subheader("Quartely Balance Sheet")
        st.write(balance_sheet)


def display_cash_flow(company_name, period):
    if period == "Yearly":
        cashflow = company_name.cashflow
        st.subheader("Cash Flow Statement")
        st.write(cashflow)
    else:
        cashflow = company_name.quarterly_cashflow
        st.subheader("Cash Flow Statement")
        st.write(cashflow)


def display_income_statment(company_name, period):
    if period == "Yearly":
        income_statment = company_name.income_stmt
        st.subheader("Income Statement")
        st.write(income_statment)
    else:
        income_statment = company_name.quarterly_income_stmt
        st.subheader("Income Statement")
        st.write(income_statment)

def main():
    st.title("Financial Statements")
    company_name = st.text_input("Enter the company Ticker Symbol")
    stock = ticker_building(company_name)
    if stock is not None:
        period = st.radio("Select the period", ("Quarterly", "Yearly"))
        if st.button("Balance sheet"):
            display_balance_sheet(stock, period)
        elif st.button("cashflow"):
            display_cash_flow(stock, period)
        elif st.button("Income Statement"):
            display_income_statment(stock, period)

if __name__ == "__main__":
    main()