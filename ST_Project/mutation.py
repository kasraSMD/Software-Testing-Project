import os
import random
import shutil
import unittest

MAX_ITERATION = 100
GENERATIONS_MUTATIONS_SCORE = {}
RESULT_FOLDER_NAME = "mutation_files"

testFile_attribute = {
    "test_file_address": f"{RESULT_FOLDER_NAME}",
    "test_class_name": "TestCalculateAreaAndPerimeter",
    "test_function_name": "test_rectangle_with_positive_values"
}
ALL_ASSIGNMENT_OPERATORS = [' = ', ' += ', ' -= ', ' *= ', ' /= ', ' %= ', ' **= ', ' //= ', ' &= ', ' |= ', ' ^= ',
                            ' <<= ', ' >>= ']

ASSIGNMENT_OPERATORS_LIST = [{' = ': 'Assigns'},
                             {' += ': 'Adds'},
                             {' -= ': 'Subtracts'},
                             {' *= ': 'Multiplies'},
                             {' /= ': 'Divides'},
                             {' %= ': 'Modulus'},
                             {' **= ': 'Exponentiation'},
                             {' //= ': 'FloorDivision'},
                             {' &= ': 'BitwiseAND'},
                             {' |= ': 'BitwiseOR'},
                             {' ^= ': 'BitwiseXOR'},
                             {' <<= ': 'BitwiseLeftShift'},
                             {' >>= ': 'BitwiseRightShift'}]


class Assignment_Element:
    def __init__(self, line, index, element):
        self.line = line
        self.index = index
        self.element = element

    def __str__(self):
        return f"{self.line} , {self.index} , {self.element}"


def find_all_occurrences(sub_string, main_string, line):
    indexes = []
    index = -1
    arrays = []
    while True:
        index = main_string.find(sub_string, index + 1)
        if index == -1:
            break
        indexes.append(index)
    for i in range(len(indexes)):
        if indexes[i] is not None:
            c = Assignment_Element(line=line, index=indexes[i], element=sub_string)
            arrays.append(c)
    return arrays


def get_random_elements(array, n, special_index):
    excluded_array = array[:special_index] + array[special_index + 1:]
    n = min(n, len(excluded_array))
    random_elements = random.sample(excluded_array, n)
    return random_elements


def calculate_mutation_score(live_mutations, killed_mutations, stillborn_mutations):
    total_mutations = live_mutations + killed_mutations + stillborn_mutations
    effective_mutations = killed_mutations + stillborn_mutations
    mutation_score = (effective_mutations / total_mutations) * 100
    return mutation_score


def runTest(test_file_address, test_class_name, test_function_name):
    module = __import__(test_file_address.replace('.py', ''), fromlist=[test_class_name])
    test_class = getattr(module, test_class_name)

    suite = unittest.TestSuite()
    suite.addTest(test_class(test_function_name))

    result = unittest.TestResult()
    suite.run(result)

    test_results = {
        'passed': result.wasSuccessful(),
        'failed': len(result.failures),
        'errors': len(result.errors),
        'error_results': result.errors
    }

    return test_results


