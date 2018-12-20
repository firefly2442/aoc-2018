import click, re

from modules import console, Timer, DataProvider
from modules.graph import Node

def find(name, nodes):
    return next((n for n in nodes if n.name == name))

@click.command()
def executor():
    console.header('day 7, part 1')

    timer = Timer()
    steps = DataProvider.load('day7')
    # steps = [
    #     'Step C must be finished before step A can begin.',
    #     'Step C must be finished before step F can begin.',
    #     'Step A must be finished before step B can begin.',
    #     'Step A must be finished before step D can begin.',
    #     'Step B must be finished before step E can begin.',
    #     'Step D must be finished before step E can begin.',
    #     'Step F must be finished before step E can begin.',
    # ]

    timer.start()

    console.log('Task', 'Build nodes')
    node_names = set([])
    for step in steps:
        [parent, child] = re.match(r'Step ([A-Z]) .*? step ([A-Z]).*', step).group(1, 2)
        node_names.add(parent)
        node_names.add(child)

    console.log('Info', 'Creating {} nodes'.format(len(node_names)))
    nodes = []
    for node_name in node_names:
        nodes.append(Node(node_name))

    console.log('Info', 'Executing steps')
    count = 0
    for step in steps:
        count += 1
        console.log('Info', 'Step {} / {}'.format(count, len(steps)))

        [parent, child] = re.match(r'Step ([A-Z]) .*? step ([A-Z]).*', step).group(1, 2)

        parent = find(parent, nodes)
        child = find(child, nodes)

        parent.add_child(child)

    console.log('Info', 'Creating root node and children')
    root_node = Node('-')
    for node in [node for node in nodes if node.is_root()]:
        root_node.add_child(node)

    console.header('node picker')
    available_picks = root_node.child_nodes
    output = ''
    while available_picks:
        picks = set(sorted([n.name for n in available_picks]))
        pick = min(picks)

        console.log('Info', 'Picking {} from {{ {} }}'.format(pick, ', '.join([n.name for n in available_picks])))

        node = find(pick, nodes)
        node.triggered = True
        output += node.name
        available_picks = list(filter(lambda n: n.name != pick, available_picks)) + [n for n in node.child_nodes if n.can_trigger()]

    timer.end()

    console.header('output')
    console.log('Output', output)
    timer.output()
