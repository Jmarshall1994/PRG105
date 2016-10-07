def WriteAvg(outfile, year, month, avg):
    Data = [year, month, avg, '\n']
    Data = ' '.join(Data)
    outfile.write(str(Data))

def OpenFile(File):
    outfile = open ("Monthlytemp.txt","w")
    PrevMonth = ""
    PrevYear = ""
    SpotSum = 0
    Days = 0

    try:
        Lines= open(File).readlines()
    except IOError:
        Lines=[]
    for line in Lines:
        Dates = line.split()
        Year= str(Dates[0][0:4])
        Month = str(Dates[0][4:6])
        Date = str(Dates [0][6:8])
        Spots = int(Dates [2])
        if PrevMonth != Month & PrevMonth!="":
            MonthAvg = str(SpotSum*1./Days)
            WriteAvg(outfile, PrevYear, PrevMonth, MonthAvg)
            Days = 0
            SpotSum = 0
        if Spots!= 999:
            Days +=1
            SpotSum += Spots
        PrevMonth = Month
        PrevYear = Year

    MonthAvg = str(SpotSum*1./Days)
    WriteAvg(outfile, PrevYear, PrevMonth, MonthAvg)

    outfile.close()
    return Data

    print(WriteAvg)
