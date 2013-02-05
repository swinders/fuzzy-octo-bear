import serial
cc128 = serial.Serial("/dev/ttyUSB0", 57600, timeout=6)
cc128xml = cc128.readlines(6)

try:
        # Find the temperature
        tmprstart=cc128xml[0].find("<tmpr>")+len("<tmpr>")
        tmprend=cc128xml[0].find("</tmpr>",tmprstart)
        tmpr=float(cc128xml[0][tmprstart:tmprend])
        # Find ch1
        ch1start=cc128xml[0].find("<ch1>")+len("<ch1>")
        ch1end=cc128xml[0].find("</ch1>",ch1start)
        ch1=cc128xml[0][ch1start:ch1end]
        # Find the power in watts
        wattsstart=ch1.find("<watts>")+len("<watts>")
        wattsend=ch1.find("</watts>",wattsstart)
        watts=int(ch1[wattsstart:wattsend])
        print "Temperature " + str(tmpr) + "C, Power " + str(watts) + "watts"
except:
        print cc128xml
        #colour="000" # Off/Black       
else:
        if watts>2000:
                colour="100" # Red
        else:
                colour="110" # Yellow
        if watts<500:
                colour="010" # Green
LedBorg = open('/dev/ledborg', 'w')     # Open LedBorg for writing
LedBorg.write(colour)                   # Write colour to the LedBorg
LedBorg.close()                         # Close the LedBorg
