# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 23:16:08 2020

@author: avoka
"""

#Input route map data manually into the database and load them during navigation
import math
import sqlite3
from Programs import Adjacency_map_capstone
conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute("""CREATE TABLE path (
            Lattitude,
            Longitude,
            distance
            )""")
def insert_point(dist, lat, long):
    with conn:
        c.execute("INSERT INTO path VALUES (:lattitude, :longitude, :distance)", {'lattitude': lat, 'longitude': long, 'distance': dist})
def get_emps_by_name(dist):
    parsroad = []
    for i in dist:
        c.execute("SELECT Lattitude, Longitude FROM path WHERE distance=:distance", {'distance': i})
        for obj in c.fetchall():
            parsroad.append(obj)
    return parsroad
       

def remove_emp(dist):
    with conn:
        c.execute("DELETE from path WHERE first = :dist = dist",
                  {'first': dist})
        
        
#Test input points
insert_point(80, 523525.887478, 6467.475862) #coordinates changed for security reasons. Put your own coordinates




road = get_emps_by_name(Adjacency_map_capstone.pathID)

#calculates the angle between two lines that start from the same point. 
def getAngle(a, b, c):
    ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
    return ang
 
def takepoint():
    i = 0;
    nextpoint = road[0]
    lastpoint = road[len(road)-1]
    
    while  nextpoint != road[len(road)-1]:
        val =  getAngle(road[i],road[i-1],nextpoint)
        i = i+1
        if i >= len(road):
            print("sorry you are have missed the path, call for help")
            break
        if val < 0 :
            print("Turn right by  "+"{:.1f}".format(abs(val)))
        elif val > 0 :
           print("Turn left by  "+"{:.1f}".format(val)) 
        nextpoint = input("Enter nexpoint:")
        nextpoint = tuple(map(float,nextpoint.split(',')))
        if nextpoint == lastpoint:
            print("You have reached your destination!")
            break
       
takepoint()
conn.close()
