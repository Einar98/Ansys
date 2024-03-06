import pandas as pd 
import random 
import os 
import itertools

# GLOBAL VARIABLES.
all_names = ["x", "y", "z", "Rx", "Ry", "Rz"]
name_pos = {"x":0, "y":1, "z":2, "Rx":3, "Ry":4, "Rz":5} 

def get_directions(dofs:list):
    all_dirs = [] 
    dir_name = []
    for indx, dof in enumerate(dofs):
        if dof:
            all_dirs.append((-1, 1)) 
            dir_name.append(all_names[indx])
        else:
            pass 
    return all_dirs 

def get_dof_indexes(names:list):
    indices = [] 
    for name in names:
        indices.append(name_pos[name]) 
    return indices 

def get_inactive_indices(active_indices:list):
    inactive_indices = []
    for i in range(6):
        if i not in active_indices:
            inactive_indices.append(i) 
    return inactive_indices

def get_name_vector(combination:list):
    name_vector = []
    for indx, val in enumerate(combination):
        if val != 0:
            name = all_names[indx]
            name_vector.append(name)
    return name_vector

def create_header(names:list) -> str:
    output = "|  " 
    for name in names:
        output = output + name + "  |  " 
    return output.strip("  ")

def display_combinations(filtered_combinations:list, names:list):
    print()
    header = create_header(names)
    title = " " * int(0.5 * len(header)) + "DOFs" + " " * int(0.5 * len(header))
    print(title)
    print('-' *len(header))
    print(header)
    print("-" * len(header)) 
    print() 
    for ind, combination in enumerate(filtered_combinations):
        print(f"Nr. {ind + 1}: ")
        name_vector = get_name_vector(combination) 
        output_str = "|  " 
        indicies = get_dof_indexes(name_vector) 
        for indx in indicies:
            output_str = output_str + str(combination[indx]) + "  |  " 
        output_str = output_str.strip("  ") 
        print("-"*len(output_str))
        print(output_str) 
        print("-" * len(output_str))

def get_dof_variables():
    variables = input("Enter the names of the variables, separated by comma (x, y, Rx, Ry, Rx2, etc ...): ") 
    dof_names = variables.split(",") 
    return dof_names 

def get_all_combinations(dof_names:list):
    options = [[-1, 1] for _ in range(len(dof_names))] 
    return list(itertools.product(*options)) 

def create_df(names:list, combinations:list):
    df = pd.DataFrame() 
    comb_lst = [list(comb) for comb in combinations]
    df[names] = comb_lst 
    return df 

def main():
    filename = "dof_combinations.csv" # name of the csv file storing all combinations.
    names = get_dof_variables() 
    combinations = get_all_combinations(names) 
    try:
        df = create_df(names, combinations) 
        df.to_csv(filename, index=False)  
        display_combinations(combinations, names)
        print("Combinations saved to " + filename)
    except Exception as e:
        print(e) 

if __name__ == "__main__":
    main()

