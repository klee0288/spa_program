"""
This is a Solar Zenith Angle Calculator
by Kevin Lee


Using built in module
"""

from pysolar.solar import *
import datetime
import math

Station_List = ["EU", "TEST"]
EUO = {"Latitude": 44.046775, "Longitude":-123.074214, "Time_zone": -8}

josh = []


def solpos(station, date, time_interval):
    output = []
    if station in Station_List:
        Latitude = station["Latitude"]
        Longitude = station["Longitude"]
        Time_zone = station["Timezone"]

    Y,M,D = date[0:4], date[5:7], date[8:10] #Parsing the string into different sections of year/month/date
    Y,M,D = int(Y), int(M), int(D)


    # print("The year is {} the minute is : {} and the date is : {}".format(Y,M,D))
    # Fraction of the day is minute of the day / 1440
    # seconds_in_day = 86400
    # second_interval = 86400 / int(time_interval)
    # minute_interval = 1440 / second_interval
    # hour_interval = 60 / minute_interval
    # variable = 0

    f  = open("kevin.txt", "w")
    f.write("DOY,SZA,AZM\n")
    if int(time_interval) < 60:
        # x = seconds_in_day % (int(time_interval))
        for hour in range(24):
            for min in range(60):
                for sec in range(0, 60, int(time_interval)):
                    dobj = datetime.datetime(int(Y), int(M), int(D), int(hour), int(min), int(sec),
                                             tzinfo=datetime.timezone.utc) - datetime.timedelta(hours=-8)
                    # print(dobj)
                    sza = float(90) - get_altitude(44.046775, - 123.074214, dobj, 431)
                    azm = get_azimuth(44.046775,- 123.074214, dobj)
                    doy = day_of_year(Y,M,D,hour, min,sec)
                    josh.append(josh)
                    # print(doy)
                    f.write("{},{},{}\n".format(doy, sza, azm))
    elif (int(time_interval) < 3600):
        for hour in range(24):
            minute = int(time_interval)/60
            # print(f"minute is %d", minute)
            for min in range (0, 60, int(minute)):
                print("Time interval is {}:{}:00".format(hour, min))
                dobj = datetime.datetime(int(Y), int(M), int(D), int(hour), int(minute),
                                         tzinfo=datetime.timezone.utc) - datetime.timedelta(hours=-8)
                sza = float(90) - get_altitude(44.046775, - 123.074214, dobj)
                output.append(sza)
    elif (int(time_interval) < 86400):
        hour = int(time_interval)/3600
        minute = 0
        print(f"hour is &d", hour)
        for hour in range(0, 24, int(hour)):
            print("Time interval is {}:00:00".format(hour))
            dobj = datetime.datetime(int(Y), int(M), int(D), hour, minute,
                                     tzinfo=datetime.timezone.utc) - datetime.timedelta(hours=-8)
            sza = float(90) - get_altitude(44.046775, - 123.074214, dobj)
            output.append(sza)

def day_of_year(YY,MM,day,hour, min,sec):
    dt = datetime.timedelta(days=day, hours=hour, minutes=min, seconds=sec)
    secs_per_day = 24 * 60 * 60  # hours * mins * secs
    days_in_the_year = (datetime.date(YY, MM, day) - datetime.date(YY, 1, 1)).days
    return days_in_the_year + dt.total_seconds() / secs_per_day
    # return days_in_the_year

    # if hour_interval <= 1:
    #     if minute_interval <= 1:
    #         variable = second_interval
    #     variable = minute_interval
    # varaible = second_interval
    #     minute = 0
    #     second = 0
    #     for i in range(0, 24, int(hour)):
    #         print("The hour it loops through: {}:{}:{}".format(i, minute, second))


        # second = i % 3600
    #     if variable > 3600:
    #
    #         hour = math.floor(i / 3600)
    #     if minutes_interval > 24:
    #         hour = minute
    #     if i >= 24:
    #         hour = i - (60*hour)-
    #         minute = i/60
    #     else:
    #         minute =0
    #         second =0
    #     print("The hour it loops through: {}:{}:{}".format(hour, minute, second))
    # #
    # print("timezone = UTC+4,",sza)
    # print(output)



def driver():
    # station = input("Enter station ex(EUO): ")
    # Date = input("Enter date YYYY/MM/DD: ")
    # Time_Interval = input("Time intervals in seconds ex. 2 hour = 7200: ")
    # solpos(station, Date, Time_Interval)
    solpos(EUO, "2016/12/31", "1")






if __name__ == "__driver__":
    driver()
    print(josh)
driver()



