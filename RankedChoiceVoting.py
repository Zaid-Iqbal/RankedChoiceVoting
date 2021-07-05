import sys
from Stack import Stack
import os

#TODO

def getCandidates():
    lst = []
    file = open(os.path.join(sys.path[0], "Candidates.txt"), "r")
    for x in file:
        if x in lst:
            print("Duplicate candidate detected. Exiting...")
            return []
        lst.append(x[x.index('.')+2:-1])
    return lst

def getVotes(numCandidates):
    file = open(os.path.join(sys.path[0], "Votes.txt"), "r")
    votes = []
    for x in file:
        vote = Stack()

        if x.count(',') != numCandidates - 1:
            print("Voter #" + str(len(votes)+1) + "does not have exactly " + str(numCandidates) + "Votes. Exiting...")
            return[]

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

def PrintSimulation(candidates, votes):
    RoundCount = 1
    tally = {}

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
        # if someone did get +50%, the rest are removed from contention
        for x in tally.items():
            if x[0] != lead:
                del tally[x[0]]
    else:
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

def redistribute(tally, candidates, losers):
    tallyCopy = list(tally.items()).copy()
    for x in tallyCopy:
        if x[0] in losers:
            for y in x[1]:
                while candidates[int(y.peek())-1] not in tally.keys() or candidates[int(y.peek())-1] in losers:
                    y.pop()
                tally[candidates[int(y.peek())-1]].append(x[1])
            del tally[x[0]]
    return tally

def getWinner(tallies):
    max = len(list(tallies.values())[0])
    name = list(tallies.keys())[0]
    for x in tallies.items():
        if len(x[1]) > max:
            max = len(x[1])
            name = x[0]
    return name

def getLoser(tallies):
    min = len(list(tallies.values())[0])
    name = list(tallies.keys())[0]
    losers = [name]
    for x in list(tallies.items())[1:]:
        if len(x[1]) < min:
            min = len(x[1])
            name = x[0]
            losers = [name]
        elif len(x[1]) == min:
            name = x[0]
            losers.append(name)
    return losers



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