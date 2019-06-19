"""
This is the run function for the spa.c program.

"""
from sys import argv
import subprocess
import sys, string, os
from datetime import datetime  
from datetime import timedelta

import numpy as np

Station_List = ["EUO", "TEST"]
EUO = {"Latitude": 44.046775, "Longitude":-123.074214, "Time_zone": -8}

def run_calculator(y, mo, d, h, mi, s, t, lo, la):
	path = os.path.dirname(os.path.realpath(__file__))
	year = str(y)
	month = str(mo)
	day = str(d)
	hour = str(h)
	minute = str(mi)
	second = str(s)
	timezone = str(t)
	longtitude= str(lo)
	latitude = str(la)
    # parameters = "\\a.exe 2018 10 17 12 30 30 -7.0 -105.1786 39.742476"
	# program = path + parameters
	# print(program)
	output = (subprocess.run(["SZA_calculator.exe", year, month, day, hour,
		minute, second, timezone, longtitude, latitude]))
	return output
	



def main(argv):

	# run calculator((year, month, day, hour, minute, second,
	# timezone, longtitude, latitude)

	station = argv[1]
	#Check if station is valid
	if station == 'EUO':
		lat = EUO["Latitude"]
		lon = EUO["Longitude"]
		time_z = EUO["Time_zone"]


	#START YEAR/MONTH DATE PARSE=====================================
	# start_date = argv[2]
	# start_date = start_date.split("/")
	# start_year = start_date[0]
	# start_month = start_date[1]
	# start_day = start_date[2]
	# # print("START DATE {}, YEAR {}, MONTH {}, DAY {}".format(start_date,year,month,day))
	# #EMD YEAR/MONTH DATE PARSE=======================================
	# end_date = argv[3]
	# end_date = end_date.split("/")
	# end_year = end_date[0]
	# end_month = end_date[1]
	# end_day = end_date[2]

	# print("END DATE {}, YEAR {}, MONTH {}, DAY {}".format(end_date,end_year,end_month,end_day))



	#INTERVAL PARSER (in seconds) =============================================

	
	# output = run_calculator(year, month, day, 12, 30, 30, time_z, lon, lat)
	output = run_calculator("2018", "08", "13", "12", "30", "30", time_z, lon, lat)
	# tiemstart = timestart + interval


	#TIMESERIES==================================================================
	# dates = pd.to_datetime([datetime(2015, 7, 3), "4th of July, 2015", '2015-Jul-6', '07-07-2015', '20150708'])
	
	# print("Dates are: {}".format(dates))
	return

	# print(output[1])




if __name__ == "__main__":
	main(argv)


