###################
# Imports go here #
###################
from os import system
import time
import string
import re
import csv

###################
#   END IMPORTS   #
###################

####################
# Needed vars here #
####################
bslash = "\\"
installPath = "c:\BirdyDeployer"
remotePath = bslash * 2 + "127.8.9.10\networkdeploymentshare\AutoDeploy\AutoInstall"
words = []
d = {}

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

###################################################
# Start Some Function # Annoying Separator Bar 😈 #
###################################################

# TODO stuffs here, lorum ipsum, n stuff, lulz

####################################################
# END of Some Function # Annoying Separator Bar 😈 #
####################################################

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

######################################################
# Start Package Obtainer # Annoying Separator Bar 😈 #
######################################################

def pkgDownloader(returnDeploy):
    # get deployType
    deployType = returnDeploy
    # TODO package downloader here
    # Deploy type could be (MSR, Accounting, etc..)
    deployBase = "C:\AutoInstaller\\"
    deployFlags = []
    ## todo : thoughts below
    # while deployType is equal to deployDepts.txt item, get deployItems?
    # using a key from the text file to match deployType, so MSR, IT, etc..


    # Open the deployDepts file and read it
    with open("deployDepts.txt", 'r') as dlist:
        for line in dlist:
            for word in line.split():
                if word in line.split() == deployType:
                    rescap = word in line.split()
                    print("Gathering resources for " + str(deployType) + " department...")

                    # Todo: finish the package downloader ... LALALALALALALALAA README
                    # Todo: next step: gather resources for selected dept from remote path
                    # todo: stick downloaded stuff from remote path to "deployBase".

                    # todo: deploy downloaded stuff

#######################################################
# END of Package Obtainer # Annoying Separator Bar 😈 #
#######################################################

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

###############################################
# Start Main Menu # Annoying Separator Bar 😈 #
###############################################
def AppMetas():

    # Creating a dictionary for all my info and crap
    AppData =  {
        "Name": "BirdyDeployer",
        "Author": "DogeBird",
        "Description": "Use this to quickly deploy assets to department employees with ease."
    }
    return AppData

# Yo -->
    # Defining some variables we may use later in the menus
AppName = ("Name: " + AppMetas().get('Name'))
AppAuthor = ("Author: ") + AppMetas().get('Author')
AppDesc = ("Description: ") + AppMetas().get('Description')

