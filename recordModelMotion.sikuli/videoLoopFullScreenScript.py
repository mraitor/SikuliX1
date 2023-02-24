#make videos in file full screen and loop
import time

for i in range(0,96):
    #click("1676503248067.png")
    click(Pattern("1677172489285.png").similar(0.91))
    #click(Pattern("1677178090795.png").similar(0.80))

    #click(Pattern("1676504083345.png").targetOffset(155,-123))
    click(Pattern("1677172223351.png").targetOffset(200,-200))

    click("1676503372713.png")
    click("1676503393645.png")
    click("1676503408328.png")
    #click("1676503248067.png")
    click(Pattern("1677172489285.png").similar(0.91))
    #click(Pattern("1677178090795.png").similar(0.80))
    type(Key.DOWN)
 
    time.sleep(1)