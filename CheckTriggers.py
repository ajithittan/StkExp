import configparser
import configparser
from TurtleProgram import retrievedatafromweb

class checkTriggers:

    def checkforsignificantchange (self,inpVal):

        config = configparser.ConfigParser()
        config.read("configitems.ini")

        listofStks = retrievedatafromweb().retDataToRun(inpVal)
        print("trigger....",listofStks)

objretdata = checkTriggers()
objretdata.checkforsignificantchange("CURRENT")
