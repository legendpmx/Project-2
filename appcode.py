import csv
import json
import os.path
import urllib.request
import urllib.parse

def get_data():
  url = "https://data.cityofnewyork.us/api/views/5t4n-d72c/rows.json?accessType=DOWNLOAD"
  data = urllib.request.urlopen(url)
  newAr = data.read().decode()
  abcd = json.loads(newAr)
  return abcd["data"]


def writeDataToCSVFile():
  with open ("data.csv", "w") as f:
    writer =csv.writer(f)
    for line in get_data():
      writer.writerow(line)
    
def readDataFromCSVFile2012(filename):
  newAr = {}
  with open(filename, newline='', encoding="utf-8") as fileObject:
    reader = csv.reader(fileObject)
    for line in reader:
      if line[8]== "2012":
        newAr[line[9]]=line[10]
  return newAr 

def readDataFromCSVFile2011(filename):
  newAr = {}
  with open(filename, newline='', encoding="utf-8") as fileObject:
    reader = csv.reader(fileObject)
    for line in reader:
      if line[8]== "2011":
        newAr[line[9]]=line[10]
  return newAr 

def readDataFromCSVFile2010(filename):
  newAr = {}
  with open(filename, newline='', encoding="utf-8") as fileObject:
    reader = csv.reader(fileObject)
    for line in reader:
      if line[8]== "2010":
        newAr[line[9]]=line[10]
  return newAr 

def readDataFromCSVFile2009(filename):
  newAr = {}
  with open(filename, newline='', encoding="utf-8") as fileObject:
    reader = csv.reader(fileObject)
    for line in reader:
      if line[8]== "2009":
        newAr[line[9]]=line[10]
  return newAr 


def data2012():
  oldAr = readDataFromCSVFile2012("data.csv")
  newAr = {}
  newAr["Bronx"]=oldAr["Surface Area - Bronx "]
  newAr["Manhattan"]=oldAr["Surface Area - Manhattan "]
  newAr["Brooklyn"]=oldAr["Surface Area - Brooklyn "]
  newAr["Staten Island"]=oldAr["Surface Area - Staten Island "]
  newAr["Queens"]=oldAr["Surface Area - Queens "]
  newAr["TOTAL"] = oldAr["Total Unsheltered Individuals "]
  return newAr

def data2011():
  oldAr = readDataFromCSVFile2011("data.csv")
  newAr = {}
  newAr["Bronx"]=oldAr["Surface Area - Bronx "]
  newAr["Manhattan"]=oldAr["Surface Area - Manhattan "]
  newAr["Brooklyn"]=oldAr["Surface Area - Brooklyn "]
  newAr["Staten Island"]=oldAr["Surface Area - Staten Island "]
  newAr["Queens"]=oldAr["Surface Area - Queens "]
  newAr["TOTAL"] = oldAr["Total Unsheltered Individuals "]
  return newAr

def data2009():
  oldAr = readDataFromCSVFile2009("data.csv")
  newAr = {}
  newAr["Bronx"]=oldAr["Surface Area - Bronx "]
  newAr["Manhattan"]=oldAr["Surface Area - Manhattan "]
  newAr["Brooklyn"]=oldAr["Surface Area - Brooklyn "]
  newAr["Staten Island"]=oldAr["Surface Area - Staten Island "]
  newAr["Queens"]=oldAr["Surface Area - Queens "]
  newAr["TOTAL"] = oldAr["Total Unsheltered Individuals "]
  return newAr

def data2010():
  oldAr = readDataFromCSVFile2010("data.csv")
  newAr = {}
  newAr["Bronx"]=oldAr["Surface Area - Bronx "]
  newAr["Manhattan"]=oldAr["Surface Area - Manhattan "]
  newAr["Brooklyn"]=oldAr["Surface Area - Brooklyn "]
  newAr["Staten Island"]=oldAr["Surface Area - Staten Island "]
  newAr["Queens"]=oldAr["Surface Area - Queens "]
  newAr["TOTAL"] = oldAr["Total Unsheltered Individuals "]
  return newAr

def yearsData():
  newAr = {}
  newAr["2010"] = data2010()
  newAr["2009"] = data2009()
  newAr["2011"] = data2011()
  newAr["2012"] = data2012()
  return newAr


  