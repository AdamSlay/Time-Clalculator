def add_time(start_time, duration, day = None):
# Starting/setup variables
    start = start_time.split(' ')
    stime = start[0].split(':')
    dtime = duration.split(':')
    if duration == '0:00':
        return start_time

# Variables in use
    start_hour = int(stime[0])
    start_min = int(stime[1])    
    dur_hour = int(dtime[0]) # duration hours
    dur_min = int(dtime[1])  # duration minutes
    final_hour = start_hour + dur_hour # total hours 
    final_min =  start_min + dur_min  # total minutes
    tofd = start[1]  # time of day
    day_diff = 0
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
    # AM start
    if tofd == 'AM':
        if final_hour >= 12 and final_hour < 24:
            tofd = 'PM'    
            if final_hour > 12:
                final_hour = final_hour % 12
        elif final_hour >= 24:
            day_diff = final_hour // 24
            if day != None:
                day += final_hour // 24
            if (final_hour // 12) % 2 == 1:
                tofd = 'PM'
            if final_hour % 12 != 0:
                final_hour = final_hour % 12
            else: final_hour = 12 


    #PM start
    elif tofd == 'PM':
        if final_hour >= 12 and final_hour < 24:
            tofd = 'AM'
            day_diff += 1
            if day != None: 
                day += 1
            if final_hour > 12:
                final_hour = final_hour % 12
        
        elif final_hour >= 24:
            day_diff += final_hour // 24
            if day != None: 
                day += final_hour // 24
            if (final_hour // 12) % 2 == 1:
                day_diff += 1
                if day != None: 
                    day += 1
                tofd = 'AM'
       
            if final_hour % 12 != 0:
                final_hour = (final_hour % 12)
            else: final_hour = 12
      

# Formatting the final time 
    final_time = ':'.join([str(final_hour), str(final_min)])

      
      
# Formatting the total diff in days  
    if day_diff == 1:
        final_diff = '(next day)'
    elif day_diff > 1:
        final_diff = f'({day_diff} days later)'
    if day > 6:
        day = day % 7


# return the formatted final time
    try:
        final_day = days[day][0].capitalize() + days[day][1:]
        if day_diff > 0: 
            return f'{final_time} {tofd}, {final_day} {final_diff}' 
        else: 
            return f'{final_time} {tofd}, {final_day}'
    except:
        if day_diff > 0:
            return f'{final_time} {tofd} {final_diff}'
        else:
            return f'{final_time} {tofd}'
# Call func    
#print(add_time('6:30 PM', '205:12'))