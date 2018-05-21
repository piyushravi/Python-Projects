class Date:

    daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    weekDays = [6, 0, 1, 2, 3, 4, 5]




    def __init__(self, S, form = "%m/%d/%Y"):
        splitter = form[2]
        L = list(map(int, S.split(splitter)))
        #print(L)
        for x in range(1, 8, 3):
            #print(x, S[x], L[x//3], x//3)
            if form[x] == "m":
                self.month = L[x//3]
            elif form[x] == "d":
                self.day = L[x//3]
            else:
                self.year = L[x//3]



    def isEqual(self, compDate):
        if self.year == compDate.year:
            if self.month == compDate.month:
                if self.day == compDate.day:
                    return True

        return False

    def getDaysAway(self, fromDate = None):

        daysAwayLastYear = ((self.year-1)*365)+((self.year-1)//4)-1
        daysThisYear = sum(self.daysInMonth[:self.month-1])+self.day
        daysAwayFrom = 0
        if self.year%4==0 and self.month > 2:
            daysThisYear += 1

        if fromDate != None:
            daysAwayFrom = fromDate.getDaysAway()

        return daysAwayLastYear+daysThisYear-daysAwayFrom

    def getWeekday(self):

        #print(self.getDaysAway())

        return self.weekDays[self.getDaysAway()%7]


'''
#For testing purpose.
test = Date("5/22/2018")
print(test.getWeekday())
daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
print (sum(daysInMonth))
prev = 5
for year in range(2019):
    if (year+1)%4 == 0:
        daysInMonth[1] = 29
    else:
        daysInMonth[1] = 28
    for month in range(12):
        for day in range(daysInMonth[month]):
            temp = Date(str(month+1)+"/"+str(day+1)+"/"+str(year+1))

            if temp.getWeekday() != ((prev+1)%7):
                print(month+1, day+1, year+1)
                print (temp.getWeekday(), prev, ((prev+1)%7))

            prev += 1
            prev %= 7
'''
