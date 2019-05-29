#!/usr/bin/python3

# Given the list of IDs, which contains many duplicate integers and one unique integer, find the unique integer. 

#using for 0(n) and 0(n) for space
def find_unique_integer_id(delivery_id_confirmations):
    lands = [True]*len(delivery_id_confirmations)

    for b in delivery_id_confirmations:
        lands[b]= not lands[b]

    for i in range(len(delivery_id_confirmations)):
        if not lands[i]:
            return i;

# using XOR =>  O(n) and O(1) for space
def find_unique_delivery_id(delivery_id_confirmations):
    unique_delivery_id = 0

    for delivery_id in delivery_id_confirmations:
        unique_delivery_id ^= delivery_id

    return unique_delivery_id

print(find_unique_delivery_id([0, 1, 2,3,3,1, 0]))

