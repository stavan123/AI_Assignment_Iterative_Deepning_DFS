import pygame 
from pygame import *
import sys
import time
import os
from cityXY import *

# from SearchGraph import *

##########################################################################################################
#  Author: ArgO1ne (Github: Stavan Khisty)
##########################################################################################################

dirname = os.path.dirname(__file__) #get the current directory


# initialize pygame
pygame.init()

###############################
# for images folder
filename = os.path.join(dirname, './images/')

###############################
# screen creation
screen = pygame.display.set_mode((863, 725))
pygame.display.set_caption(
    "Iterative DFS Visualisation ")
icon = pygame.image.load(filename + 'logo.png')
pygame.display.set_icon(icon)


################################
# city marker
dot = pygame.image.load(filename + 'dot.png')
dotx = 370
doty = 370


def cityMarker(): # The logo of the city
    screen.blit(dot, (dotx, doty))


#################################
# background image
bgImage = pygame.image.load(filename + 'bgImage.png')


def backgroungImage():
    screen.blit(bgImage, (0, 80)) 


#################################
# button
bState = False
depthBState = False
resultState = False
color = (80, 200, 120)
colorBright = (0, 168, 107)
startB = pygame.image.load(filename + 'startB.png')#Button Image for the start
depthB = pygame.image.load(filename + 'depthB.png')#Button Image for the destination


def StartButton():
    screen.blit(startB, (675, 15)) # Render the start button image on the screen


def depthButton():
    screen.blit(depthB, (60, 627))# # Render the depth button image on the screen


depthCountInt = 1 # Initialize the depth count to 1 initally
depthT = "" 
pathFontBT = pygame.font.SysFont(None, 25, bold=False, italic=False) #Rendering the font


def depthButtonT():
    pathTextDB = pathFontBT.render(depthT, True, (80, 200, 120))
    screen.blit(pathTextDB, [250, 649])


def depthButtonText():   #for instructing the increement of the depth
    depthInstruct = pathFontBT.render(
        "Click to increment depth", True, (80, 200, 120))
    screen.blit(depthInstruct, [60, 687])


resultB = pygame.image.load(filename + 'resultB.png')  # Load the image for generating the path


def resultButton():
    screen.blit(resultB, (610, 627)) # Render the generate path buttion the screen 


finalDepthText = "" # Text for the final depth text

finalDepthTe = pygame.font.SysFont(None, 31, bold=False, italic=False)# Spefify the font size of the final depth


def FinalDepthText():# Rendering the font for final depth Text
    finalDepthT = finalDepthTe.render(finalDepthText, True, (80, 200, 120))
    screen.blit(finalDepthT, [30, 655])


restartB = pygame.image.load(filename + 'restartB.png') # Load the image restart button


def restartButton():
    screen.blit(restartB, (371, 663)) # Render the restart button on the screen


#################################
# path message
instruct = "Simulation of iterative Depth First Search!!"
instruct1 = "Click once on any node to select Starting city."
instruct2 = "Again click on any node to select Destination city. "
pathT = ""

pathFont = pygame.font.SysFont(None, 31, bold=False, italic=False)# Specify the font style
pathFontT = pygame.font.SysFont(None, 25, bold=False, italic=False)# Specify the font style

# final path


def pathMessage():
    pathText = pathFont.render(pathT, True, (80, 200, 120))
    screen.blit(pathText, [30, 627])


def pathMessageSeq():

    pathText = pathFontT.render(instruct, True, (80, 200, 120))  #Rendering all the  text on the screen
    screen.blit(pathText, [28, 10])
    pathText1 = pathFontT.render(instruct1, True, (0, 0, 0)) #Rendering all the text on the screen
    screen.blit(pathText1, [28, 30])
    pathText2 = pathFontT.render(instruct2, True, (0, 0, 0))#Rendering all the text on the screen
    screen.blit(pathText2, [28, 50])


###################################
maker = pygame.font.SysFont(None, 21, bold=False, italic=False)
name = ""


def makerFun():
    makerT = maker.render(name, True, (80, 200, 120))
    screen.blit(makerT, [703, 710])


###################################
# tree geneartion list
tree = []
treeLength = 0
iteratorTree = 2
currentTree = []
printBool = False
finalPathPair = []


