import time
class Time:
    '''Играем со временем'''

    def __init__(self, Hours, Mins, Seconds):
        self.Hours = Hours
        self.Mins = Mins
        self.Seconds = Seconds

    def Metodi(self, Hours, Mins, Seconds):
        print(Hours * 3600 + Mins * 60 + Seconds)
        while Hours < 24:
            time.sleep(1)
            Seconds = Seconds + 1
            if Seconds > 59:
                Seconds = 0
                Mins += 1
            elif Mins > 59:
                Mins = 0
                Hours += 1
            print(Hours, ":", Mins, ":", Seconds)


print('enter hours')
Hours = int(input())
print('enter mins')
Mins = int(input())
print('enter seconds')
Seconds = int(input())
opred = Time(Hours, Mins, Seconds)
opred.Metodi(opred.Hours, opred.Mins, opred.Seconds)