trial = "'/Volumes/Extreme SSD/Balance Metric/Subject 5/OpenSim/S05DA1/IK/S05DA101_ik.mot'"

click(Pattern("1670294082506.png").targetOffset(-8,66))

loadMotionString = "loadMotion(" + trial + ")" +'\n'

type(loadMotionString)
