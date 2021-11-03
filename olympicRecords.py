#CSci 127 Teaching Staff
#FALL 2021
#A template for a program that returns olympic world records
#Modified by:  Sameera Shamsudeen

def worldRecord(gender, event):
     """
     Write a function worldRecord(), that takes two parameters: gender (string) and the event type (int). 
     The function should return a float for the Olympic world record for the event. 
     
     Men's Standard, event type 100 meters: record is 9.63 seconds.
     Men's Standard, event type 200 meters: record is 19.30 seconds.
     Men's Standard, event type 400 meters: record is 43.03 seconds.
     Women's Standard, event type 100 meters: record is 10.62 seconds.
     Women's Standard, event type 200 meters: record is 21.34 seconds.
     Women's Standard, event type 400 meters: record is 48.25 seconds.
     Return -1 for any other value
     """
     
     time = 0.0
     
import pandas as pd 
def worldRecord(gender, event):     
        z = str(input(men))
        t = int(input(‘100’))
        time = float(input(9.63))
        return(time,'seconds')

def worldrecord(gender,event):
        z = str(input(men))
        t = int(input(‘200’))
        time = float(input(19.30))
        return(time,'seconds')

def worldrecord(gender,event):
        z = str(input(men))
        t = int(input(‘400’))
        time = float(input(43.03))
        return(time,'seconds')

def worldrecord(gender,event):
        z = str(input(women))
        t = int(input(‘100’))
        time = float(input(10.62))
        return(time,'seconds')

def worldrecord(gender,event):
        z = str(input(women))
        t = int(input(‘200’))
        time = float(input(21.34))
        return(time,'seconds')

def worldrecord(gender,event):
        z = str(input(women))
        t = int(input(‘400’))
        time = float(input(48.25))
        return(time,'seconds')

else:
        return -1



def main():
     z = input('Enter the gender: ').lower()
     t = int(input('Enter the event distance: '))
     record = worldRecord(z,t)
     print("The record for "+z+" 's "+ str(t) + " meters is", record)

#Allow script to be run directly:
if __name__ == "__main__":
     main()
