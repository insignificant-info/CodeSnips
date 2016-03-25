def  friendCircles( friends):
    chain = []
    for test_person, test_person_friends in enumerate(friends):
        if test_person == 0:
            #Case: This is the first iteration
            #Add all of the first person's friends to a list and append that list to the chain
            chain.append(friendCount(test_person_friends))
        else:
            friend_match_list=[]
            for identified_friend_number, identified_friend_list in enumerate(chain):
                if identified_friend_list == -1:
                    #Case: This person's is part of a friend circle represented earlier in the chain
                    #Just continue
                    continue
                if test_person in identified_friend_list:
                    #Case: Person has been found in a friend list
                    #Append that friend to the friend_match_list
                    friend_match_list.append(identified_friend_number)
            if len(friend_match_list) == 0:
                #Case: This person is not part of any previously found chain
                #Create a new chain
                chain.append(friendCount(test_person_friends))
            else:
                #Case: This person is part of one or more previously found chains
                #Add their chain, then check the number of chains
                chain.append(friendCount(test_person_friends))
                if len(friend_match_list) > 1:
                    #Case: This person is part of multiple isolated friend chains
                    #Consolidate to one chain. Mark this person and the owners of other identified isolated chains
                    #as -1 to indicate that they are already included in another chain
                    first_friend_index = friend_match_list[0]
                    for i,chain_number in enumerate(friend_match_list):
                        if i == 0:
                            #Case: This person is the first friend found, all other friend lists will be collapsed
                            #to this persons list in the chain
                            #Simply continue, everything will be added to this persons list chain in later iterations
                            continue
                        else:
                            #Case: Not the first person in the list
                            #This person's chain should be collapsed to the first person in the list's chain and 
                            #their chain set to -1
                            #Note: I'm not worried about duplicates appearing in chains
                            chain[first_friend_index].extend(chain[chain_number])
                            chain[chain_number] = -1
                else:
                    #Case: len(friend_match_list) = 1
                    #Append this persons list to the first_friend's list and set this person to -1
                    chain[friend_match_list[0]].extend(chain[test_person])
                chain[test_person] = -1
    #Find the number of lists in chain, these are the friend circles                
    circle_count = sum(1 for x in chain if isinstance(x, list))
    return circle_count

def friendCount(friends_to_test):
    friend_list = []
    for friend_number,friend_status in enumerate(friends_to_test):
        if friend_status == 'Y':
            friend_list.append(friend_number)
    return friend_list

friends = [['Y','N','N','Y'],['N','Y','Y','Y'],['N','Y','Y','N'],['Y','Y','N','Y']]
print(friendCircles( friends))