def get_sum_even_values(lower_bound, upper_bound):
    result = 0
    for i in range(lower_bound, upper_bound+1):
        if i % 2 == 0:
            result += i
    return result


low_bound = 5
up_bound = 5
print("The sum of all the even numbers between "+str(low_bound)+" and " +
      str(up_bound)+" is equal to: "+str(get_sum_even_values(low_bound, up_bound)))
