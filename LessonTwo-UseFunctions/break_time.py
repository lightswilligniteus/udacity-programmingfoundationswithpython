import webbrowser
import time

#counter for maximum calls for the while loop and counter
count = 0
maxcount = 3

#while loop that is called up to maxcount and opens a web browser
#every 2 hours.
while count < maxcount:
    time.sleep(7200)
    webbrowser.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")
    count = count + 1
