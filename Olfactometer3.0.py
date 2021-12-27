# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 14:32:42 2016

@author: nathhall
"""
############################################################################
##Load Libraries 
import Panel_Auto3 as UI
from PyQt5 import QtCore, QtGui, QtWidgets
import fileIO
import serial
import time
import sys
from datetime import datetime
import os
import random
import serial.tools.list_ports
import math
myos=os.name
if myos=='posix':
    import pyglet
else: 
    import winsound

############################################################################



odorFile=fileIO.fileIO("Odors.csv")
O1=odorFile.lookup(returnval=1,key1="Valve 1")
O2=odorFile.lookup(returnval=1,key1="Valve 2")
O3=odorFile.lookup(returnval=1,key1="Valve 3")
O4=odorFile.lookup(returnval=1,key1="Valve 4")
O5=odorFile.lookup(returnval=1,key1="Valve 5")
O6=odorFile.lookup(returnval=1,key1="Valve 6")
odorlist=[O1, O2, O3,O4,O5, O6]

def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = myapp()
    ui.setupUi(MainWindow)
    ui.setupApp()
    MainWindow.show()  
    sys.exit(app.exec_())
    

def create_datasheet(subj_ID, folder, headerType=0):
    #C:\Users\DogOdorLab\Documents/AutoPanelData
    now=datetime.now()
    sessiontime=now.strftime("%m_%d_%y_%H_%M_%S")#Create date to save data sheet
    wd=os.getcwd()
    #########################################################################
    #wd="C:/Users/DogOdorLab/Documents/AutoPanelData"
    filename="{}_{}.csv".format(subj_ID, sessiontime)
    datasheet=fileIO.fileIO(("{}/data/{}/{}_{}.csv").format(wd, folder, subj_ID, sessiontime))
    
    header=['subjID', 'expID', 'numbTrials', "alertTime", 
             "trialTime", "session", "daySession", "trainingLevel",
             "handlerBlind", "waitforCorrect", "runCorrections",
             "odorPrevelance", "reinforceBlanks", "reinforceTargets",
             "useTones", "generalizationTest", "autoscoreAlerts",
             "notes", "correctPort", "response",
             "latency", "poke1Number", "poke2Number", "poke3Number",
             "cumulative1", "cumulative2", "cumulative3", "firstResponse",
             "timestamp","port1Odor", "port2Odor", "port3Odor", 
             "temp", "humidity", "pressure", "pokeOrder", "pokeTimes", 
             "pokeITI","reinforced", "probe", "TrialNumber"]       
   
    if headerType=="Threshold":
        header =['subjID', 'expID', 'numbTrials', "alertTime", 
             "trialTime", "session", "daySession", "trainingLevel",
             "handlerBlind", "waitforCorrect", "runCorrections",
             "odorPrevelance", "reinforceBlanks", "reinforceTargets",
             "useTones", "generalizationTest", "autoscoreAlerts",
             "notes", "correctPort", "response",
             "latency", "poke1Number", "poke2Number", "poke3Number",
             "cumulative1", "cumulative2", "cumulative3", "firstResponse",
             "timestamp","port1Odor", "port2Odor", "port3Odor", 
             "temp", "humidity", "pressure", "pokeOrder", "pokeTimes", 
             "pokeITI","reinforced", "probe", "TrialNumber", "concIndex", 
             "concentration", "reversal"]
        
    datasheet.create(header)
    return(datasheet, filename)

    
class myapp(UI.Ui_MainWindow):

    def __init__(self):
       UI.Ui_MainWindow.__init__(self)
        
    def setupApp(self):  
       
        #Connect buttons to functions 
        self.Submit.clicked.connect(self.runTrials)
        self.AlertTime.setValue(4.00)
        self.NumberofTrials.setCurrentIndex(4)
        self.TargDist_2.addItem("Probe")
        self.OdorPrev.setCurrentIndex(2)
        self.NumberofTrials.setCurrentIndex(2)
        self.TrainingLevel.currentIndexChanged.connect(self.updateSettings)
        self.ResetOdors.clicked.connect(self.updateOdors)
        self.TrainingLevel.setCurrentIndex(0)
        
        #Add odor list to 

        for i in odorlist:
            self.Odor1.addItem(i)
            self.Odor2.addItem(i)
            self.Odor3.addItem(i)
            self.Odor4.addItem(i)
            self.Odor5.addItem(i)
            self.Odor6.addItem(i)
            self.Odor1.setCurrentIndex(0)
            self.Odor2.setCurrentIndex(1)
            self.Odor3.setCurrentIndex(2)
            self.Odor4.setCurrentIndex(3)
            self.Odor5.setCurrentIndex(4)
            self.Odor6.setCurrentIndex(5)
    
    def updateSettings(self):
            
        if self.TrainingLevel.currentText()=="GoNoGo":
            print("updating stuff")
            self.OdorPrev.setCurrentIndex(5)
            
        if self.TrainingLevel.currentText=="Last Saved":
            mysettings=fileIO.fileIO("Settings.csv")
            self.NumberTrials.setCurrentIndex(mysettings.lookup(1, "Number of Trials"))
            self.AlertTime.setValue(float(mysettings.lookup(1, "Alert Time")))
            self.TrialTime.setValue(float(mysettings.lookup(1, "Trial Time")))
            self.Session.setValue(float(mysettings.lookup(1, "Session")))
            self.DaySession.setValue(int(mysettings.lookup(1, "Day Session")))
            self.HandlerBlind.setCurrentIndex(int(mysettings.lookup(1, "Handler Blind")))
            self.WaitforCorrect.setCurrentIndex(int(mysettings.lookup(1, "Wait for Correct")))
            self.RunCorrections.setCurrentIndex(int(mysettings.lookup(1, "Run Corrections")))
            self.OdorPrev.setCurrentIndex(int(mysettings.lookup(1, "Target Odor Frequency")))
            self.ReinforceBlanks.setCurrentIndex(int(mysettings.lookup(1, "Reinforce Blanks")))
            self.ReinforceTargets.setCurrentIndex(int(mysettings.lookup(1, "Reinforce Targets")))
            self.Context.setCurrentIndex(int(mysettings.lookup(1, "Use Tones")))
            self.GenProbes.setCurrentIndex(int(mysettings.lookup(1, "N Generalization Trials")))
            self.comboBox.setCurrentIndex(int(mysettings.lookup(1, "AutoScore")))
            self.Notes.setText(mysettings.lookup(1, "Notes"))
            
            self.TargDist_1.setCurrentIndex(int(mysettings.lookup(1, "Valve1")))
            self.TargDist_2.setCurrentIndex(int(mysettings.lookup(1, "Valve2")))
            self.TargDist_3.setCurrentIndex(int(mysettings.lookup(1, "Valve3")))
            self.TargDist_4.setCurrentIndex(int(mysettings.lookup(1, "Valve4")))
            self.TargDist_5.setCurrentIndex(int(mysettings.lookup(1, "Valve5")))
            self.TargDist_6.setCurrentIndex(int(mysettings.lookup(1, "Valve6")))
            
            
            
    def updateOdors(self):
        newodors=[str(self.NewOdor_1.text()).capitalize().strip(),
                  str(self.NewOdor_2.text()).capitalize().strip(),
                  str(self.NewOdor_3.text()).capitalize().strip(),
                  str(self.NewOdor_4.text()).capitalize().strip(),
                  str(self.NewOdor_5.text()).capitalize().strip(),
                  str(self.NewOdor_6.text()).capitalize().strip()
                  ]
        
        odorFile=fileIO.fileIO("Odors.csv")
        
        row1=["Valve 1", newodors[0]]
        row2=["Valve 2", newodors[1]]
        row3=["Valve 3", newodors[2]]
        row4=["Valve 4", newodors[3]]
        row5=["Valve 5", newodors[4]]
        row6=["Valve 6", newodors[5]]
        odorFile.save_all([row1, row2, row3, row4, row5, row6])
        
        self.Odor1.clear()
        self.Odor2.clear()
        self.Odor3.clear()
        self.Odor4.clear()
        self.Odor5.clear()
        self.Odor6.clear()
        
        for i in newodors:
          
            self.Odor1.addItem(i)
            self.Odor2.addItem(i)
            self.Odor3.addItem(i)
            self.Odor4.addItem(i)
            self.Odor5.addItem(i)
            self.Odor6.addItem(i)
            self.Odor1.setCurrentIndex(0)
            self.Odor2.setCurrentIndex(1)
            self.Odor3.setCurrentIndex(2)
            self.Odor4.setCurrentIndex(3)
            self.Odor5.setCurrentIndex(4)
            self.Odor6.setCurrentIndex(5)
            
        self.tabWidget.setCurrentIndex(0)
        
        
        
    def runTrials(self):
        #Get values and deactivate user input
        self.Submit.setEnabled(False)
        self.Info={}
        self.tabWidget.setCurrentIndex(1)
        #Collect User input
        self.Info['DogName']=str(self.DogName.text()).capitalize().strip()
        self.Info['ExpName']=str(self.ExperimenterName.text()).capitalize().strip()
        self.Info['NumberTrials']=int(self.NumberofTrials.currentText())
        self.Info['SniffTime']=int(float(self.AlertTime.value())*1000) #Convert to millisecond 
        self.Info['AddSniffTime']=int(float(self.AlertTime_2.value())*1000) #Convert to millisecond 
        self.Info['TrialTime']=int(self.TrialTime.value())
        self.Info['SessionNumber']=self.Session.value()
        self.Info['DaySession']=self.DaySession.value()
        self.Info['TrainingLevel']= str(self.TrainingLevel.currentText())
        self.Info['HandlerBlind']=str(self.HandlerBlind.currentText())
        
        self.Info['WaitforCorrect']=str(self.WaitforCorrect.currentText())
        self.Info['RunCorrections']=str(self.RunCorrections.currentText())
        self.Info['OdorPrev']=float(self.OdorPrev.currentText())
        self.Info['ReinforceBlanks']=float(self.ReinforceBlanks.currentText())
        self.Info["ReinforceTargets"]=float(self.ReinforceTargets.currentText())
        self.Info['Tones']=str(self.Context.currentText())
        self.Info['GeneralizationProbes']=int(self.GenProbes.currentText())
        self.Info['AutoScore']=str(self.comboBox.currentText())
        self.Info['Notes']=str(self.Notes.text()).capitalize().strip()
        
        
        
        self.Info["Odor1"]=self.Odor1.currentText()
        self.Info["Odor2"]=self.Odor2.currentText()
        self.Info["Odor3"]=self.Odor3.currentText()
        self.Info["Odor4"]=self.Odor4.currentText()
        self.Info["Odor5"]=self.Odor5.currentText()
        self.Info["Odor6"]=self.Odor6.currentText()
        
        self.Info["Odor1Type"]=self.TargDist_1.currentText()
        self.Info["Odor2Type"]=self.TargDist_2.currentText()
        self.Info["Odor3Type"]=self.TargDist_3.currentText()
        self.Info["Odor4Type"]=self.TargDist_4.currentText()
        self.Info["Odor5Type"]=self.TargDist_5.currentText()
        self.Info["Odor6Type"]=self.TargDist_6.currentText()
        
        
        mytargets=[]
        mydistractors=[]
        myprobes=[]
        mykeys=["Odor1Type", "Odor2Type", "Odor3Type", "Odor4Type", "Odor5Type", "Odor6Type"]
        mykeys2=["Odor1", "Odor2", "Odor3", "Odor4", "Odor5", "Odor6"]
        
        for i in range(0, len(mykeys)):
            if self.Info[mykeys[i]]=="Target":
                mytargets.append(self.Info[mykeys2[i]]) 
            elif self.Info[mykeys[i]]=="Probe":
                myprobes.append(self.Info[mykeys2[i]])  
            elif self.Info[mykeys[i]]=="Distractor":
                mydistractors.append(self.Info[mykeys2[i]])
            else:
                pass
              
        self.Info["Targets"]=mytargets
        self.Info["Distractors"]=mydistractors
        self.Info['Probes']=myprobes
        print(myprobes)
        
        
        myweights=[]
        if self.Info["Odor1Type"]=="Target":
            myweights.append(int(self.OdorWeights_1.currentText()))
        if self.Info["Odor2Type"]=="Target":
            myweights.append(int(self.OdorWeights_2.currentText()))
        if self.Info["Odor3Type"]=="Target":
            myweights.append(int(self.OdorWeights_3.currentText()))
        
        self.Info["OdorWeights"]=myweights
        
        
        
        
        self.devices=self.connectArduinos()
        arduinosConnected="no"
        
        #######################################################################
        #Have this update the list of Olfactometers to indicate which are connected and which are not
        if self.Info['TrainingLevel']=="3AFC":
            if "Olfactometer1" and "Olfactometer2" and "Olfactometer3" in self.devices: 
                arduinosConnected="yes" 
        elif self.Info['TrainingLevel']=="GoNoGo":
            if "Olfactometer1"  in self.devices: 
                arduinosConnected="yes" 
                
        if arduinosConnected=="no":
            self.exception_screen("Something is not connected")
       ###########################################################################
       
       
       
        if arduinosConnected=="yes":
           
            #Start Testing Thread
            if self.Info['TrainingLevel']=="3AFC":
                self.Info['datasheet'], self.Info['filename'] =create_datasheet(self.Info['DogName'], self.Info['TrainingLevel']) 
                self.Trials= AFCThread(self.devices, self.Info)

                               
            if self.Info['TrainingLevel']=="GoNoGo":
                if "Olfactometer2" in self.devices:
                    self.devices.pop("Olfactometer2")
                if "Olfactometer3" in self.devices:
                    self.devices.pop("Olfactometer3")    
                self.Info['datasheet'], self.Info['filename'] =create_datasheet(self.Info['DogName'], self.Info['TrainingLevel']) 
                self.Trials=GoNoGoThread(self.devices, self.Info)
                
            if self.Info['TrainingLevel']=="Threshold":
                self.Info['datasheet'], self.Info['filename'] =create_datasheet(self.Info['DogName'], self.Info['TrainingLevel'], headerType="Threshold") 
                self.Trials=Threshold(self.devices, self.Info)
                
            
            #Set Connections to update User info
            self.Trials.statusUpdate.connect(self.infoLabel.setText)
            self.Trials.trialNum.connect(self.trialNumber.display)
            self.Trials.msg.connect(self.exception_screen)
            self.Trials.start()
        else: 
            self.exception_screen("Something wrong")
        
        
    def position1(self):
        self.Trials.R1=5000
        
    def position2(self):
        self.Trials.R2=5000
        
    def position3(self):
        self.Trials.R3=5000
        
    def position4(self):
        self.Trials.R4=5000
           
    def exception_screen(self, msg):
        choice=QtWidgets.QMessageBox.question(self.centralwidget, 'Alert', msg,
                                   QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        return choice
        pass
        
    
    def connectArduinos(self):
       
        #Find Arduino ports and connect them 
        arduino_ports = []
        ports= serial.tools.list_ports.comports()
        for p in ports: 
            if "Arduino" in p.description or "USB Serial" in p.description or "Nano" in p.description:
                arduino_ports.append(p.device)
                
        print(arduino_ports)
        devices={}
        arduinos=[]
        print (arduino_ports)
        for port in arduino_ports:
            arduinos.append(Arduino(port))
            
        #Create a named dictionary by port name
        print(len(arduinos))
        for a in arduinos:
            print("Getting Arduino")
            print(a)
            time.sleep(2)
            name=a.whatisyourname()
            print(name)
            devices[name]=a
            
        return(devices)
    
    
    
    

class AFCThread(QtCore.QThread):
    statusUpdate=QtCore.pyqtSignal(str)
    trialNum=QtCore.pyqtSignal(int)
    msg=QtCore.pyqtSignal(str)
   
    
    def __init__(self, Devices, Info):     
        QtCore.QThread.__init__(self)
        self.stopped = QtCore.QEvent(QtCore.QEvent.User)
        self.stopped.setAccepted(False)
        self.devices=Devices
        self.Info=Info
        self.odorOff()
      
        
    def loadAudio(self):
        wd=os.getcwd()
        
        if myos=='posix':
            self.sound=pyglet.media.load('{}/Tones/food.wav'.format(wd), streaming=False)
            self.tone=pyglet.media.load('{}/Tones/432_short.wav'.format(wd), streaming=False)
            self.fail=pyglet.media.load('{}/Tones/fail_buzzer.wav'.format(wd), streaming=False)
            self.end=pyglet.media.load('{}/Tones/beepEnd.wav'.format(wd), streaming=False)
        else:
            
            self.sound ='{}/Tones/food.wav'.format(wd)
            self.tone ='{}/Tones/432_short.wav'.format(wd)
            self.fail ='{}/Tones/fail_buzzer.wav'.format(wd)
            self.end ='{}/Tones/beepEnd.wav'.format(wd)
        
        
        
    def playAudio(self, audio):
        
        if self.Info["Tones"]=="Yes":
            if myos=="posix":
                audio.play()
            else:
                winsound.PlaySound(audio, winsound.SND_FILENAME)
        
    def initializeRun(self):
        #Get Temp# Get Humidity # Get Pressure
        self.Temp=self.getTemperature()
        self.Humidity=self.getHumidity()
        self.Pressure=self.getPressure()
        
        #Load Audios
        self.loadAudio()
        
        #Create Randomized Trials 
        self.odors, self.valves, self.odorNames = self.createOdorDictionary()
        self.trialOrder, self.outcome, self.probes=self.createTrialOrder()
      
        
        
    def run(self):   
        self.initializeRun()
       
        trial=0
        for i in self.trialOrder:
            #Update the Alert Time
            self.changeSniffTime()
            port=i
            self.updateMessage(port, trial+1)
            self.odorOn(port, self.probes[trial])
            
            #Start the Trial
            self.startTime= time.time()
            self.playAudio(self.tone)
            
            self.Trial=self.lookForResponse(port=port, 
                                            waitforcorrect=self.Info["WaitforCorrect"],
                                            timeout= self.Info["TrialTime"], 
                                            blankSearch="yes")
             
            
            self.giveFeedback(port, trial)
            
            self.odorOff() #Clear the ports
            self.runExhaust()
            self.statusUpdate.emit("Odor Off")
            
            self.Trial["reinforce"]=self.outcome[trial]
            self.Trial["probe"]=self.probes[trial]
            self.Trial['TrialNumber']=trial+1
            self.recordData()
            
            #ITI
            time.sleep(20)
            trial=trial+1
            self.stopExhaust()
            
        self.statusUpdate.emit("Finished")

        
    def changeSniffTime(self):
        addRandom=random.uniform(0, self.Info['AddSniffTime'])
        self.Info['TrialSniff']=self.Info['SniffTime']+addRandom
        for key in self.devices:
            self.devices[key].updateSniffTime(self.Info['TrialSniff'])
        
        
    def updateMessage(self, port, trial):
        self.trialNum.emit(trial)
        message="Blind"
        if self.Info["HandlerBlind"]=="No":
            message=port
        self.statusUpdate.emit(message)
            
        
        
    def giveFeedback(self, port, trial):  
        if self.outcome[trial]==1:
            if port==self.Trial['response']:
                self.playAudio(self.sound)
                time.sleep(1)
                self.playAudio(self.end)
                
            
            elif port=="blank" :
                if self.Trial['response']=="all clear":
                    self.playAudio(self.sound)  
                    time.sleep(1)
                    self.playAudio(self.end)
                    
                if self.Trial['response']!= "all clear":
                    self.playAudio(self.fail)
                    time.sleep(0.5)
                    self.playAudio(self.end)
        
            else: 
                self.playAudio(self.fail)
                self.playAudio(self.end)
       
        elif self.outcome[trial]==0:
            self.playAudio(self.end)
         
            
    def createTrialOrder(self):
        trialTypes=[]
        
        Odorreinforce=[]
        Blankreinforce=[]
        
        probes=self.Info["GeneralizationProbes"]
            
        reinforcerList=[]
        probenumbers=[]
        probeList=[]
        blocks=round(self.Info['NumberTrials']/10)

        #Calculate number of odor and non odor trials for a block of 10 trials
        odornumber=int(round(10*self.Info["OdorPrev"]))
        blanknumber=int (round(10-odornumber))
    
        eachportnumber=math.floor(odornumber/len(self.devices))
        unbalance=odornumber%len(self.devices) # get the remainder of dividing odor number by 3
       
        
        
        Odorreinforcenumber=int(math.floor(odornumber*self.Info["ReinforceTargets"]*blocks))
        nonreinforceodornumber=(blocks*odornumber)-Odorreinforcenumber
        
        Blankreinforcenumber=int(math.floor(blanknumber*self.Info["ReinforceBlanks"]*blocks))
        nonreinforceblanknumber=(blocks*blanknumber)-Blankreinforcenumber
        
        
        for i in range(0,Odorreinforcenumber):
            Odorreinforce.append(1)
        for i in range(0, nonreinforceodornumber):
            Odorreinforce.append(0)
        random.shuffle(Odorreinforce)
        
        for i in range(0, Blankreinforcenumber):
            Blankreinforce.append(1)
        for i in range(0, nonreinforceblanknumber):
            Blankreinforce.append(0)
        random.shuffle(Blankreinforce)
        
        
        for i in range(0, probes): 
            probenumbers.append(1)    
        for i in range(0, len(Odorreinforce)-probes):
            probenumbers.append(0)
        random.shuffle(probenumbers)
        

        for i in range(0,blocks): #4 block of 10 trials for 40 trials
            odorlist=[]
            portlist=[]
            for i in range(0,len(self.devices)):
                portlist.append("port{}".format(str(i+1)))
                
            #Make an odor list with each of the olfactometer numbers for the number of times the port should appear    
            for i in range(0, eachportnumber):
                for i in portlist:
                    odorlist.append(i)
             
            additionals=random.sample(portlist,unbalance)
            odorlist=odorlist+additionals
            for i in range (0, blanknumber):
                odorlist.append('blank')
            #shuffle to randomize the mix
            random.shuffle(odorlist)
            trialTypes=trialTypes+odorlist 
        
        reinforcerIndex=0
        blankReinforceIndex=0
        
        for i in trialTypes:
            if i != "blank":
                toReinforce=Odorreinforce[reinforcerIndex]
                if probenumbers[reinforcerIndex]==1:
                    toReinforce=0
    
                reinforcerList.append(toReinforce)
                probeList.append(probenumbers[reinforcerIndex])
                reinforcerIndex=reinforcerIndex+1
            else:
                reinforcerList.append(Blankreinforce[blankReinforceIndex])
                blankReinforceIndex=blankReinforceIndex+1
                probeList.append(0)
        
        return(trialTypes, reinforcerList, probeList)
    
    
    
    
    
    def createOdorDictionary(self):
        #Create Dictionary of odors
        myodors={}
        myvalves={}
        pins=[1,2,3,4,5,6]
        Odornames=[self.Info["Odor1"], self.Info["Odor2"],self.Info["Odor3"],
               self.Info["Odor4"], self.Info["Odor5"],self.Info["Odor6"]]
        index=0        
        for i in pins:
            myodors[i]=Odornames[index]
            myvalves[Odornames[index]]=i
            index=index+1    
        return(myodors, myvalves, Odornames)
           
        
    
    def getTemperature(self):
        vals=[]
        for key in self.devices:
            vals.append(float(self.devices[key].readTemp()))
        AvgVal=sum(vals)/len(vals)
        return(AvgVal)
    
    def getHumidity(self):
        vals=[]
        for key in self.devices:
            vals.append(float(self.devices[key].readHumidity()))
        AvgVal=sum(vals)/len(vals)
        return(AvgVal)
    
    def getPressure(self):
        vals=[]
        for key in self.devices:
            vals.append(float(self.devices[key].readPressure()))
        AvgVal=sum(vals)/len(vals)
        return(AvgVal)
    
    
    def runExhaust(self):
        for key in self.devices:
            self.devices[key].exhaustOn()
    
    def stopExhaust(self):
        for key in self.devices:
            self.devices[key].exhaustOff()
        
        
    def recordData(self):
        now=datetime.now()
        timestamp=now.strftime("%m_%d_%y_%H_%M_%S")
        

                
        trialData=[self.Info["DogName"], self.Info["ExpName"],
                   self.Info["NumberTrials"],
                   self.Info["TrialSniff"], self.Info["TrialTime"],
                   self.Info["SessionNumber"], self.Info['DaySession'],
                    self.Info['TrainingLevel'],self.Info["HandlerBlind"],
                    self.Info["WaitforCorrect"], self.Info['RunCorrections'],
                    self.Info["OdorPrev"], self.Info["ReinforceBlanks"],
                    self.Info["ReinforceTargets"], self.Info["Tones"],
                    self.Info["GeneralizationProbes"], self.Info["AutoScore"],
                    self.Info["Notes"],
                   self.Trial["correctPort"],
                   self.Trial['response'], self.Trial['latency'],
                   self.Trial['poke1number'], self.Trial['poke2number'],
                   self.Trial['poke3number'], self.Trial['cumulative1'],
                   self.Trial['cumulative2'], self.Trial['cumulative3'],
                   self.Trial['firstResponse'],timestamp, self.port1Odor,
                   self.port2Odor, self.port3Odor, self.Temp, self.Humidity,
                   self.Pressure, self.Trial["pokeOrder"], self.Trial["pokeTimes"], 
                   "ITIs",
                   self.Trial["reinforce"], self.Trial["probe"], self.Trial["TrialNumber"]]
        
        self.Info['datasheet'].appendrow(trialData)
  
    
    
    def odorOn(self, port, probe=0):
        #Activate the Target port and distractor for the remainder
        Targets=self.Info['Targets']
        Distractors=self.Info['Distractors']
        Probes=self.Info['Probes']

        if port=="port1":
            target=random.choices(Targets, weights=self.Info["OdorWeights"])[0]
            if probe==1:
                target=Probes[0]
            self.devices['Olfactometer1'].activateValve(self.valves[target])
            self.port1Odor=target
        else: 
             distractor=random.choice(Distractors)
             self.devices["Olfactometer1"].activateValve(self.valves[distractor])
             self.port1Odor=distractor
        
        if port=="port2":
            target=random.choices(Targets, weights=self.Info["OdorWeights"])[0]
            if probe==1:
                target=Probes[0]
            self.devices['Olfactometer2'].activateValve(self.valves[target])
            self.port2Odor=target
        else: 
             distractor=random.choice(Distractors)
             self.devices["Olfactometer2"].activateValve(self.valves[distractor])
             self.port2Odor=distractor
        
        if port=="port3":
            target=random.choices(Targets, weights=self.Info["OdorWeights"])[0]
            if probe==1:
                target=Probes[0]
            self.devices['Olfactometer3'].activateValve(self.valves[target])
            self.port3Odor=target
        else: 
             distractor=random.choice(Distractors)
             self.devices["Olfactometer3"].activateValve(self.valves[distractor])
             self.port3Odor=distractor
            
            
    def lookForResponse(self, port, waitforcorrect, timeout, blankSearch):
        self.Trial={}
        self.Trial["correctPort"]=port
        self.isSniffed=0
        self.startTime=time.time()
        self.Trial['response']=0
        self.Trial['latency']=0
        self.Trial['poke1number']=0
        self.Trial['poke2number']=0
        self.Trial['poke3number']=0
        self.Trial['cumulative1']=0
        self.Trial['cumulative2']=0
        self.Trial['cumulative3']=0
        self.Trial['firstResponse']=0
        self.Trial['pokeOrder']=[]
        self.Trial['pokeTimes']=[]
        self.lastResponse=0
        self.waitforcorrect=waitforcorrect
             
        while(self.Trial['response']==0):
            sniff1=int(self.devices["Olfactometer1"].readIRs())
            self.checkResponse(sniff1, "port1")
            if self.Trial['response']==0:
               sniff2=int(self.devices["Olfactometer2"].readIRs())
               self.checkResponse(sniff2, "port2")
               if self.Trial['response']==0:
                  sniff3=int(self.devices["Olfactometer3"].readIRs())
                  self.checkResponse(sniff3, "port3")
                  if self.Trial['response']==0:
                      #Check for a timeout
                      if time.time()-self.startTime>timeout:
                          self.Trial['response']="timeout"
                          
                      ###Check if it was an all clear response
                      if blankSearch=='yes':
                          if self.Trial['poke1number']>0 and self.Trial['poke2number']>0 and self.Trial['poke3number']>0:
                              if self.waitforcorrect=="Yes":
                                  if port=="blank":
                                      if time.time()-self.lastResponse>self.Info['TrialSniff']/1000:
                                          self.Trial['response']="all clear"                                    
                              else:
                                 if time.time()-self.lastResponse> self.Info['TrialSniff']/1000:
                                     self.Trial['response']="all clear"
                          
                          
                              
        return(self.Trial)  
   
    
    def checkResponse(self, sniffTime, port):
    
        if port=="port1":
                datalist=["poke1number", "cumulative1"]
        if port=="port2":
                datalist=["poke2number", "cumulative2"]
        if port=="port3":
                datalist=["poke3number", "cumulative3"]
        
        if sniffTime>0:
               self.Trial[datalist[0]]=self.Trial[datalist[0]]+1
               self.Trial[datalist[1]]=self.Trial[datalist[1]]+sniffTime
               self.Trial['pokeOrder'].append(port)
               self.Trial['pokeTimes'].append(sniffTime)
               self.lastResponse=time.time()
              
               if self.isSniffed==0:
                   self.Trial['latency']=time.time()-self.startTime
                   self.isSniffed=1
                   
        if sniffTime>=self.Info["TrialSniff"]:
                 if self.Trial['firstResponse']==0:
                     self.Trial['firstResponse']=port
                 if self.waitforcorrect=='Yes':
                     if self.Trial["correctPort"]==port:
                         self.Trial['response']=port
                    
                 if self.waitforcorrect=="No":
                    self.Trial['response']=port
        
        
    def odorOff(self):
        for i in range (1,7):
            for key in self.devices:
                self.devices[key].deactivateValve(i)
            






    
class Threshold(AFCThread):
    statusUpdate=QtCore.pyqtSignal(str)
    trialNum=QtCore.pyqtSignal(int)
    msg=QtCore.pyqtSignal(str)
   
    
    def __init__(self, Devices, Info):     
        QtCore.QThread.__init__(self)
        self.stopped = QtCore.QEvent(QtCore.QEvent.User)
        self.stopped.setAccepted(False)
        self.devices=Devices
        self.Info=Info
        wd=os.getcwd()
        self.sound ='{}/Tones/food.wav'.format(wd)
        self.tone ='{}/Tones/432_short.wav'.format(wd)
        self.fail ='{}/Tones/fail_buzzer.wav'.format(wd)
        self.end ='{}/Tones/beepEnd.wav'.format(wd)
        self.odorOff()
        self.concentrationIndex=0
        self.reversals=0
        self.reversalList=[]
        self.answerList=[]
        self.correctList=[]
        self.wrongList=[]
        
        
    def run(self):   
        self.initializeRun()
       
        trial=0
        for i in self.trialOrder:
            port=i
            self.updateMessage(port, trial+1)
            self.odorOn(port, self.concentrationIndex)
            
            #Start the Trial
            self.startTime= time.time()
            self.playAudio(self.tone)
            
            self.Trial=self.lookForResponse(port=port, 
                                            waitforcorrect=self.Info["WaitforCorrect"],
                                            timeout= self.Info["TrialTime"], 
                                            blankSearch="yes")
             
            self.giveFeedback(port, trial)
            self.odorOff() #Clear the ports
            self.runExhaust()
            self.statusUpdate.emit("Odor Off")
            
            self.Trial["reinforce"]=self.outcome[trial]
            self.Trial["probe"]=self.probes[trial]
            self.Trial['TrialNumber']=trial+1
            self.recordData()
            
            
            self.evalConcentration()
            
            if self.reversals>7:
                self.playAudio(self.sound)
                time.sleep(0.5)
                self.playAudio(self.sound)
                break
            
            if self.concentrationIndex>2:
                self.playAudio(self.sound)
                time.sleep(0.5)
                self.playAudio(self.sound)
                break
           
            
            #ITI
            time.sleep(20)
            trial=trial+1
            self.stopExhaust()
            
            
        self.statusUpdate.emit("Finished")
        if self.reversals>7:
            self.statusUpdate.emit("Reached Threshold")
        elif self.concentrationIndex>2:
            self.statusUpdate.emit("Passed ALl Conc")
        else:
            self.statusUpdate.emit("TimedOut")
            
        self.playAudio(self.sound)
        time.sleep(0.5)
        self.playAudio(self.sound)



    def evalConcentration(self):
        if self.answerList[-1]==0:
            self.answerList=[]
            if self.concentrationIndex>0:
                self.concentrationIndex=self.concentrationIndex-1
                self.reversalList.append("Up")
                self.evalReversal()
                
        if len(self.answerList)==2:
            if self.answerList[-1]==1 and self.answerList[-2]==1:
                self.concentrationIndex=self.concentrationIndex+1
                self.reversalList.append("Down")
                self.evalReversal()
                self.answerList=[]
    
    
    def evalReversal(self):
        if len(self.reversalList)>1:
            if self.reversalList[-1] != self.reversalList[-2]:
                self.reversals=self.reversals+1
    
    

    def giveFeedback(self, port, trial):  
        if port==self.Trial['response']: 
            if self.outcome[trial]==1:
                self.playAudio(self.sound)
                time.sleep(1)
                self.playAudio(self.end)
                self.correct=1
                self.correctList.append(1)
                self.wrongList.append(0)
                self.answerList.append(1)
            else:
                self.playAudio(self.end)
                self.correct=0
                self.correctList.append(0)
                self.wrongList.append(1)
                self.answerList.append(1)
                
        elif port=="blank" :
            if self.outcome[trial]==1:
                if self.Trial['response']=="all clear":
                    self.playAudio(self.sound)  
                    time.sleep(1)
                    self.playAudio(self.end)
                    self.correct=1
                    self.correctList.append(1)
                    self.wrongList.append(0)
                    self.answerList.append(1)
            else:
                if self.Trial['response']!= "all clear":
                    self.playAudio(self.fail)
                    time.sleep(1)
                    self.correct=0
                    self.correctList.append(0)
                    self.wrongList.append(1)
                    self.playAudio(self.end)
                    self.answerList.append(0)
                    
        
        else: 
            self.playAudio(self.fail)
            time.sleep(1)
            self.playAudio(self.end)
            self.correct=0
            self.correctList.append(0)
            self.wrongList.append(1)
            self.answerList.append(0)
   
    
    
    def odorOn(self, port, targetIndex=0):
        #Activate the Target port and distractor for the remainder
        Targets=self.odorNames[0:3]
        Distractors=self.odorNames[3:6]

        if port=="port1":
            self.devices['Olfactometer1'].activateValve(self.valves[Targets[targetIndex]])
            self.port1Odor=Targets[targetIndex]
        else: 
             distractor=Distractors[targetIndex]
             self.devices["Olfactometer1"].activateValve(self.valves[distractor])
             self.port1Odor=distractor
        
        if port=="port2":
            self.devices['Olfactometer2'].activateValve(self.valves[Targets[targetIndex]])
            self.port2Odor=Targets[targetIndex]
        else: 
             distractor=Distractors[targetIndex]
             self.devices["Olfactometer2"].activateValve(self.valves[distractor])
             self.port2Odor=distractor
        
        if port=="port3":
            self.devices['Olfactometer3'].activateValve(self.valves[Targets[targetIndex]])
            self.port3Odor=Targets[targetIndex]
        else: 
             distractor=Distractors[targetIndex]
             self.devices["Olfactometer3"].activateValve(self.valves[distractor])
             self.port3Odor=distractor



    def recordData(self):
        now=datetime.now()
        timestamp=now.strftime("%m_%d_%y_%H_%M_%S")
                
        trialData=[self.Info["DogName"], self.Info["ExpName"],
                   self.Info["NumberTrials"],
                   self.Info["SniffTime"], self.Info["TrialTime"],
                   self.Info["SessionNumber"], self.Info['DaySession'],
                    self.Info['TrainingLevel'],self.Info["HandlerBlind"],
                    self.Info["WaitforCorrect"], self.Info['RunCorrections'],
                    self.Info["OdorPrev"], self.Info["ReinforceBlanks"],
                    self.Info["ReinforceTargets"], self.Info["Tones"],
                    self.Info["GeneralizationProbes"], self.Info["AutoScore"],
                    self.Info["Notes"],
                   self.Trial["correctPort"],
                   self.Trial['response'], self.Trial['latency'],
                   self.Trial['poke1number'], self.Trial['poke2number'],
                   self.Trial['poke3number'], self.Trial['cumulative1'],
                   self.Trial['cumulative2'], self.Trial['cumulative3'],
                   self.Trial['firstResponse'],timestamp, self.port1Odor,
                   self.port2Odor, self.port3Odor, self.Temp, self.Humidity,
                   self.Pressure, self.Trial["pokeOrder"], self.Trial["pokeTimes"], 
                   "ITIs",
                   self.Trial["reinforce"], self.Trial["probe"], self.Trial["TrialNumber"], 
                   self.concentrationIndex, self.odorNames[self.concentrationIndex], self.reversals]
        self.Info['datasheet'].appendrow(trialData)
        




class GoNoGoThread(AFCThread):
    statusUpdate=QtCore.pyqtSignal(str)
    trialNum=QtCore.pyqtSignal(int)
    msg=QtCore.pyqtSignal(str)
   
    
    def __init__(self, Devices, Info):     
        QtCore.QThread.__init__(self)
        super().__init__(Devices, Info)
        self.stopped = QtCore.QEvent(QtCore.QEvent.User)
        self.stopped.setAccepted(False)
        self.devices=Devices
        self.Info=Info
        
        
        
   
   

    def lookForResponse(self, port, waitforcorrect, timeout, blankSearch):
        self.Trial={}
        self.Trial["correctPort"]=port
        self.isSniffed=0
        self.startTime=time.time()
        self.Trial['response']=0
        self.Trial['latency']=0
        self.Trial['poke1number']=0
        self.Trial['poke2number']=0
        self.Trial['poke3number']=0
        self.Trial['cumulative1']=0
        self.Trial['cumulative2']=0
        self.Trial['cumulative3']=0
        self.Trial['firstResponse']=0
        self.Trial['pokeOrder']=[]
        self.Trial['pokeTimes']=[]
        self.lastResponse=0
        self.waitforcorrect=waitforcorrect
             
        while(self.Trial['response']==0):
            sniff1=int(self.devices["Olfactometer1"].readIRs())
            self.checkResponse(sniff1, "port1")
        
            if self.Trial['response']==0:
                      #Check for a timeout
                     print("checking for all clear")
                     if time.time()-self.startTime>timeout:
                          self.Trial['response']="timeout"
                          
                      ###Check if it was an all clear response
                     if blankSearch=='yes':
                          print("blank search is yes")
                          if self.Trial['poke1number']>0 :
                              print("poke1 number is >0")
                              if self.waitforcorrect=="Yes":
                                  if port=="blank":
                                      if time.time()-self.lastResponse>(self.Info['TrialSniff'])/1000:
                                          self.Trial['response']="all clear"                                    
                              else:
                                 print ("Checking the time")
                                 print (self.Info['TrialSniff'])
                                 print (time.time()-self.lastResponse)
                                 if time.time()-self.lastResponse> (self.Info['TrialSniff'])/1000:
                                     
                                     self.Trial['response']="all clear"
                                     
        return(self.Trial)                          
                                     
                          
    def odorOn(self, port, probe=0):
        #Activate the Target port and distractor for the remainder
        Targets=self.Info['Targets']
        Distractors=self.Info['Distractors']
        Probes=self.Info['Probes']
        self.port2Odor="NA"
        self.port3Odor="NA"
        
        if port=="port1":
            target=random.choices(Targets, weights=self.Info["OdorWeights"])[0]
            if probe==1:
                target=Probes[0]
            self.devices['Olfactometer1'].activateValve(self.valves[target])
            self.port1Odor=target
          
        else: 
             distractor=random.choice(Distractors)
             self.devices["Olfactometer1"].activateValve(self.valves[distractor])
             self.port1Odor=distractor
        
        
            

      
class Arduino(object):

    def __init__(self, port):   
  
        self.status='not connected'
        try:
            self.serial = serial.Serial (port, 9600)
            self.status= "Connected"
            print('connected')
            time.sleep(1)
         
        except:
              self.status="Maybe not Connected"  

    def returnport(self):
        return self.port
        
    def returnstatus(self):
        return self.status
        
        
    def activateValve(self, pin):
        self.__sendData1('1\r')
        self.__sendData1(str(pin)+ '\r')
        #val=self.__getData()
        #return (val)
        
    def deactivateValve(self, pin):
        self.__sendData1('2\r')
        self.__sendData1(str(pin)+ '\r')
        time.sleep(.01)
        #val=self.__getData()
        #return (val)
        
    def panelDown(self):
        self.__sendData1('6\r')
       
        
    def panelUp(self):
        self.__sendData1('7\r')
        
        
    def whatisyourname (self):
        self.__sendData1('4\r')
        myname=self.__getData()
        return (myname)
    
    def readIRs(self):
        self.__sendData1('5\r')
        val=self.__getData()
        return (val)
    
    def updateSniffTime(self, time):
        self.__sendData1('14\r')
        self.__sendData1('{}\r'.format(time))
        
    def runFeeder (self):
        self.__sendData1('8\r')
        
        
    def readTemp(self):
        self.__sendData1('9\r')
        val=self.__getData()
        return(val)
    
    def readHumidity(self):
        self.__sendData1('10\r')
        val=self.__getData()
        return(val)
    
    def readPressure(self):
        self.__sendData1('11\r')
        val=self.__getData()
        return(val)
        
    def exhaustOn(self):
        self.__sendData1('12\r')
        
    def exhaustOff(self):
        self.__sendData1('13\r')
   
    def __sendData1(self, serial_data):
        #print('sent: {}'.format(serial_data))
        serial_data = str(serial_data).encode('utf-8')
        self.serial.write(serial_data)
        print("sent {}".format(serial_data))
        time.sleep(0.01)
        

    def __getData(self):
        input_string = self.serial.readline()
        input_string = input_string.decode('utf-8')
        print ('recieved: {}'.format(input_string))
        return input_string.rstrip()    

    def __formatPinState(self, pinValue):
        if pinValue == '1':
            return True
        else:
            return False

    def close(self):
        self.serial.close()
        return True

if __name__ == "__main__":main()
