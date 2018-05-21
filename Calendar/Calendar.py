class Date:

    daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    weekDays = [5, 6, 0, 1, 2, 3, 4]


    def __init__(self, S, form = "%m/%d/%Y"):
        splitter = form[2]
        L = list(map(int, S.split(splitter)))

        for x in range(1, 8, 3):
            if S[x] == "m":
                self.month = L[x//3]
            elif S[x] == "d":
                self.day = L[x//3]
            else:
                self.year = L[x//3]


    defDate = Date("01/01/0001")
    def isEqual(self, compDate):
        if self.year == compDate.year:
            if self.month == compDate.month:
                if self.day == compDate.day:
                    return True

        return False

    def getDaysAway(self, fromDate = self.defDate):

        daysAwayLastYear = ((self.year-1)*365)+((self.year-1)//4)-1
        daysThisYear = sum(daysInMonth[:self.month])+self.day
        daysAwayFrom = 0
        if self.year%4==0:
            daysThisYear += 1

        if not fromDate.isEqual(self.defDate):
            daysAwayFrom = fromDate.getDaysAway()

        return daysAwayLastYear+daysThisYear-daysAwayFrom

    def getWeekday(self):



        return weekDays[self.getDaysAway()%7]
