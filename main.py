import streamlit as st
from fiancial_statement.statement import financial_statement

# Streamlit UI
st.title("Financial Statement Viewer")

ticker = st.text_input("Enter Ticker Symbol (e.g., AAPL):")
period = st.radio("Select Period:", ('Yearly', 'Quarterly'))

if st.button("Fetch Data"):
    if ticker:
        fs = financial_statement(ticker, period)
        if period == 'Yearly':
            balance_sheet = fs.balance_sheet(ticker, 'yearly')
            cashflow = fs.cashflow(ticker, 'yearly')
            income_statement = fs.income_statement(ticker, 'yearly')
        else:
            balance_sheet = fs.balance_sheet(ticker, 'quarterly')
            cashflow = fs.cashflow(ticker, 'quarterly')
            income_statement = fs.income_statement(ticker, 'quarterly')
        
        st.write("Balance Sheet:\n", balance_sheet)
        st.write("Cashflow:\n", cashflow)
        st.write("Income Statement:\n", income_statement)
    else:
        st.warning("Please enter a valid ticker symbol.")
