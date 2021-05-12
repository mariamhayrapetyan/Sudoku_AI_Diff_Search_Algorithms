from Heuristics import *

#AC-3

def AC3(csp, q = None):

    if q == None:
        q = list(csp.binary_constraints)

    while q:
        (xi, xj) = q.pop(0)

        if Revise(csp, xi, xj):
            if len(csp.domains[xi]) == 0:
                return False

            for xk in csp.neighbors[xi]:
                if xk != xj:
                    q.append((xk, xi))
    return True


counter = 0
our_list_ac3 = []
def Revise(csp, xi, xj):
    global counter
    global our_list_ac3
    removed = False

    for val in csp.domains[xi]:
            if not any([not_equal(val, domain) for domain in csp.domains[xj]]):
                csp.domains[xi].remove(val)
                removed = True

    print((xi, xj), "Domain of " + str(xi) + ": " + str(csp.domains[xi]))

    counter += 1
    our_list_ac3.append(counter)
    return removed



#BACKTRACKING


count1 = 0
our_list1 = []
def Backtracking_Heuristicless(assignment, csp):
    global count1
    global our_list1
    if len(assignment) == len(csp.variables):
        return assignment

    var = select_unassigned_variables(assignment, csp)

    for value in order_domain_values(csp, var):

        if is_consistent(csp, assignment, var, value):

            assign(var, value, assignment)
            print(assignment)
            count1 += 1
            our_list1.append(count1)

            result = Backtracking_Heuristicless(assignment, csp)

            if result:
                return result

            unassign(var, assignment)
            print(assignment)
            count1 += 1
            our_list1.append(count1)

    return False



count12 = 0
our_list12 = []
def Backtracking_Heuristicless_Forward_Checking(assignment, csp):
    global count12
    global our_list12
    if len(assignment) == len(csp.variables):
        return assignment

    var = select_unassigned_variables(assignment, csp)

    for value in order_domain_values(csp, var):

        if is_consistent(csp, assignment, var, value):

            assign_with_forward_check(csp, var, value, assignment)
            print(assignment)
            count12 += 1
            our_list12.append(count12)

            result = Backtracking_Heuristicless_Forward_Checking(assignment, csp)

            if result:
                return result

            unassign_with_forward_check(csp, var, assignment)
            print(assignment)
            count12 += 1
            our_list12.append(count12)

    return False


count2 = 0
our_list2 = []
def Backtracking_MRV(assignment, csp):
    global count2
    global our_list2
    if len(assignment) == len(csp.variables):
        return assignment

    var = MRV(assignment, csp)

    for value in order_domain_values(csp, var):

        if is_consistent(csp, assignment, var, value):

            assign(var, value, assignment)
            print(assignment)
            count2 += 1
            our_list2.append(count2)

            result = Backtracking_MRV(assignment, csp)

            if result:
                return result

            unassign(var, assignment)
            print(assignment)
            count2 += 1
            our_list2.append(count2)

    return False


count22 = 0
our_list22 = []
def Backtracking_MRV_Forward_Checking(assignment, csp):
    global count22
    global our_list22
    if len(assignment) == len(csp.variables):
        return assignment

    var = MRV(assignment, csp)

    for value in order_domain_values(csp, var):

        if is_consistent(csp, assignment, var, value):

            assign_with_forward_check(csp, var, value, assignment)
            print(assignment)
            count22 += 1
            our_list22.append(count22)

            result = Backtracking_MRV_Forward_Checking(assignment, csp)

            if result:
                return result

            unassign_with_forward_check(csp, var, assignment)
            print(assignment)
            count22 += 1
            our_list22.append(count22)

    return False


count3 = 0
our_list3 = []
def Backtracking_LCS(assignment, csp):
    global count3
    global our_list3
    if len(assignment) == len(csp.variables):
        return assignment

    var = select_unassigned_variables(assignment, csp)

    for value in LCS(csp, var):

        if is_consistent(csp, assignment, var, value):

            assign(var, value, assignment)
            print(assignment)
            count3 += 1
            our_list3.append(count3)

            result = Backtracking_LCS(assignment, csp)

            if result:
                return result

            unassign(var, assignment)
            print(assignment)
            count3 += 1
            our_list3.append(count3)

    return False


count32 = 0
our_list32 = []
def Backtracking_LCS_Forward_Checking(assignment, csp):
    global count32
    global our_list32
    if len(assignment) == len(csp.variables):
        return assignment

    var = select_unassigned_variables(assignment, csp)

    for value in LCS(csp, var):

        if is_consistent(csp, assignment, var, value):

            assign_with_forward_check(csp, var, value, assignment)
            print(assignment)
            count32 += 1
            our_list32.append(count32)

            result = Backtracking_LCS_Forward_Checking(assignment, csp)

            if result:
                return result

            unassign_with_forward_check(csp, var, assignment)
            print(assignment)
            count32 += 1
            our_list32.append(count32)

    return False


count4 = 0
our_list4 = []
def Backtracking_MRV_LCS(assignment, csp):
    global count4
    global our_list4
    if len(assignment) == len(csp.variables):
        return assignment

    var = MRV(assignment, csp)

    for value in LCS(csp, var):
        if is_consistent(csp, assignment, var, value):
            assign(var, value, assignment)
            print(assignment)
            count4 += 1
            our_list4.append(count4)

            result = Backtracking_MRV_LCS(assignment, csp)
            if result:
                return result

            unassign(var, assignment)
            print(assignment)
            count4 += 1
            our_list4.append(count4)

    return False


count42 = 0
our_list42 = []
def Backtracking_MRV_LCS_Forward_Checking(assignment, csp):
    global count42
    global our_list42
    if len(assignment) == len(csp.variables):
        return assignment

    var = MRV(assignment, csp)

    for value in LCS(csp, var):
        if is_consistent(csp, assignment, var, value):
            assign_with_forward_check(csp, var, value, assignment)
            print(assignment)
            count42 += 1
            our_list42.append(count42)

            result = Backtracking_MRV_LCS_Forward_Checking(assignment, csp)
            if result:
                return result

            unassign_with_forward_check(csp, var, assignment)
            print(assignment)
            count42 += 1
            our_list42.append(count42)

    return False





