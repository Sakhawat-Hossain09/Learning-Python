import time
def countdownProgram():
    try:
        enteredTime = input("How long do you want the timer to last [Hour:Minute:Second] : ")
        enteredHour = int(enteredTime[0:2])
        enteredMinute = int(enteredTime[3:5])
        enteredSecond = int(enteredTime[6:8])       
        totalSeconds = enteredHour*3600+enteredMinute*60+enteredSecond
        for i in range(totalSeconds, 0, -1):
            displayingSecond = i%60
            displayingMinute = int(i/60)%60
            displayingHour = int(i/3600)%60
            print(f"{displayingHour:02}:{displayingMinute:02}:{displayingSecond:02}")
            time.sleep(1)
        print("Countdown finished successfully.")
    except: ValueError
    print("Check if entered values are correct.")
