import yfinance 
import pandas as pd
import numpy as np



class financial_statement:

    def __init__(self, ticker, period):
        self.ticker = ticker
        self.period = period
        return
    
    def stock_name(self,ticker):
        company_data = yfinance.Ticker(ticker= ticker)
        return company_data
    

    def balance_sheet(self, company_name, period):
        company_data = self.stock_name(company_name)
        if period == 'quarterly':
            quarterly_balance_sheet = company_data.quarterly_balance_sheet
            quarterly_balance_sheet.to_excel(f"quarterly_balance_sheet_{company_name}")
            return quarterly_balance_sheet
        else:
            yearly_balance_sheet = company_data.balance_sheet
            yearly_balance_sheet.to_excel(f"year_balance_sheet_{company_name}")
            return yearly_balance_sheet
    
    def cashflow(self, company_name, period):
        company_name = self.stock_name(company_name)
        if period == 'quarterly':
            quarterly_cashflow = company_name.quarterly_cashflow
            quarterly_cashflow.to_excel(f"quarterly_cashflow_{company_name}")
            return quarterly_cashflow
        else:
            yearly_cashflow = company_name.cashflow
            yearly_cashflow.to_excel(f"yearly_cashflow_{company_name}")
            return yearly_cashflow
    
    def income_statement(self, company_name, period):
        company_name = self.stock_name(company_name)
        if period == 'quarterly':
            quarterly_income_statement = company_name.quarterly_income_stmt
            quarterly_income_statement.to_excel(f"quarterly_income_statement_{company_name}")
            return quarterly_income_statement
        else:
            yearly_income_statement = company_name.income_stmt
            yearly_income_statement.to_excel(f"yearly_income_statement_{company_name}")
            return quarterly_income_statement, yearly_income_statement