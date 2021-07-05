import sys
from Stack import Stack
import os

#TODO

#Reads the candidates from the Candidates.txt file
#Candidates must be written in the following format
#"[number of candidate on the list]. [name of candidate]
#example "1. Hannah Strickland"
def getCandidates():
    lst = []
    file = open(os.path.join(sys.path[0], "Candidates.txt"), "r")
    for x in file:
        if x in lst:
            print("Duplicate candidate detected. Exiting...")
            return []
        lst.append(x[x.index('.')+2:-1])
    return lst

#Reads the votes from the Votes.txt file
#Votes must be written in the following format
#"[number of voter]. [number of candidate choice1],[number of candidate choice2],[number of candidate choice3],[number of candidate choice4],...
#1. 10,5,2,4,7,6,1,9,8,3
def getVotes(numCandidates):
    file = open(os.path.join(sys.path[0], "Votes.txt"), "r")
    votes = []
    for x in file:
        vote = Stack()

        currentVote = ""
        for y in x[x.index('.')+2:][::-1].strip('\n'):
            if y == ',':
                vote.push(currentVote[::-1])
                currentVote = ""
            else:
                currentVote += y
        vote.push(currentVote[::-1])
        votes.append(vote)

    return votes

#Goes through all the loser candidates and distributes their votes to the next candidate they ranked on their voting card
def redistribute(tally, candidates, losers):
    tallyCopy = list(tally.items()).copy()
    for x in tallyCopy:
        #a candidate who lost is found
        if x[0] in losers:
            #iterate through all the candidates voter cards
            for y in x[1]:
                #removes the candidate at the top of their list and sees if the next candidate is still in contention and can be moved to their list
                while candidates[int(y.peek())-1] not in tally.keys() or candidates[int(y.peek())-1] in losers:
                    y.pop()
                #card is destroyed if they have no more candidates in contention
                if not y.empty:
                    tally[candidates[int(y.peek())-1]].append(x[1])
            del tally[x[0]]
    return tally

#Gets the candidate with the largest number of votes constructed kinda similar to getLoser()
def getWinner(tallies):
    max = len(list(tallies.values())[0])
    name = list(tallies.keys())[0]
    for x in tallies.items():
        if len(x[1]) > max:
            max = len(x[1])
            name = x[0]
    return name

#returns a list of all the candidates with the lowest amount of votes
def getLoser(tallies):
    #records the lowest number of votes a candidate has gotten so far
    min = len(list(tallies.values())[0])

    #initialize the list that will be returned with all the names of losers
    losers = [list(tallies.keys())[0]]

    #min and losers initialized with the values of the first candidate and their # of votes just so its not empty

    for x in list(tallies.items())[1:]:
        #If a new minimum number of votes is found, the losers list is emptied and the new loser candidate is added
        if len(x[1]) < min:
            min = len(x[1])
            losers = [x[0]]
        #If someone else with the same number of lowest votes is found, they are also added to the list.
        elif len(x[1]) == min:
            losers.append(x[0])
    return losers

def PrintSimulation(candidates, votes):
    #Keeps track of what round the program is on
    RoundCount = 1

    #A dictionary that defines each candidates name by their votes
    #Example of data organization
    #[Candidate name: [[voter card 1] [voter card 2] [voter card 3] [voter card 4]]
    #Each voter card is a stack
    tally = {}

    #initializes the list
    for x in candidates:
        tally[x] = []

    #Round 1
    print("Round: " + str(RoundCount) + "\n---------")

    #Assign all vote cards to each candidate
    for x in votes:
        tally[candidates[int(x.peek())-1]].append(x)

    # Check to see if someone got +50% of the vote in round 1
    lead = getWinner(tally)
    if len(tally[lead]) > len(tally) / 2:
        # if someone did get +50%, the rest are removed from contention and the program goes directly to printing the winner
        for x in tally.items():
            if x[0] != lead:
                del tally[x[0]]
    else:
        #Finds the loser(s) of the round and removes them from contention
        losers = getLoser(tally)
        print("\nLoser of Round " + str(RoundCount) + ": " + str(losers))
        if len(losers) == len(tally):
            print("There is a tie between the remaining candidates: " + str(losers))
            return
        else:
            tally = redistribute(tally,candidates, losers)
            RoundCount += 1

    #The rest of the rounds after round 1
    while len(tally) > 1:
        print("Round: " + str(RoundCount) + "\n---------\n" + str(tally))

        losers = getLoser(tally)
        print("\nLoser of Round " + str(RoundCount) + ": " + str(losers))

        #If all the candidates got the same number of votes, the program ends in a tie
        if len(losers) == len(tally):
            print("There is a tie between the remaining candidates: " + str(losers))
            return
        else:
            tally = redistribute(tally, candidates, losers)
            RoundCount += 1

    if (len(tally) == 1):
        print("\n\nWinner: " + list(tally.keys())[0])
    else:
        message = "\n\nWinners: "
        for x in tally.keys():
            message += x + ", "
        print(message[:-2])

#MAIN PROGRAM
mode = -1
while mode != '1' or mode != '2':
    print("[1]Input Votes from File\n[2]Exit")
    mode = input("Choose what mode to use")
    if mode != '1' and mode != '2':
        print("Please only type '1' or '2'. Other inputs are not accepted")
    if mode == '1':
        candidates = getCandidates()
        votes = getVotes(len(candidates))
        if candidates == [] or votes == []:
            mode == '2'
        else:
            PrintSimulation(candidates, votes)
    if mode == '2':
        print("Program Ended")
        break

#Old approach to the algorithm. No longer works with the changed getLoser(0) method
#def PrintSimulation(candidates,votes):
#     RoundCount = 1
#     tally = {}
#
#     for x in candidates:
#         tally[x] = 0
#
#     #Runs each round of elemination till one remains
#     while len(tally) != 1:
#         tally = tally.fromkeys(tally,0)
#         print("Round: " + str(RoundCount) + "\n---------")
#         #Goes through each voter
#         for x in votes:
#             topVote = candidates[int(x.peek())-1]
#             #if the candidate at the top of stack is not in contention, they are removed
#             while topVote not in tally.keys():
#                 x.pop()
#                 topVote = candidates[int(x.peek())-1]
#             #if the voter's card is empty then they are skipper
#             if x.empty():
#                 continue
#             #Add candidate vote to tally
#             tally[topVote] += 1
#         print("\n" + str(tally))
#
#         #Check to see if someone got +50% of the vote in round 1
#         if RoundCount == 1:
#             max = list(tally.values())[0]
#             name = list(tally.keys())[0]
#             for x in tally.items():
#                 if x[1] > max:
#                     max = x[1]
#                     name = x[0]
#             if max > len(tally)/2:
#                 for x in tally.items():
#                     if x[0] != name:
#                         del tally[x[0]]
#                         break
#         losers = getLoser(tally)
#         print("\nLoser of Round " + str(RoundCount) + ": " + str(losers))
#         if len(losers) == len(tally):
#             print("There is a tie between the remaining candidates: " + str(losers))
#             break
#         else:
#             for y in losers:
#                 del tally[y]
#             RoundCount += 1
#     if(len(tally) == 1):
#         print("\n\nWinner: " + list(tally.keys())[0])
#     else:
#         message = "\n\nWinners: "
#         for x in tally.keys():
#             message += x + ", "
#         print(message[:-2])