#################################
# draw edge line

# This function is used for the purpose 
#of drawing the edges of the graph
# after the start and the destination are specified
def takeEdgeDrawInput():
    city = getCityXY()
    edges = currentTree
    c1x = 0
    c1y = 0
    c2x = 0
    c2y = 0
    for e in edges:
        f1 = 0
        f2 = 0
        for c in city:
            if f1 == 0 or f2 == 0:

                if(c[0] == e[0]): 
                    c1x = c[1] #take the x coordinate
                    c1y = c[2]# take the y coordinate
                    f1 = 1

                if(c[0] == e[1]):
                    c2x = c[1]
                    c2y = c[2]
                    f2 = 1
            else:
                break

        if(sequence != -3):
            drawEdge(c1x, c1y, c2x, c2y) #This draw edge function is defined below
        else:
            drawEdgeFinal(c1x, c1y, c2x, c2y)# same for this


#####################################################
# speed of drawing line
drawSpeed = 0.2


def drawEdge(cx1, cy1, cx2, cy2):
    pygame.draw.line(screen, (0, 0, 203), [cx1, cy1], [cx2, cy2], 4)#203


def drawEdgeFinal(cx1, cy1, cx2, cy2):
    pygame.draw.line(screen, (51, 255, 0), [cx1, cy1], [cx2, cy2], 8) #surface, color, start and end position,width here 4


##################################
# end point
endPoint = pygame.image.load(filename + 'end.png')
ex = -1
ey = -1


def endpointPlot():
    screen.blit(endPoint, (ex, ey)) #blit takes image and its cordinates 


##################################
# Start point
startPoint = pygame.image.load(filename + 'start.png')
sx = -100
sy = -100


def startPointPlot():
    screen.blit(startPoint, (sx, sy))


###################################
# city coordiinates ---fileName: cityXY.py
cityPoint = getCityXY()
print(cityPoint[0][0]) #printing the city heuristics on the console

edges = getCityEdges()
print(edges[0][0], edges[0][1])


###################################
# find city name from click
def getCityFromClick(pos):
    margin = 18
    x = pos[0]
    y = pos[1]
    print(x, y)
    found = 0
    for c in cityPoint:
        px = c[1]
        py = c[2]
        # print(px, py)
        if (px-margin < x) and (px+margin > x) and (py-margin < y) and (py+margin > y):
            found = 1
            return c[0]

    return "notFound"


# sequence = 0 (both cities selected)
# sequence = 1 (start city not selected yet)
# seqence = 2 (end city not selected yet, start city selected)
sequence = 1
endCity = ""
startCity = ""


############################################################################################################################################
####################################################################################################################
# main algorithm logic


######################################################################################################################################
# Main iterative dfs logic


def read_graph():

    edges = {}#dictionary of the edges

    edgePair = getCityEdges()

    for roadInfo in edgePair:

        if (len(roadInfo) > 0):
            srcCity = roadInfo[0]
            destCity = roadInfo[1]
            print(srcCity, destCity)

            if srcCity in edges:
                edges[srcCity] = edges[srcCity] + [destCity]
            else:
                edges[srcCity] = [destCity]

            if destCity in edges:
                edges[destCity] = edges[destCity] + [srcCity]
            else:
                edges[destCity] = [srcCity]

    return edges


######################################
######################################


visitedPaths = ""
finalPath = []
countOfDepth = 0
tempVar = ""


def iterativeDFS(source, destination, maxDepth, edges):
    countOfIterarion = 0
    global countOfDepth, visitedPaths, tempVar
    tempVar = source

    # Check source and destination not in edges list
    if source not in edges.keys() or destination not in edges.keys():
        finalPath.append('FAIL')
        return finalPath

    for limit in range(maxDepth):
        # visited = source
        # print(source)
        countOfDepth = limit
        if depthLimitSearch(source, destination, limit, edges, source):
            countOfIterarion += 1
            print("#####################################################loop count:  " +
                  str(countOfIterarion) + "   limit:  " + str(limit))
            # prints all the visited states
            print(visitedPaths)
            finalPath.append(tempVar)
            finalPath.reverse()
            return finalPath
    # State not found Fail.
    finalPath.append("FAIL")
    return finalPath


