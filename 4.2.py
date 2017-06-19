def main():

    ndays = input('Enter the number of days')

    pay = 0.005


    for day in range(1,ndays+1):

        pay *= 2.0
        print ' Day', day, ' Salary', pay


    print 'Your salary on day', ndays, 'would be $%.2f' % pay


main()