def process_input_file(input_file, test_file):
    assignment_elements = []

    try:
        with open(input_file, 'r') as fin:
            lines = fin.readlines()
            for i in range(len(lines)):
                if lines[i].__contains__("#"):
                    continue
                output0 = find_all_occurrences(ALL_ASSIGNMENT_OPERATORS[0], lines[i], i)
                output1 = find_all_occurrences(ALL_ASSIGNMENT_OPERATORS[1], lines[i], i)
                output2 = find_all_occurrences(ALL_ASSIGNMENT_OPERATORS[2], lines[i], i)
                output3 = find_all_occurrences(ALL_ASSIGNMENT_OPERATORS[3], lines[i], i)
                output4 = find_all_occurrences(ALL_ASSIGNMENT_OPERATORS[4], lines[i], i)
                output5 = find_all_occurrences(ALL_ASSIGNMENT_OPERATORS[5], lines[i], i)
                output6 = find_all_occurrences(ALL_ASSIGNMENT_OPERATORS[6], lines[i], i)
                output7 = find_all_occurrences(ALL_ASSIGNMENT_OPERATORS[7], lines[i], i)
                output8 = find_all_occurrences(ALL_ASSIGNMENT_OPERATORS[8], lines[i], i)
                output9 = find_all_occurrences(ALL_ASSIGNMENT_OPERATORS[9], lines[i], i)
                output10 = find_all_occurrences(ALL_ASSIGNMENT_OPERATORS[10], lines[i], i)
                output11 = find_all_occurrences(ALL_ASSIGNMENT_OPERATORS[11], lines[i], i)
                output12 = find_all_occurrences(ALL_ASSIGNMENT_OPERATORS[12], lines[i], i)
                if output0:
                    assignment_elements += output0
                if output1:
                    assignment_elements += output1
                if output2:
                    assignment_elements += output2
                if output3:
                    assignment_elements += output3
                if output4:
                    assignment_elements += output4
                if output5:
                    assignment_elements += output5
                if output6:
                    assignment_elements += output6
                if output7:
                    assignment_elements += output7
                if output8:
                    assignment_elements += output8
                if output9:
                    assignment_elements += output9
                if output10:
                    assignment_elements += output10
                if output11:
                    assignment_elements += output11
                if output12:
                    assignment_elements += output12

            if len(assignment_elements) == 0:
                raise Exception("There Is NO MUTATIONS ")

            for generationNumber in range(MAX_ITERATION):
                generation_name = f"generation{generationNumber + 1}"
                generation_mutations_folder_address = fr"{RESULT_FOLDER_NAME}\{generation_name}"
                os.makedirs(generation_mutations_folder_address)
                print(generation_name)
                total_mutationNumber = 0
                all_mutation_files = []
                live_mutations = []
                killed_mutations = []
                stillborn_mutations_files = []
                stillborn_mutations = {}
                for i in range(len(assignment_elements)):
                    index_element = ALL_ASSIGNMENT_OPERATORS.index(assignment_elements[i].element)
                    mutation_number = random.randint(1, len(ALL_ASSIGNMENT_OPERATORS) - 1)
                    mutation_list = get_random_elements(array=ALL_ASSIGNMENT_OPERATORS, n=mutation_number,
                                                        special_index=index_element)

                    for q in range(len(mutation_list)):
                        total_mutationNumber += 1
                        for j in range(len(lines)):
                            new_file = lines.copy()
                            if j == assignment_elements[i].line:
                                new_line = new_file[j][:assignment_elements[i].index] + mutation_list[q] + \
                                           new_file[j][
                                           assignment_elements[i].index + len(assignment_elements[i].element):]

                                new_file[j] = new_line

                                main_assignment_Name = ""
                                replaced_assignment_Name = ""
                                for assignment in ASSIGNMENT_OPERATORS_LIST:
                                    if assignment.keys().__contains__(assignment_elements[i].element):
                                        main_assignment_Name = assignment[assignment_elements[i].element]
                                    if assignment.keys().__contains__(mutation_list[q]):
                                        replaced_assignment_Name = assignment[mutation_list[q]]

                                new_file += "\n\n\n\n\n\n\n\n\n"
                                for testLine in test_file:
                                    new_file += testLine

                                mutation_filename = \
                                    f"{total_mutationNumber} mutation{q + 1} for {main_assignment_Name} " \
                                    f"To {replaced_assignment_Name} (Line_{assignment_elements[i].line} " \
                                    f"Index_{assignment_elements[i].index}).py"

                                all_mutation_files.append(mutation_filename)
                                with open(fr"{generation_mutations_folder_address}\{mutation_filename}", 'w') as f:
                                    f.writelines(new_file)
                                break

                for i in range(len(all_mutation_files)):

                    test_file_address = testFile_attribute["test_file_address"]
                    test_class_name = testFile_attribute["test_class_name"]
                    test_function_name = testFile_attribute["test_function_name"]

                    result = runTest(
                        test_file_address=fr"{test_file_address}.{generation_name}.{all_mutation_files[i]}",
                        test_class_name=f"{test_class_name}",
                        test_function_name=f"{test_function_name}")

                    if result['passed'] is True:
                        live_mutations.append(all_mutation_files[i])
                    elif result['passed'] is False and result["errors"] == 0:
                        killed_mutations.append(all_mutation_files[i])

                    if result['errors'] > 0:
                        stillborn_mutations_files.append(all_mutation_files[i])
                        stillborn_mutations.update({all_mutation_files[i]: result["error_results"]})

                mutation_score = calculate_mutation_score(live_mutations=len(live_mutations),
                                                          killed_mutations=len(killed_mutations),
                                                          stillborn_mutations=len(stillborn_mutations))
                GENERATIONS_MUTATIONS_SCORE.update({generation_name: mutation_score})

                text = f"Total mutation number : {total_mutationNumber}\n" \
                       f"Number of live mutations : {len(live_mutations)}\n" \
                       f"Number of killed mutations : {len(killed_mutations)}\n" \
                       f"Number of stillborn mutations : {len(stillborn_mutations)}\n" \
                       f"\nThe Mutation Score : {mutation_score}\n\n" \
                       f"Live mutations files name :\n" \
                       f"{live_mutations}\n" \
                       f"\nKilled mutations files name :\n" \
                       f"{killed_mutations}\n" \
                       f"\nStillborn mutations files name :\n" \
                       f"{stillborn_mutations_files}\n"

                with open(fr"{generation_mutations_folder_address}\result.txt", 'w') as f:
                    f.writelines(text)

        print("\u001B[32m\nGenerations with Mutation Scores :")
        print(GENERATIONS_MUTATIONS_SCORE, "\u001B[0m")

        max_value = max(GENERATIONS_MUTATIONS_SCORE.values())
        max_keys = [key for key, value in GENERATIONS_MUTATIONS_SCORE.items() if value == max_value]
        print(f"\u001B[36m\nMax Mutation Score : {max_value}")
        print(max_keys, "\u001B[0m")

        min_value = min(GENERATIONS_MUTATIONS_SCORE.values())
        min_keys = [key for key, value in GENERATIONS_MUTATIONS_SCORE.items() if value == min_value]
        print(f"\u001B[31m\nMin Mutation Score : {min_value}")
        print(min_keys, "\u001B[0m")

        key_with_score_not_100 = [key for key, value in GENERATIONS_MUTATIONS_SCORE.items() if value != 100.0]
        print(f"\u001B[35m\nGenerations with Mutation Score != 100% :")
        print(key_with_score_not_100, "\u001B[0m")

        report_file = f"Generations with Mutation Scores : \n{GENERATIONS_MUTATIONS_SCORE}\n" + \
                      f"\nMax Mutation Score : {max_value}\n" + \
                      f"{max_keys}\n" + \
                      f"\nMin Mutation Score : {min_value}\n" + \
                      f"{min_keys}\n" + \
                      f"\nGenerations with Mutation Score != 100% :\n" + \
                      f"{key_with_score_not_100}\n"
        with open(fr"{RESULT_FOLDER_NAME}\report.txt", 'w') as f:
            f.writelines(report_file)

    except FileNotFoundError:
        print(f"File {input_file} not found.")


if __name__ == "__main__":
    # if len(sys.argv) < 2:
    #     print("Please provide the filename as a command-line argument.")
    # else:
    #     input_file = sys.argv[1]
    #     process_input_file(input_file)
    if os.path.exists(RESULT_FOLDER_NAME):
        shutil.rmtree(RESULT_FOLDER_NAME)
    os.makedirs(RESULT_FOLDER_NAME)
    with open("test.py", 'r') as file:
        testFile = file.readlines()

    try:
        process_input_file(input_file="input.py", test_file=testFile)

    except Exception as e:
        print(e)