def depthLimitSearch(source, destination, limit, edges, parent):

    global countOfDepth, visitedPaths, tempVar, finalPath

    # 3
    if (countOfDepth-limit) <= 0:
        tree.append(["aaa", "aaa"])
        visitedPaths += '\n' + source
        tree

        if(parent != source):
            print(parent + " --- " + source)
            tree.append([parent, source])

    else:
        visitedPaths += ('\n' + '\t' * (countOfDepth - limit)) + source
        print(parent + " --- " + source)
        tree.append([parent, source])

    # 3
    if source == destination:
        return True

    if limit < 1:
        return False

    temp = []
   
    for adjacentNode in edges[source]:
        # remove non included path nodes
        temp = edges[adjacentNode]
        if source in temp:
            temp.remove(source)
            edges[adjacentNode] = temp
        # recursive call to the DLS function with limit - 1
        # time.sleep(0.5)
        if depthLimitSearch(adjacentNode, destination, limit - 1, edges, source):
            # appends final node
            finalPath.append(adjacentNode)
            return True

    return False


#########################
# Main program
#########################
def main():
    print("Loading graph: ")
    edges = {}
    edges = read_graph()# This function returns the edges

    ##################################################################################################################
    # start = "Arad"
    # goal = "Eforie"
    start = startCity
    goal = endCity
    ###############################################################################################################

    print("  done.\n")

    # Comment out the following lines to hide the graph description.
    print("-- Adjacent Cities (Edge Dictionary Data) ------------------------")
    for location in edges.keys():
        s = '  ' + location + ':\n     '
        s = s + str(edges[location])

        print(s)

    if not start in edges.keys():
        print("Start location is not in the graph.")
    else:

        print('')
        print('-- States Visited ----------------')
        # program will need to show the search tree - prints the visited states while the function iterativeDFS is executing
        solution = iterativeDFS(start, goal, 1000, edges)
        print('')
        print('--  Solution for: ' + start +
              ' to ' + goal + '-------------------')
        # program will need to provide solution path or indicate failure.
        print(solution)
        print('')


# Execute the main program.
# main()


