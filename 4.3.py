years = int(input('How many years do you want to track? '))

months = 12

grandTotal = 0.0

for years_rain in range(years):

    total= 0.0

    print('\nYear number', years_rain + 1)
    print('------------------------------')
    for month in range(months):
        print('How many inches for month ', month + 1, end)
        rain = int(input(' did it rain? '))






print('The total inches of rain was ', format(average, '.2f'),'.')
print('The number of months measured was', number_months)
print('The average rainfall was', format(average, '.2f'), 'inches')
