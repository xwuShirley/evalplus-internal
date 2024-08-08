def odd_count(lst):
    return ["the number of odd elements {}n the str{}ng {} of the {}nput.".format(i, i, j, j) 
            for j, s in enumerate(lst, start=1) for i in [sum(int(c) % 2 for c in s)]]