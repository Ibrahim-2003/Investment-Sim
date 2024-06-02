import os,pyperclip
os.system('clear')

j=360000
increment = 50000
log = ''

def shagil(i):
    m = income*((1+annual_returns/100)**i)
    return m

def taxed(i):
    m = (income*(1-tax/100))*((1+annual_returns/100)**i)
    return m

def spend(i):
    m = ((income*(1-tax/100))-spending)*((1+annual_returns/100)**i)
    return m

def sigma(low,high,expression):
    return sum(expression(i) for i in range(low,high+1))

while (j<364000):
    income = j
    annual_returns = 20
    tax = 35
    spending = 100000
    time = 2050-2022

    

    summ = sigma(0,time,shagil)
    sumt = sigma(0,time,taxed)
    sumi = sigma(0,time,spend)
    print(f'Calculation Assumptions:\n\nIncome\t\t${income:,.2f}\nAnnual ROI\t{annual_returns:,.2f}%\nTax\t\t{tax:,.2f}%\nSpending\t${spending:,.2f}\nTime\t\t{time} Years')
    hline = '_'*20
    log+=f'Calculation Assumptions:\n\nIncome\t\t${income:,.2f}\nAnnual ROI\t{annual_returns:,.2f}%\nTax\t\t{tax:,.2f}%\nSpending\t${spending:,.2f}\nTime\t\t{time} Years\n'

    print(hline + '\n')
    log+=f'{hline}\n'
    log+=f'\nNon-Taxed\t\tTaxed\t\t\tSpending w/ Tax\n${summ:,.2f}\t\t${sumt:,.2f}\t\t${sumi:,.2f}\n\n'
    print(f'Non-Taxed\t\tTaxed\t\t\tSpending w/ Tax\n${summ:,.2f}\t\t${sumt:,.2f}\t\t${sumi:,.2f}\n')
    j+=increment

pyperclip.copy(log)
perc = 990000/10000 *100
print(f'{perc:.2f}%')