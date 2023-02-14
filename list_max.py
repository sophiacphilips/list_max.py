#Name: Sophia Philips
#GitHub Username: sophiacphilips
#Date: 02/12/2023
#This code is designed to take a list of number and return the maximum value without using recursion or the built-in max function



def list_max(my_list):
    """
    This method uses recursion by taking values with list_max(my_list) and returns the max value
    """
    if len(my_list) == 1: #sets base case that list contains at least one element
        return my_list[0]
    else:
        find_max = list_max(my_list[1:]) #moves through list starting with first integer, and will finish at base case
        if my_list[0] > find_max: #compares value of integer, to next in list
            find_max = my_list[0]
        return find_max




