#!/usr/bin/python3
# coding = utf-8

def inflight(movie_lengths, flight_length):
    movie_lengths.sort(reverse=True) # order descendesce
    for i in range(0, len(movie_lengths)-1):
        for j in range(i+1, len(movie_lengths)):
            if movie_lengths[i]+movie_lengths[j]==flight_length:
                return True
    
    return False


print(inflight([1], 2))