################################################
# END of Main Menu # Annoying Separator Bar 😈 #
################################################


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#####################################################
# Start Deployment Menu # Annoying Separator Bar 😈 #
###############################w######################
def deploymentMenu():
    # Clear screen, bla bla
    system("cls")

    # Create DEPLOYMENT Menu Selection
    deployDict = {
        "01": "1.  Customer Service",
        "02": "2.  Tech Support I",
        "03": "3.  Tech Support II",
        "04": "4.  Tech Support III",
        "05": "5.  Human Resources",
        "06": "6.  Telecom",
        "07": "7.  Networking",
        "08": "8.  Financial",
        "09": "9.  Some other dept 1",
        "10": "10. Some other dept 2",
        "11": "11. Some other dept 3",
        "12": "12. Some other dept 4",
        "13": "13. Some other dept 5",
        "14": "14. Some other dept 6",
        "15": "15. Some other dept 7",
        "16": "16. Some other dept 8",
        "17": "17. Some other dept 9",
        "18": "18. Some other dept 10",
        "19": "19. Some other dept 11",
        "20": "20. Some other dept 12",
        "21": "21. Exit"
    }

    print ("Make a selection from the menu below.")

    # Start Deployment menu top
    dmenuTop="""
    [B] [I] [R] [D] [Y] [D] [E] [P] [L] [O] [Y]
    *******************************************
    *""" + """ Application """ + AppName + """              *
    * """ + AppAuthor + """                 *
    *****************************************************************************************
    * Select the appropriate department, this will deploy all needed software for that user *
    *****************************************************************************************"""

    print(dmenuTop)

    # Draw menu box
    menuboxDeploy = """
    **************************************************************
    *    """ + deployDict.get('01') + """                                          *
    *    """ + deployDict.get('02') + """                             *
    *    """ + deployDict.get('03') + """                                              *  
    *    """ + deployDict.get('04') + """                                    *  
    *    """ + deployDict.get('05') + """                                          *  
    *    """ + deployDict.get('06') + """                  *  
    *    """ + deployDict.get('07') + """                                       *  
    *    """ + deployDict.get('08') + """                                            *  
    *    """ + deployDict.get('09') + """                                           *  
    *    """ + deployDict.get('10') + """                                         *  
    *    """ + deployDict.get('11') + """                                     *  
    *    """ + deployDict.get('12') + """                                               *  
    *    """ + deployDict.get('13') + """                                      *  
    *    """ + deployDict.get('14') + """                                     *  
    *    """ + deployDict.get('15') + """                                 *  
    *    """ + deployDict.get('16') + """                                          *  
    *    """ + deployDict.get('17') + """                                             *  
    *    """ + deployDict.get('18') + """                                  *  
    *    """ + deployDict.get('19') + """                                   *  
    *    """ + deployDict.get('20') + """                                          *  
    *    """ + deployDict.get('21') + """                                                *  
    **************************************************************"""

    # show Deployment menu selections
    print (menuboxDeploy)

    # Deployment menu selection process
    dpmenuSel = input("Make a selection: ")
    print("You selected: " + dpmenuSel)
    dpconfirm = input("Continue? (Y/N): ")
    dpconfirm = dpconfirm.upper()

    if (dpmenuSel == "1"):
        if(dpconfirm == "Y"):
            system("cls")
            deploymentMenu.deployType = ["CustomerService"]
            print("1. Customer Service Selected")
            pkgDownloader(deploymentMenu.deployType)
    elif (dpmenuSel == "2"):
        if(dpconfirm == "Y"):
            system("cls")
            deploymentMenu.deployType = ["TechSupport I"]
            print ("2. Tech Support I Selected")
            pkgDownloader(deploymentMenu.deployType)
    elif (dpmenuSel == "3"):
        if(dpconfirm == "Y"):
            system("cls")
            deploymentMenu.deployType = ["TechSupport II"]
            print ("3. Tech Support II Selected")
            pkgDownloader(deploymentMenu.deployType)
    elif (dpmenuSel == "4"):
        if(dpconfirm == "Y"):
            system("cls")
            deploymentMenu.deployType = ["TechSupport III"]
            print ("4. Tech Support III Selected")
            pkgDownloader(deploymentMenu.deployType)
    elif (dpmenuSel == "5"):
        if(dpconfirm == "Y"):
            system("cls")
            deploymentMenu.deployType = ["HumanResources"]
            print ("5. Human Resources Selected")
            pkgDownloader(deploymentMenu.deployType)
    elif (dpmenuSel == "6"):
        if(dpconfirm == "Y"):
            system("cls")
            deploymentMenu.deployType = ["Telecom"]
            print ("6. Telecom Selected")
            pkgDownloader(deploymentMenu.deployType)
    elif (dpmenuSel == "7"):
        if(dpconfirm == "Y"):
            system("cls")
            deploymentMenu.deployType = ["Networking"]
            print ("7. Networking Selected")
            pkgDownloader(deploymentMenu.deployType)
    elif (dpmenuSel == "8"):
        if(dpconfirm == "Y"):
            system("cls")
            deploymentMenu.deployType = ["Financial"]
            print ("8. Financial Selected")
            pkgDownloader(deploymentMenu.deployType)
    elif (dpmenuSel == "9"):
        if(dpconfirm == "Y"):
            system("cls")
            deploymentMenu.deployType = ["Someotherdept1"]
            print ("9. Some other dept 1 Selected")
            pkgDownloader(deploymentMenu.deployType)
    elif (dpmenuSel == "10"):
        if(dpconfirm == "Y"):
            system("cls")
            deploymentMenu.deployType = ["Someotherdept2"]
            print ("10. Some other dept 2 Selected")
            pkgDownloader(deploymentMenu.deployType)
    elif (dpmenuSel == "11"):
        if(dpconfirm == "Y"):
            system("cls")
            deploymentMenu.deployType = ["Someotherdept3"]
            print ("11. Some other dept 3 Selected")
            pkgDownloader(deploymentMenu.deployType)
    elif (dpmenuSel == "12"):
        if(dpconfirm == "Y"):
            system("cls")
            deploymentMenu.deployType = ["Someotherdept4"]
            print ("12. Some other dept 4 Selected")
            pkgDownloader(deploymentMenu.deployType)
    elif (dpmenuSel == "13"):
        if(dpconfirm == "Y"):
            system("cls")
            deploymentMenu.deployType = ["Someotherdept5"]
            print ("13. Some other dept 5 Selected")
            pkgDownloader(deploymentMenu.deployType)
    elif (dpmenuSel == "14"):
        if(dpconfirm == "Y"):
            system("cls")
            deploymentMenu.deployType = ["Someotherdept6"]
            print ("14. Some other dept 6 Selected")
            pkgDownloader(deploymentMenu.deployType)
    elif (dpmenuSel == "15"):
        if(dpconfirm == "Y"):
            system("cls")
            deploymentMenu.deployType = ["Someotherdept7"]
            print ("15. Some other dept 7 Selected")
            pkgDownloader(deploymentMenu.deployType)
    elif (dpmenuSel == "16"):
        if(dpconfirm == "Y"):
            system("cls")
            deploymentMenu.deployType = ["Someotherdept8"]
            print ("16. Some other dept 8 Selected")
            pkgDownloader(deploymentMenu.deployType)
    elif (dpmenuSel == "17"):
        if(dpconfirm == "Y"):
            system("cls")
            deploymentMenu.deployType = ["Someotherdept9"]
            print ("17. Some other dept 9 Selected")
            pkgDownloader(deploymentMenu.deployType)
    elif (dpmenuSel == "18"):
        if(dpconfirm == "Y"):
            system("cls")
            deploymentMenu.deployType = ["Someotherdept10"]
            print ("18. Some other dept 10 Selected")
            pkgDownloader(deploymentMenu.deployType)
    elif (dpmenuSel == "19"):
        if(dpconfirm == "Y"):
            system("cls")
            deploymentMenu.deployType = ["Someotherdept11"]
            print ("19. Some other dept 11 Selected")
            pkgDownloader(deploymentMenu.deployType)
    elif (dpmenuSel == "20"):
        if(dpconfirm == "Y"):
            system("cls")
            deploymentMenu.deployType = ["Someotherdept12"]
            print ("20. Some other dept 12 Selected")
            pkgDownloader(deploymentMenu.deployType)
