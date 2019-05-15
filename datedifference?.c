// C program two find number of days between two given dates + time 
#include<stdio.h>
#include<time.h>
#include<stdlib.h>
#include<string.h>
#include <stdio.h>
#include "spa.h"

// A date has day 'd', month 'm' and year 'y' 
struct Date 
{ 
    int y,m,d; 
}; 
struct TIME
{
  int seconds;
  int minutes;
  int hours;
};
  
// To store number of days in all months from January to Dec. 
const int monthDays[12] = {31, 28, 31, 30, 31, 30, 
                           31, 31, 30, 31, 30, 31}; 
  
// This function counts number of leap years before the 
// given date 
int countLeapYears(struct Date d) 
{ 
    int years = d.y; 
  
    // Check if the current year needs to be considered 
    // for the count of leap years or not 
    if (d.m <= 2) 
        years--; 
  
    // An year is a leap year if it is a multiple of 4, 
    // multiple of 400 and not a multiple of 100. 
    return years / 4 - years / 100 + years / 400; 
} 
  
// This function returns number of days between two given 
// dates 
int getDifference(struct Date dt1, struct Date dt2) 
{ 
    // COUNT TOTAL NUMBER OF DAYS BEFORE FIRST DATE 'dt1' 
  
    // initialize count using years and day 
    long int n1 = dt1.y*365 + dt1.d; 
  
    // Add days for months in given date 
    for (int i=0; i<dt1.m - 1; i++) 
        n1 += monthDays[i]; 
  
    // Since every leap year is of 366 days, 
    // Add a day for every leap year 
    n1 += countLeapYears(dt1); 
  
    // SIMILARLY, COUNT TOTAL NUMBER OF DAYS BEFORE 'dt2' 
  
    long int n2 = dt2.y*365 + dt2.d; 
    for (int i=0; i<dt2.m - 1; i++) 
        n2 += monthDays[i]; 
    n2 += countLeapYears(dt2); 
  
    // return difference between two counts 
    return (n2 - n1); 
} 

 // Find the the time between the two intervals.
void differenceBetweenTimePeriod(struct TIME start, struct TIME stop, struct TIME *diff)
{
    if(stop.seconds > start.seconds){
        --start.minutes;
        start.seconds += 60;
    }

    diff->seconds = start.seconds - stop.seconds;
    if(stop.minutes > start.minutes){
        --start.hours;
        start.minutes += 60;
    }

    diff->minutes = start.minutes - stop.minutes;
    diff->hours = start.hours - stop.hours;
}
  
// Driver program 
int main(int argc, char *argv[]) 
{ 
    struct TIME startTime, stopTime, diff;
    struct Date dt1; 
    struct Date dt2;
    char *yesno;
    char *y = "yes";
    FILE *f = fopen("output.txt", "w"); 
    printf("Enter Start Date YYYY/MM/DD: ");
    scanf("%d/%d/%d", &dt1.y, &dt1.m, &dt1.d);
    printf("Enter Start Time HH:MM:SS: ");
    scanf("%d:%d:%d", &startTime.hours, &startTime.minutes, &startTime.seconds);
    printf("Enter End Date YYYY/MM/DD: ");
    scanf("%d/%d/%d", &dt2.y, &dt2.m, &dt2.d);
    printf("Enter Stop Time HH:MM:SS: ");
    scanf("%d:%d:%d", &stopTime.hours, &stopTime.minutes, &stopTime.seconds);
    printf("\n\nStart: %d/%d/%d ", dt1.y, dt1.m, dt1.d);
    printf("at %d:%d:%d \n", startTime.hours, startTime.minutes, startTime.seconds);
    printf("End: %d/%d/%d ", dt2.y, dt2.m, dt2.d);
    printf("at %d:%d:%d \n", stopTime.hours, stopTime.minutes, stopTime.seconds);
    printf("Is this correct? (yes/no) ");
    scanf("%s", yesno);
    if (strcmp(yesno, y) != 0){
        exit(0);
    }


    // Calculate the difference between the start and stop time period.
    differenceBetweenTimePeriod(startTime, stopTime, &diff);

    printf("\nTIME DIFFERENCE: %d:%d:%d - ", startTime.hours, startTime.minutes, startTime.seconds);
    printf("%d:%d:%d ", stopTime.hours, stopTime.minutes, stopTime.seconds);
    printf("= %d:%d:%d\n", diff.hours, diff.minutes, diff.seconds);
    int difference = getDifference(dt1, dt2);
    printf("Difference between two dates is %d\n", difference); 



    // SPA CALCULATION START ========================
    spa_data spa;  //declare the SPA structure
    int result;
    float min, sec;
    if (dt1.y != dt2.y){
        print("Elapsed year is different! Kevin you need to implement this");
        exit(0);
    }
    for (int day = 0; day < 30; day++){
        spa.year = dt1.y;
        spa.month         = dt1.m;
        spa.day           = day;
        spa.hour          = 14;
        spa.minute        = 00;
        spa.second        = 00;
        spa.timezone      = -8.0;
        spa.delta_ut1     = 0;
        spa.delta_t       = 67;
        spa.longitude     = -120;
        spa.latitude      = 39.742476;
        spa.elevation     = 1000;
        spa.pressure      = 820;
        spa.temperature   = 11;
        spa.slope         = 30;
        spa.azm_rotation  = -10;
        spa.atmos_refract = 0.5667;
        spa.function      = SPA_ALL;

        result = spa_calculate(&spa);
         if (result == 0)  //check for SPA errors
    {
        //SAVING TO 
        
        fprintf(f, "Julian Day:    %.6f\n",spa.jd);
        fprintf(f, "L:             %.6e degrees\n",spa.l);
        fprintf(f, "B:             %.6e degrees\n",spa.b);
        fprintf(f, "R:             %.6f AU\n",spa.r);
        fprintf(f, "H:             %.6f degrees\n",spa.h);
        fprintf(f, "Delta Psi:     %.6e degrees\n",spa.del_psi);
        fprintf(f, "Delta Epsilon: %.6e degrees\n",spa.del_epsilon);
        fprintf(f, "Epsilon:       %.6f degrees\n",spa.epsilon);
        fprintf(f, "Zenith:        %.6f degrees\n",spa.zenith);
        fprintf(f, "Azimuth:       %.6f degrees\n",spa.azimuth);
        fprintf(f, "Incidence:     %.6f degrees\n",spa.incidence);

        min = 60.0*(spa.sunrise - (int)(spa.sunrise));
        sec = 60.0*(min - (int)min);
        printf("Sunrise:       %02d:%02d:%02d Local Time\n", (int)(spa.sunrise), (int)min, (int)sec);

        min = 60.0*(spa.sunset - (int)(spa.sunset));
        sec = 60.0*(min - (int)min);
        printf("Sunset:        %02d:%02d:%02d Local Time\n", (int)(spa.sunset), (int)min, (int)sec);

    } else printf("SPA Error Code: %d\n", result);
    }
  
    return 0; 
} 
