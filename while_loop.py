import random

# Define logic gate functions
def AND(a, b):
    return a & b

def OR(a, b):
    return a | b

def XOR(a, b):
    return a ^ b

def NOT(a):
    return 1 - a  # Since we're working with binary values (0 or 1)

# Simulate random inputs for the gates
def generate_random_input():
    return random.randint(0, 1)  # Generate either 0 or 1 randomly

# Create a simple digital circuit with random inputs
def digital_circuit():
    # Generate random inputs
    input1 = generate_random_input()
    input2 = generate_random_input()

    # Apply logic gates
    and_result = AND(input1, input2)
    or_result = OR(input1, input2)
    xor_result = XOR(input1, input2)
    not_result1 = NOT(input1)
    not_result2 = NOT(input2)

    return {
        'input1': input1,
        'input2': input2,
        'and_result': and_result,
        'or_result': or_result,
        'xor_result': xor_result,
        'not_result1': not_result1,
        'not_result2': not_result2
    }

# Run the digital circuit simulation with a while loop
def run_simulation():
    iteration_count = 0
    max_iterations = 10  # Set a limit for how many times to run the simulation
    and_count = 0
    or_count = 0
    xor_count = 0
    not_count1 = 0
    not_count2 = 0

    while iteration_count < max_iterations:
        iteration_count += 1

        # Run the digital circuit for random inputs
        results = digital_circuit()

        # Print the random inputs and the results of the logic gates
        print(f"Iteration {iteration_count}:")
        print(f"  Random Inputs: input1 = {results['input1']}, input2 = {results['input2']}")
        print(f"  AND result: {results['and_result']}")
        print(f"  OR result: {results['or_result']}")
        print(f"  XOR result: {results['xor_result']}")
        print(f"  NOT result for input1: {results['not_result1']}")
        print(f"  NOT result for input2: {results['not_result2']}")
        print("-" * 50)

        # Count the results of each gate
        and_count += results['and_result']
        or_count += results['or_result']
        xor_count += results['xor_result']
        not_count1 += results['not_result1']
        not_count2 += results['not_result2']

    # Print final counts after the loop ends
    print("\nSimulation complete!")
    print(f"Total AND results (1s): {and_count}")
    print(f"Total OR results (1s): {or_count}")
    print(f"Total XOR results (1s): {xor_count}")
    print(f"Total NOT result for input1 (1s): {not_count1}")
    print(f"Total NOT result for input2 (1s): {not_count2}")

# Run the simulation
run_simulation()

	
