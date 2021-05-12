from Generator import *
import time
from Algorithms import *

def AC3_demo():
    level = str(input("Choose the level(Easy, Medium, Hard):"))
    g = SudokuGenerator(level).generate_grid()
    g1 = [''.join(str(e)) for ele in g for e in ele]
    g2 = "".join(g1)
    sudoku = Sudoku(g2)
    print("\nAC-3 algorithm executing...\n")
    print("Initial configuration:\n")
    print(sudoku)
    start_time = time.time()
    AC3_result = AC3(sudoku)
    if AC3_result:
        if sudoku.isFinished():
            print("\nSolution:\n")
            print(sudoku)
        else:
            print("\nFailed to solve with AC-3 only! Assigned steps to 0.\n")
            our_list_ac3.append(0)
            print(sudoku)
    else:
        print("\nThere is an inconsistency!\n")
    end_time = time.time()
    print("Duration: %s seconds" % (end_time - start_time))
    print("Steps: " + str(our_list_ac3[-1]))


def Backtracking_demo():
    level = str(input("Choose the level(Easy, Medium, Hard):"))
    if level not in ["Easy", "Medium", "Hard"]:
        print("CHOOSE A VIABLE OPTION FOR LEVEL!")
    a = str(input("Choose the heuristic(no, LCS, MRV, both):"))
    b = str(input("With forward checking inference?(no, yes):"))
    g = SudokuGenerator(level).generate_grid()
    g1 = [''.join(str(e)) for ele in g for e in ele]
    g2 = "".join(g1)
    sudoku = Sudoku(g2)
    print("\nBacktracking algorithm with " + a + " heuristic executing...\n")
    print("Initial configuration:\n")
    print(sudoku)

    assignment = {}
    for var in sudoku.variables:
        if len(sudoku.domains[var]) == 1:
            assignment[var] = sudoku.domains[var][0]

    start_time = time.time()
    if a == "no" and b == "no":
        assignment = Backtracking_Heuristicless(assignment, sudoku)
        for var in sudoku.domains:
            sudoku.domains[var] = assignment[var] if len(var) > 1 else sudoku.domains[var]
        end_time = time.time()

        if assignment:
            print("\nSolution:\n")
            print(sudoku)
        else:
            print("No solution exists!")

        print("Duration: %s seconds" % (end_time - start_time))
        print("Steps: " + str(our_list1[-1]))

    elif a == "no" and b == "yes":
        assignment = Backtracking_Heuristicless_Forward_Checking(assignment, sudoku)
        for var in sudoku.domains:
            sudoku.domains[var] = assignment[var] if len(var) > 1 else sudoku.domains[var]
        end_time = time.time()

        if assignment:
            print("\nSolution:\n")
            print(sudoku)
        else:
            print("No solution exists!")

        print("Duration: %s seconds" % (end_time - start_time))
        print("Steps: " + str(our_list12[-1]))

    elif a == "LCS" and b == "no":
        assignment = Backtracking_LCS(assignment, sudoku)
        for var in sudoku.domains:
            sudoku.domains[var] = assignment[var] if len(var) > 1 else sudoku.domains[var]
        end_time = time.time()

        if assignment:
            print("\nSolution:\n")
            print(sudoku)
        else:
            print("No solution exists!")

        print("Duration: %s seconds" % (end_time - start_time))
        print("Steps: " + str(our_list3[-1]))

    elif a == "LCS" and b == "yes":
        assignment = Backtracking_LCS_Forward_Checking(assignment, sudoku)
        for var in sudoku.domains:
            sudoku.domains[var] = assignment[var] if len(var) > 1 else sudoku.domains[var]
        end_time = time.time()

        if assignment:
            print("\nSolution:\n")
            print(sudoku)
        else:
            print("No solution exists!")

        print("Duration: %s seconds" % (end_time - start_time))
        print("Steps: " + str(our_list32[-1]))

    elif a == "MRV" and b == "no":
        assignment = Backtracking_MRV(assignment, sudoku)
        for var in sudoku.domains:
            sudoku.domains[var] = assignment[var] if len(var) > 1 else sudoku.domains[var]
        end_time = time.time()

        if assignment:
            print("\nSolution:\n")
            print(sudoku)
        else:
            print("No solution exists!")

        print("Duration: %s seconds" % (end_time - start_time))
        print("Steps: " + str(our_list2[-1]))

    elif a == "MRV" and b == "yes":
        assignment = Backtracking_MRV_Forward_Checking(assignment, sudoku)
        for var in sudoku.domains:
            sudoku.domains[var] = assignment[var] if len(var) > 1 else sudoku.domains[var]
        end_time = time.time()

        if assignment:
            print("\nSolution:\n")
            print(sudoku)
        else:
            print("No solution exists!")

        print("Duration: %s seconds" % (end_time - start_time))
        print("Steps: " + str(our_list22[-1]))

    elif a == "both" and b == "no":
        assignment = Backtracking_MRV_LCS(assignment, sudoku)
        for var in sudoku.domains:
            sudoku.domains[var] = assignment[var] if len(var) > 1 else sudoku.domains[var]
        end_time = time.time()

        if assignment:
            print("\nSolution:\n")
            print(sudoku)
        else:
            print("No solution exists!")

        print("Duration: %s seconds" % (end_time - start_time))
        print("Steps: " + str(our_list4[-1]))

    elif a == "both" and b == "yes":
        assignment = Backtracking_MRV_LCS_Forward_Checking(assignment, sudoku)
        for var in sudoku.domains:
            sudoku.domains[var] = assignment[var] if len(var) > 1 else sudoku.domains[var]
        end_time = time.time()

        if assignment:
            print("\nSolution:\n")
            print(sudoku)
        else:
            print("No solution exists!")

        print("Duration: %s seconds" % (end_time - start_time))
        print("Steps: " + str(our_list42[-1]))

    else:
        print("CHOOSE A VIABLE OPTION FOR HEURISTIC!")


