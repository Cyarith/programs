import time as datetime
programs = ["Coronation Street","Eastenders","Emmerdale","Hollyoaks"]
times = ["20:00","19:30","19:00","18:30"]
def displayTime():
    print("========================================")
    print("Welcome to the TV Listings Program")
    print("Today's date:",datetime.strftime("%x"))
    print("Current time:",datetime.strftime("%X"))
    print("========================================")
def displayProgram():
    print()
    print(program,"is on tommorow at",time)
    print("Press 'Enter' to get the next program")
    input()
    print()

for counter in range(4):
    displayTime()
    program = programs[counter]
    time = times[counter]
    displayProgram()
