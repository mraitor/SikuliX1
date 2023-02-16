#imports
import time

#constants
playWaitTimeSec = 23

#read txtfile with perturbations
pertFile = '/Volumes/Extreme SSD/Balance Metric/Scripts/' + 'PerturbationFileNames_pertID_5.txt'
f = open(pertFile, 'r')
trialList = f.readlines()
trialList = trialList[1:]
#for trialNamei, trialName in enumerate(trialList):
#    trialList[trialNamei] = trialList[trialNamei][-21:-13]

#print(trialList[trialNamei])
#trial1 = "S05DA101"
#trial2 = "S10DA401"
#trialList = [[trial1], [trial2]]

#subjectList = [5,6,7,8,9,10,11,12,13,14]
#conditionList = ['N','A','E','P']
#pertNumber = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
#for subject in subjectList:
#    for condition in conditionList:
#        for pert in pertNumber:
            

for trial in trialList:
    #trial = trial[0]
#    session = trial[0:6]
#    if trial[1] == '0':
#        subjectStr = "Subject " + trial[2:3]
#    elif trial[1] == '1':
#        subjectStr = "Subject " + trial[1:3]
#    else:
#        print('invalid subject number')
#        break
    
    #trialFile = '/Volumes/Extreme SSD/Balance Metric/' + subjectStr + '/OpenSim/' + session + '/IK/' + trial + '_ik.mot'
    trialFile = trial[:-1] #remove '/n' from string
    
    #print(trial[-21:-13])
    #open opensim
    openSimApp = App.open("/Applications/OpenSim 4.1/OpenSim 4.1.app") 

    wait("1675448932598.png")
            
    time.sleep(3)
    
    type('o',Key.CMD)

    wait("1675448976414.png")

    time.sleep(1)
    doubleClick("1675381542332.png")
    time.sleep(1)

    wait(Pattern("1675382558067.png").targetOffset(-148,0))
    time.sleep(1)

    click(Pattern("1675382558067.png").targetOffset(-148,0))

    click("1675382655445.png")
   
    #load motion
    wait("1675449104492.png")
    
    click(Pattern("1670294082506.png").targetOffset(-8,66))
    
    loadMotionString = "loadMotion('" + trialFile + "')" +'\n'
    
    type(loadMotionString)
    
    #wait("1675368575564.png")
    #doubleClick("1675368575564.png")
    time.sleep(2)

    #coordinates changed to datatype=double after matlab processing
   # wait("1675368666912.png")
    #doubleClick("1675368666912.png")
    
    wait("1675926452991.png")
    
    doubleClick("1675926452991.png")


                        
    time.sleep(1)

    #view from right
   # click("1675382726625.png")
   #view from front
    click("1675450497295.png")
            
    time.sleep(1)
    click("1675366650633.png")
    time.sleep(1)
    
    click("1675366677282.png")
    
    time.sleep(playWaitTimeSec)
    
    click("1675366747828.png")
    
    #type(Key.DELETE)
    
    wait(Pattern("1675367179190.png").targetOffset(60,0))

    type('Balance Metric Opensim Videos/' + trial[-21:-13] + '.webm' + '\n')

    #close opensim
    click(Pattern("1675383581032.png").targetOffset(-33,-18))

    wait("1675381706145.png")
    click("1675381706145.png")
    
    wait("1675450635123.png")
    
    time.sleep(2)

    
    #rightClick("1675369783302.png")
    #click("1675369829650.png")
 #   time.sleep(1)


#click(Pattern("1670294082506.png").targetOffset(-8,66))

#completeMessage = 'Sikulix Script Complete' + '\n'

#type(completeMessage)