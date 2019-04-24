"""
This is the test driver to make C an executable code

Kevin Lee

"""
import subprocess



#List of Stations
EUO = {"Latitude": 44.046775, "Longitude":-123.074214, "Time_zone": -8}

# Date has to have year in it YYYY/MM/DD - YYYY/MM/DD, 
def spa(station, start_date, end_date, time_interval):
	
	subprocess.run(["gcc", "spa_tester.c", "spa.c"])
	print(subprocess.run(["./a.out"]))




def driver():
	spa(EUO, 20, 10)


if __name__ == "__main__":
	driver()
