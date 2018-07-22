import math

def pythagorus(x1, y1, x2, y2):
           xs = x1 + x2
           ys = y1 + y2
           return math.sqrt(pow(xs,2) + pow(ys,2))

def findworld(x):
    znext = 'z' # dummy value for next
    nextlist =[]
    c=0

    for c in range(len(world)): # pairs of links from (f) to destination (t)
        f = world[c][0]
        t = world[c][1]
        if(x == world[c][0]) : nextlist.append(world[c][1])
    return nextlist;

world = [['a', 'b'],['b', 'c'],['a', 'd'],
         ['d', 'e'], ['e', 'f'], ['f', 'g'], ['g', 'h'], ['h', 'i'],
         ['i', 'k'], ['k', 'l'], ['l', 'm'], ['k', 'n'],
         ['n', 'r'],['r', 's'],['s', 't'],['t', 'u'],['u', 'v'],['w', 'x'],['x', 'q'], ['q', 'p'],['p', 'o'],['r', 'A'],['B', 'x'],
         ['A', 'z'],['z', 'y'],['A', 'C'],['C', 'D'],['D', 'E'],['E', 'H'],['C', 'G'],['L', 'F'],['F', 'B'],
         ['G', 'M'],['H', 'N'],['N', 'P'],['H', 'I'],['I', 'J'],['J', 'K'],['K', 'L'],
         ['M', 'O'], ['P', 'Q'], ['Q', 'R'],['P', 'T'],['R', 'V'],['Q', 'U'],
         ['O', 'S'],['T', 'U'],['U', 'V'],['T', 'X'],['V', 'Y'],
         ['S', 'W'],
         ['Y', 'Z']]

coordinates = [['a',0,11], ['b',1,11], ['c',2,11],
               ['d',0,10], ['e',1,10], ['f',2,10], ['g',3,10], ['h',4,10],['i',5,10],
               ['j',0,9], ['k',5,9], ['l',6,9], ['m',7,9],
               ['n',5,8], ['o',9,8],['p',10,8],['q',11,8],
               ['r',5,7], ['s',6,7], ['t',7,7], ['u',8,7], ['v',9,7],['w',10,7],['x',11,7],
               ['y',3,6], ['z',4,6],['A',5,6], ['B',11,6],
               ['C',5,5], ['D',6,5], ['E',7,5], ['F',11,5],
               ['G',5,4], ['H',7,4], ['I',8,4], ['J',9,4],['K',10,4],['L',11,4],
               ['M',5,3], ['N',7,3],
               ['O',5,2], ['P',7,2], ['Q',8,2], ['R',9,2],
               ['S',5,1], ['T',7,1], ['U',8,1], ['V',9,1],
               ['W',5,0], ['X',7,0], ['Y',9,0], ['Z',10,0]]

End = raw_input('Enter the target location between b - z lower case or A - Z upper case : ')
Location = raw_input('Enter a location where you would like to view posible moves from: a - Z lower case of A - Z upper case.')
initial ='a' # initial starting rooom
goal = End # final destination
route = [] # keep rooms visted as a route
queue = []
print ("Possible moves from location: " + Location + " are: " + str(findworld(Location)))
queue.append(initial) # the starting (initial) room
print("Robot at: ", initial)
print("Goal is: ", goal)
compter = 0
# the loop explores our
while queue != None: # if queue then stop
    headq = queue[0][0] # pull first item in queue into head
    route.append(headq) # add each locaton (headq) to route
    tail = queue[1:len(queue)] # get tail of queue after first item removed
    nextlink = findworld(headq[0][0]) # returns the next linked room
    newqueue = [] # make a new queue including the next link to follow + tail
    newqueue += nextlink
    newqueue += tail
    queue = newqueue
    
    print route

    if(headq == goal):
        extractedInitial = "start"
        extractedGoal = "end"

        for i in range(len(coordinates)):
            if initial == coordinates[i][0]:
                print "initial found"
                extractedInitial = coordinates[i]
                print "initial", extractedInitial


            if goal == coordinates[i][0]:
                print "goal found"
                extractedGoal = coordinates[i]
                print "goal", extractedGoal

                print pythagorus(extractedInitial[1], extractedInitial[2], extractedGoal[1], extractedGoal[2])

        break