####################################################################################################################
############################################################################################################################################
clock = pygame.time.Clock() # This is used to track the time
clock.tick(60)
# Game loop
running = True
while running:
    clock.tick(60)
    # screen color
    screen.fill((255, 255, 255)) #white color on the screen
    # display image
    backgroungImage()#loading the image

    # display all edge
    takeEdgeDrawInput() # display the edges on the imagess

    # button display
    if(bState == True):# After the source and the des is specified
        StartButton()
        depthButton()
        depthButtonT()
        depthButtonText()

    if(sequence == -2):
        resultButton()

    if(sequence == -3):
        restartButton()
        FinalDepthText()

    # text display
    pathMessage()
    pathMessageSeq()

    # endPoint marker syambol draw
    name = "Github: Stavan Khisty"
    endpointPlot()
    makerFun()

    # startPoint marker syambol draw
    startPointPlot()

    for event in pygame.event.get():#get events from the queue

        # for quit

        if event.type == pygame.QUIT:
            running = False

        # for mouse click coordinates

        # sequence = 1 (start city not selected yet)
        if (event.type == pygame.MOUSEBUTTONDOWN) and (sequence == 1):

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()#(x, y) get the mouse cursor position
                print(pos[0],pos[1] )
                

                print("start city: " + startCity + "     End city: " + endCity)
                startCity = getCityFromClick(pos)#displaying from the mouse position
                # print(startCity)S
                print(pos)
                if(startCity != "notFound"):#if the start is found
                    print(startCity)
                    for i in cityPoint:
                        if(startCity == i[0]):
                            sx = i[1] - 13
                            sy = i[2] - 14
                            print("aaaaaa    " + str(sx) + "    " + str(sy))
                    print("seq: " + str(sequence))
                    sequence += 1
                    print("seq: " + str(sequence))
            continue

        # seqence = 2 (end city not selected yet, start city selected)
        if (event.type == pygame.MOUSEBUTTONDOWN) and (sequence == 2):
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                print(pos)

                print("start city: " + startCity + "     End city: " + endCity)
                endCity = getCityFromClick(pos)
                # print(endCity)
                # print(pos)
                if(endCity != "notFound"):
                    print(endCity)

                    for i in cityPoint:

                        if(endCity == i[0]):
                            ex = i[1] - 16
                            ey = i[2] - 32
                            print("aaaaaa    " + str(ex) + "    " + str(ey))
                    # print("seq: " + str(sequence))
                    sequence = 0
                    bState = True
                    print(bState)
                    # print("seq: " + str(sequence))
            print("start city: " + startCity + "     End city: " + endCity)
            continue

        # sequence = 0 (both cities selected, execute search operation 'main()' function)
        if (event.type == pygame.MOUSEBUTTONDOWN) and (sequence == 0):
            #########################################################################################################
            if pygame.mouse.get_pressed()[0]:#get the state of the mouse button
                pos = pygame.mouse.get_pos()
                print(str(pos[0]) + "    " + str(pos[1]) + "aaaaaaaa")
                if (bState == True) and (pos[0] > 675) and (pos[0] < 675+144) and (pos[1] > 15) and (pos[1] < 15+44):

                    main()
                    if printBool == False:

                        for i in tree:
                            print(i)

                        printBool = True
                    sequence = -1
                    # print(tree)
                    treeLength = len(tree)
                    print(treeLength)

        if (event.type == pygame.MOUSEBUTTONDOWN) and (sequence == -1):
            #########################################################################################################
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()

                if (pos[0] > 60) and (pos[0] < 60+170) and (pos[1] > 627) and (pos[1] < 627+42) and (depthBState == False):

                    depthBState = True#Set the depth state to true

        if (event.type == pygame.MOUSEBUTTONDOWN) and (sequence == -2):
            #########################################################################################################
            if pygame.mouse.get_pressed()[0]:

                pos = pygame.mouse.get_pos()
                print(str(pos[0]) + "   " + str(pos[1]))

                if (pos[0] > 610) and (pos[0] < 610+166) and (pos[1] > 627) and (pos[1] < 627+43):
                    print(resultState)
                    resultState = True

        # restart button state
        if (event.type == pygame.MOUSEBUTTONDOWN) and (sequence == -3):
            #########################################################################################################
            if pygame.mouse.get_pressed()[0]:

                pos = pygame.mouse.get_pos()
                print(str(pos[0]) + "   " + str(pos[1]))

                if (pos[0] > 371) and (pos[0] < 371+120) and (pos[1] > 663) and (pos[1] < 663+45):
                    ######################################################################################################################
                    # re initialize to original value (restart game)
                    
                    sequence = 1
                    currentTree = []
                    bState = False
                    depthBState = False
                    resultState = False
                    depthCountInt = 1
                    depthT = ""
                    tree = []
                    treeLength = 0
                    iteratorTree = 2
                    currentTree = []
                    printBool = False
                    finalPathPair = []
                    pathT = ""
                    sequence = 1
                    endCity = ""
                    startCity = ""
                    sx = -100
                    sy = -100
                    ex = -1
                    ey = -1
                    visitedPaths = ""
                    finalPath = []
                    countOfDepth = 0
                    tempVar = ""

                    #########################################################################################################
                    # out of event loop display edges
    if (sequence == -1):
        if iteratorTree == treeLength:
            depthT = "Current depth: " + str(depthCountInt)
            sequence = -2
        else:
            if (tree[iteratorTree][0] != "aaa"):
                time.sleep(drawSpeed)
                currentTree.append(tree[iteratorTree])
                iteratorTree += 1

            elif (tree[iteratorTree][0] == "aaa"):
                depthT = "Current depth: " + str(depthCountInt)

                if (depthBState == True):
                    depthCountInt += 1
                    currentTree.clear()
                    depthBState = False
                    iteratorTree += 1
                else:
                    print("enter")

        # print(tree[iteratorTree])

    # sequence = -2 (path is drawn show the final path generated )
    if(sequence == -2) and (resultState == True):

        pathT = "Path: "
        for c in finalPath:

            pathT += c + " -> "
        pathT = pathT[0:len(pathT)-4]
        finalDepthText = "Node found at Depth: " + str(depthCountInt)

        bState = False
        currentTree.clear()
        for i in range(0, len(finalPath)-1):
            currentTree.append([finalPath[i], finalPath[i+1]])
        sequence = -3

    pygame.display.update()


# game loop end
####################################################################################################################################
  