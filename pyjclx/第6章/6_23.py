def convertMillis(millis):
        totalSecond=millis//1000
        currentSecond=totalSecond%60
        totalMinute=totalSecond//60
        currentMinute=totalMinute%60
        currentHour=totalMinute//60
        time=str(currentHour)+':'+str(currentMinute)+':'+str(currentSecond)
        return time
def main():
        millis=eval(input("enter a millis:"))
        print(convertMillis(millis))
main()
