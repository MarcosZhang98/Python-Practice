month=0
annual_salary=float(input('what is your annual salary?'))
z=annual_salary
bisection_counter=0
low=0
high=10000
rate=high+low/2
semi_annual_raise=0.07
down_payment=250000
current_savings=0.0
while abs(current_savings-down_payment)>100:
    for y in range(36):
        if y%6==0 and y>1:
            annual_salary+=annual_salary*semi_annual_raise
        current_savings+=current_savings*float(4)/1200
        current_savings+=(annual_salary/float(12))*(rate/10000.0)
    bisection_counter+=1
    if abs(current_savings-down_payment)>100 and current_savings>down_payment:
        high=rate
    elif abs(current_savings-down_payment)>100 and current_savings<down_payment:
        low=rate
    else:
        break
    rate=(high+low)/2
    current_savings=0.0
    annual_salary=z
    if rate==10000:
        break
if rate==10000:
    print('cannot afford household')
else:
    print('your best savings rate is',rate/10000)
    print(bisection_counter)
    
    
    