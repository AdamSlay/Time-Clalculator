def add_time(start_time, duration, day = None):
# Starting/setup variables
    start = start_time.split(' ')
    stime = start[0].split(':')
    dtime = duration.split(':')


# Variables in use
    start_hour = int(stime[0])
    start_min = int(stime[1])    
    dur_hour = int(dtime[0]) # duration hours
    dur_min = int(dtime[1])  # duration minutes
    final_hour = start_hour + dur_hour # total hours 
    final_min =  start_min + dur_min  # total minutes
    tofd = start[1]  # time of day
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    if day != None:
        day = days.index(day.lower())
# add hours according to mins over 60
    if final_min >= 60:
        final_hour += final_min // 60
        final_min = final_min % 60
        if len(str(final_min)) < 2:
            final_min = '0' + str(final_min)


# Trying to get the time of day to switch accordingly
    # AM less than 24 hour duration
    if tofd == 'AM':
        if final_hour >= 12 and final_hour < 24:
            tofd = 'PM'    
            if final_hour > 12:
                final_hour = final_hour % 12
        elif final_hour >= 24:
            if day != None: day += final_hour // 24
            if (final_hour // 12) % 2 == 1:
                tofd = 'PM'
            if final_hour % 12 != 0:
                final_hour = final_hour % 12
            else: final_hour = 12 
    #PM less than 24 hour duration
    elif tofd == 'PM':
        if final_hour >= 12 and final_hour < 24:
            tofd = 'AM'
            if day != None: day += 1
            # **add(next day)**
            if final_hour > 12:
                final_hour = final_hour % 12
        elif final_hour >= 24:
            if day != None: day += final_hour // 24
            # **add(n days later)**
            if (final_hour // 12) % 2 == 1:
                if day != None: day += 1
                tofd = 'AM'
            if final_hour % 12 != 0:
                final_hour = (final_hour % 12)
            else: final_hour = 12
# return the formatted final time
    final_time = [str(final_hour), str(final_min)]
    try:
        day / 1 == day
        return ':'.join(final_time) + " " + tofd + ' ' + days[day][0].capitalize() + days[day][1:] 
    except:
        return ':'.join(final_time) + " " + tofd

# Call func    
print(add_time('6:30 PM', '205:12'))