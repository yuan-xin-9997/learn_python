print(__name__)
loan_total_amount = 121.082016  # 贷款金额，单位: W
loan_year_rate = 3.85  # 贷款年利率，单位%
loan_term = 360  # 还款月数

_loan_year_rate = loan_year_rate / 100  # 贷款年利率
_loan_month_rate = _loan_year_rate / 12  # 贷款月利率

# 计算月供
monthly_repay = loan_total_amount * (_loan_month_rate * (1 + _loan_month_rate) ** loan_term) / (
        (1 + _loan_month_rate) ** loan_term - 1)
print(f"月供：{monthly_repay} 万元")

# 计算累计还款（累计还的本金利息之和）
loan_total_repay = (loan_term * loan_total_amount * _loan_month_rate * (1 + _loan_month_rate) ** loan_term) / (
            (1 + _loan_month_rate) ** loan_term - 1)
print(f"累计还款：{loan_total_repay} 万元")

# 计算累计利息
loan_interest_amount = loan_total_repay - loan_total_amount  # 贷款产生的利息总额，单位：W
print(f"贷款产生的总利息：{loan_interest_amount} 万元")
