# Author: Dennis Lam
# GitHub username: dennislam4
# Date: 7/11/2022
# Description: A function that returns the statistical median from a parameter that represents a list of numbers.

def find_median(num):
    """Returns the statistical median of numbers given."""
    ordered_list = sorted(num)
    list_length = len(num)
    index = (list_length - 1) // 2
   
    if len(num) % 2 == 1:
        return(ordered_list[index])
    else:
        return (ordered_list[index] + ordered_list[index + 1]) / 2.0