def Statistics_AC3_demo():
    level = str(input("Choose the level(Easy, Medium, Hard):"))
    duration_sum = 0
    all_steps = []
    all_durations = []

    for i in range(0, 100):
        g = SudokuGenerator(level).generate_grid()
        g1 = [''.join(str(e)) for ele in g for e in ele]
        g2 = "".join(g1)
        sudoku = Sudoku(g2)
        start_time = time.time()
        AC3(sudoku)
        end_time = time.time()
        duration = end_time - start_time
        all_steps.append(our_list_ac3[-1])
        duration_sum += duration
        all_durations.append(duration)

    average_steps = all_steps[-1]/100
    average_duration = duration_sum/100
    print("Average steps for AC-3 with difficulty level " + level + ": " + str(average_steps))
    print("Average duration for AC-3 with difficulty level " + level + ": " + str(average_duration))


def Statistics_Backtracking_demo():
    level = str(input("Choose the level(Easy, Medium, Hard):"))
    if level not in ["Easy", "Medium", "Hard"]:
        print("CHOOSE A VIABLE OPTION FOR LEVEL!")
    a = str(input("Choose the heuristic(no, LCS, MRV, both):"))
    b = str(input("With forward checking inference?(no, yes):"))
    duration_sum = 0
    all_steps = []
    all_durations = []

    for i in range(0, 100):
        g = SudokuGenerator(level).generate_grid()
        g1 = [''.join(str(e)) for ele in g for e in ele]
        g2 = "".join(g1)
        sudoku = Sudoku(g2)

        assignment = {}
        for var in sudoku.variables:
            if len(sudoku.domains[var]) == 1:
                assignment[var] = sudoku.domains[var][0]

        start_time = time.time()
        if a == "no" and b == "no":
            assignment = Backtracking_Heuristicless(assignment, sudoku)
            for var in sudoku.domains:
                sudoku.domains[var] = assignment[var] if len(var) > 1 else sudoku.domains[var]
            end_time = time.time()

            duration = end_time - start_time
            all_steps.append(our_list1[-1])
            duration_sum += duration
            all_durations.append(duration)

        elif a == "no" and b == "yes":
            assignment = Backtracking_Heuristicless_Forward_Checking(assignment, sudoku)
            for var in sudoku.domains:
                sudoku.domains[var] = assignment[var] if len(var) > 1 else sudoku.domains[var]
            end_time = time.time()

            duration = end_time - start_time
            all_steps.append(our_list12[-1])
            duration_sum += duration
            all_durations.append(duration)

        elif a == "LCS" and b == "no":
            assignment = Backtracking_LCS(assignment, sudoku)
            for var in sudoku.domains:
                sudoku.domains[var] = assignment[var] if len(var) > 1 else sudoku.domains[var]
            end_time = time.time()

            duration = end_time - start_time
            all_steps.append(our_list3[-1])
            duration_sum += duration
            all_durations.append(duration)

        elif a == "LCS" and b == "yes":
            assignment = Backtracking_LCS_Forward_Checking(assignment, sudoku)
            for var in sudoku.domains:
                sudoku.domains[var] = assignment[var] if len(var) > 1 else sudoku.domains[var]
            end_time = time.time()

            duration = end_time - start_time
            all_steps.append(our_list32[-1])
            duration_sum += duration
            all_durations.append(duration)

        elif a == "MRV" and b == "no":
            assignment = Backtracking_MRV(assignment, sudoku)
            for var in sudoku.domains:
                sudoku.domains[var] = assignment[var] if len(var) > 1 else sudoku.domains[var]
            end_time = time.time()

            duration = end_time - start_time
            all_steps.append(our_list2[-1])
            duration_sum += duration
            all_durations.append(duration)

        elif a == "MRV" and b == "yes":
            assignment = Backtracking_MRV_Forward_Checking(assignment, sudoku)
            for var in sudoku.domains:
                sudoku.domains[var] = assignment[var] if len(var) > 1 else sudoku.domains[var]
            end_time = time.time()

            duration = end_time - start_time
            all_steps.append(our_list22[-1])
            duration_sum += duration
            all_durations.append(duration)

        elif a == "both" and b == "no":
            assignment = Backtracking_MRV_LCS(assignment, sudoku)
            for var in sudoku.domains:
                sudoku.domains[var] = assignment[var] if len(var) > 1 else sudoku.domains[var]
            end_time = time.time()

            duration = end_time - start_time
            all_steps.append(our_list4[-1])
            duration_sum += duration
            all_durations.append(duration)

        elif a == "both" and b == "yes":
            assignment = Backtracking_MRV_LCS_Forward_Checking(assignment, sudoku)
            for var in sudoku.domains:
                sudoku.domains[var] = assignment[var] if len(var) > 1 else sudoku.domains[var]
            end_time = time.time()

            duration = end_time - start_time
            all_steps.append(our_list42[-1])
            duration_sum += duration
            all_durations.append(duration)

    average_steps = all_steps[-1] / 100
    average_duration = duration_sum / 100
    print("Average steps for Backtracking with difficulty level " + level + ", " + a + " heuristic, and inference(" + b + "): " + str(average_steps))
    print("Average duration for Backtracking with difficulty level " + level + ", " + a + " heuristic, and inference(" + b + "): " + str(average_duration))


if __name__ == "__main__":
    #AC3_demo()
    Backtracking_demo()