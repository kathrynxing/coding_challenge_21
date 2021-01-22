import sys

filename = sys.argv[1]
f = open(filename,'r')
# f = open('j4/j4.03.in', 'r')
D = int(f.readline().strip())
# the total num of minutes elapsed on clock = 720
remainder = D % 720
num_cycles = D // 720

# preprocessing 
def clock_tick(time):
    # time <= 720 
    hour = time // 60
    minutes = time % 60
    hour = 12 if hour == 0 else hour
    minutes_str = str(minutes) if minutes>9 else '0'+str(minutes)
    time_str = str(hour)+minutes_str
    return time_str

def check_arithmetic(time_str):
    # time_str is a 3/4 digits str
    diff = int(time_str[0]) - int(time_str[1])
    for i in range(len(time_str)-1):
        value = int(time_str[i]) - int(time_str[i+1])
        if value != diff:
            return False
    return True

def preprocessing():
    tally = 720*[0]
    counter = 0
    for minute in range(720):
        # time string
        time_str = clock_tick(minute)
        # check pattern
        if check_arithmetic(time_str):
            counter += 1
        tally[minute] = counter
    return tally

# a = check_arithmetic('111')
tally = preprocessing()
result = num_cycles*tally[-1] + tally[remainder]
print(result)