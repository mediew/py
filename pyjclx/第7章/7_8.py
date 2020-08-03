from stopwatch import stopwatch
sw=stopwatch()
count=1
sw.start()
while count<=1000000:
        count+=1
sw.stop()
print(sw.getElapsedTime())
