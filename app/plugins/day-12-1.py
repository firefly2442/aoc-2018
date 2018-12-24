import click, re

from modules import console, Timer, DataProvider

def getPlantIteration(initial_state, rules, replacement):
    # add "negative" and "positive" spots to account for plants spreading outside the initial array
    while(not initial_state.startswith("....")):
        initial_state = "." + initial_state
    while(not initial_state.endswith("....")):
        initial_state = initial_state + "."
    # make an empty list for the plants
    final_state = list()
    for i in range(0,len(initial_state)):
        final_state.append(".")

    for i in range(2, len(initial_state)-2):
        substring = ''.join(list(initial_state)[i-2:i+3])
        if substring in rules:
            final_state[i] = replacement[rules.index(substring)-2]

    final_state = ''.join(final_state) # turn our list back into a string
    total_plants = len([m.start() for m in re.finditer(re.escape('#'), final_state)])
    return(final_state, total_plants)

@click.command()
def executor():
    console.header('day 12, part 1')

    timer = Timer()
    timer.start()

    initial_state = "#..#.#..##......###...###"

    rules = DataProvider.load('day12')
    matching = list()
    replacement = list()
    for spread in rules:
        split = spread.split(' => ')
        matching.append(split[0].strip()) # .strip() removes all whitespace characters including newlines
        replacement.append(split[1].strip())
    res = None
    inp = initial_state
    total_plants = 0
    for i in range(0,21):
        print(i, inp, ' Total Plants: ', len([m.start() for m in re.finditer(re.escape('#'), inp)]))
        inp, k = getPlantIteration(inp, matching, replacement)
        total_plants += k

    final_state = inp

    timer.end()

    console.header('output')
    console.log('After 20 iterations:')
    console.log('Initial State', initial_state)
    console.log('Final State', final_state)
    console.log('Total Plants', total_plants)
    timer.output()
