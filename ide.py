# Write your code here :-)
import time
current_year = int(time.strftime("%Y"))
recieved_year = int(input('What year did you get your passport? '))
if recieved_year + 10 < current_year:
    print("You should get a new passport")
else:
    print("you can use your current passport")

print("the big blackbox")
