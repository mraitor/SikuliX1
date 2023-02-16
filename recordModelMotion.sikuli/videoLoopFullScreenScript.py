#make videos in file full screen and loop
import time

for i in range(0,120):
    click("1676503248067.png")

    #click("1676503333316.png")
    click(Pattern("1676504083345.png").targetOffset(155,-123))

    click("1676503372713.png")
    click("1676503393645.png")
    click("1676503408328.png")
    click("1676503248067.png")

    type(Key.DOWN)
 
    time.sleep(1)