# ------------------------------------------------- Exit Below
    elif (dpmenuSel == "21"):
        if(dpconfirm == "Y"):
            print("Exiting...")
            quit()

    returnDeploy = [deploymentMenu.deployType]
    return returnDeploy
# ------------------------------------------------- Exit Above

######################################################
# END of Deployment Menu # Annoying Separator Bar 😈 #
######################################################



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



###############################################
# Start Main Menu # Annoying Separator Bar 😈 #
###############################################

def mainMenu():
    # Clear the screen to look pretty and stuff
    system('cls')

    # Create an overly done garbage but beautifully simple menu
    menuTop="""
[B] [I] [R] [D] [Y] [D] [E] [P] [L] [O] [Y]
*******************************************
*""" + """ Application """ + AppName + """              *
* """ + AppAuthor + """                 *
*************************************************************************************
* """ + AppDesc + """ *
*************************************************************************************
"""

    # Print the overly done menu top in all of its glory
    print(menuTop)


    # Create Main Menu Selection
    menuDict = {
        "1": "1. Deploy a Laptop",
        "2": "2. Deploy a Desktop",
        "3": "3. Exit"
    }

    print ("Make a selection from the menu below.")

    # Draw menu box
    menuboxMain = """
    ******************************
    *    """ + menuDict.get('1') + """      *
    *    """ + menuDict.get('2') + """     *
    *    """ + menuDict.get('3') + """                 *  
    ******************************"""

    print (menuboxMain)
    # Time to see what the employee wants to do
    # Get the user selection input and do some crap
    # But, confirm they want to take the journey first!
    mainmenuSel = input("Make a selection: ")
    print("You selected: " + mainmenuSel)
    mmconfirm = input("Continue? (Y/N): ")
    mmconfirm = mmconfirm.upper()

    if (mainmenuSel == "1"):
        if(mmconfirm == "Y"):
            system("cls")
            deploymentMenu()
    elif (mainmenuSel == "2"):
        if(mmconfirm == "Y"):
            print ("2. Something more exciting")

    elif (mainmenuSel == "3"):
        if(mmconfirm == "Y"):
            print("Exiting...")
            quit()

################################################
# END of Main Menu # Annoying Separator Bar 😈 #
################################################

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

mainMenu()
