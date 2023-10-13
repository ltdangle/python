# 3. Simulate an election for two candidates. Program should take amount of regions and rating for 1st candidate in each region (in percentage). Program should run election in every region. In every region, program should ask 10 000 voters. Candidate count as a winner if he gains more than 50% of all votes. Program should print the result of the election for each region and the winner
#
#     Example:
#
#     Enter number of regions: 2 
#
#     Enter rating for 1st candidate in 1 region: 34
#     Enter rating for 1st candidate in 2 region: 56
#
#     Region 1: 3456 votes for 1st candidate, 6544 votes for 2nd candidate
#
#     Region 2: 5623 votes for 1st candidate, 4356 votes for 2nd candidate
#
#     Result: 2nd candidate won with 10900 votes and 54.5% of all votes
#
# In your solution your should use input function to get the value from user. After that, use random function to generate votes for your candidate. After that calculate these votes and print the result. In your solution you should implement these functions:
#
# ```python
# def receive_input():
#     pass
#
# def simulate_region_election():
#         pass
#
# def simulate_election():
#     pass
#
# def calculate_result():
#     pass
#
# def announce_result():
#     pass
#
# input_data = receive_input()
# election_result = simulate_election(input_data)
# result = calculate_result(election_result)
# announce_result(result)
# ```

import random

def receive_input():
    regions = int(input("Enter number of regions: "))
    ratings = []
    for i in range(regions):
        rating = int(input(f"Enter rating for 1st candidate in {i+1} region: "))
        ratings.append(rating)
    return ratings

def simulate_region_election(rating):
    votes_1st_candidate = 0
    votes_2nd_candidate = 0
    for i in range(10000):
        if random.randint(0, 100) < rating:
            votes_1st_candidate += 1
        else:
            votes_2nd_candidate += 1
    return votes_1st_candidate, votes_2nd_candidate

def simulate_election(ratings):
    election_result = []
    for rating in ratings:
        votes_1st_candidate, votes_2nd_candidate = simulate_region_election(rating)
        election_result.append((votes_1st_candidate, votes_2nd_candidate))
    return election_result

def calculate_result(election_result):
    total_votes_1st_candidate = 0
    total_votes_2nd_candidate = 0
    for votes_1st_candidate, votes_2nd_candidate in election_result:
        total_votes_1st_candidate += votes_1st_candidate
        total_votes_2nd_candidate += votes_2nd_candidate
    total_votes = total_votes_1st_candidate + total_votes_2nd_candidate
    percent_1st_candidate = total_votes_1st_candidate / total_votes * 100
    percent_2nd_candidate = total_votes_2nd_candidate / total_votes * 100
    if percent_1st_candidate > 50:
        winner = '1st candidate'
    else:
        winner = '2nd candidate'
    return total_votes_1st_candidate, total_votes_2nd_candidate, percent_1st_candidate, percent_2nd_candidate, winner

def announce_result(result):
    total_votes_1st_candidate, total_votes_2nd_candidate, percent_1st_candidate, percent_2nd_candidate, winner = result
    print(f"Result: {winner} won with {total_votes_2nd_candidate} votes and {percent_2nd_candidate:.1f}% of all votes")

input_data = receive_input()
election_result = simulate_election(input_data)
for i, (votes_1st_candidate, votes_2nd_candidate) in enumerate(election_result):
    print(f"Region {i+1}: {votes_1st_candidate} votes for 1st candidate, {votes_2nd_candidate} votes for 2nd candidate")
result = calculate_result(election_result)
announce_result(result)
