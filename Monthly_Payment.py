# Prgram to calculate monthly payment with interest

def pay_cal():
    principal = float(input('Enter loan amount:'))
    apr = float(input('Enter annual rate of interest:'))
    years = int(input('Enter time epriod in years:'))

    monthly_apr = apr/1200
    months = years*12
    monthly_payment  = principal*monthly_apr/(1-(1+monthly_apr)**(-months))

    print('The monthly payment is: %.2f' % monthly_payment)

pay_cal()
