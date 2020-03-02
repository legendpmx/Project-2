import json
import bottle
import appcode

appcode.writeDataToCSVFile()

@bottle.route("/")
def create_webpage():
  return bottle.static_file("index.html",root = ".")

@bottle.route("/frontEnd.js")
def showGraph():
  return bottle.static_file("frontEnd.js",root = ".")

@bottle.route("/pies")
def pieGraphData():
  newAr={}
  newAr = appcode.data2012()
  return json.dumps(newAr)

@bottle.route("/charts")
def pieGraphData():
  newAr={}
  newAr = appcode.yearsData()
  return json.dumps(newAr)

@bottle.post("/send")
def do_chat():
    content = bottle.request.body.read()
    #print(content)
    content = content.decode()
    #print(content)
    content_ = json.loads(content)
    if content_ == "2012":
      return json.dumps(appcode.data2012())
    if content_ == "2011":
      return json.dumps(appcode.data2011())
    if content_ == "2010":
      return json.dumps(appcode.data2010())
    if content_ == "2009":
      return json.dumps(appcode.data2009())

bottle.run(host = "0.0.0.0", port = 8080, debug = True)


