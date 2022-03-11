def find_max(list)
    max = 0
    for i in list:
        if i["Price"] > max:
            max = i["Price"]
    return max
    
def find_total(list):
    cost = 0
    for i in list:
        cost = cost + i["Price"]
    return cost

def find_avg(list):
    total= find_total(list): #using find_total function given above
    number_of_items=len(list)
    return total / number_of_items 


# Main Program
for i in range(len(orders)):
    print("Order ", i, "’s costliest iterm is ",find_max(orders[i]))
    print("The total cost of order ", i, " is ", find_total(orders[i]))
    print("The average cost of order ", i, " is ", find_avg(orders[i]))