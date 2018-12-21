import click, re

from functools import reduce
from modules import console, Timer, DataProvider, Container
from modules.graph import Node

def find(name, nodes):
    return next((n for n in nodes if n.name == name))

def best(available_picks):
    picks = set([n.name for n in available_picks])
    pick = min(picks)

    return pick

def get_step_execution_time(step):
    MIN_EXECUTION_TIME = 60
    return 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.index(step) + 1 + MIN_EXECUTION_TIME

def get_thread(node, execution_time):
    thread = Container()
    thread.node = node
    thread.remaining = execution_time

    return thread

def build_graph(root):
    if not root.child_nodes:
        return root.name
    return '[ {} -> {} ]'.format(root.name, ' '.join([build_graph(n) for n in root.child_nodes]))


@click.command()
def executor():
    console.header('day 7, part 2')

    timer = Timer()
    steps = DataProvider.load('day7')
    WORKERS = 5

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

    available_picks = root_node.child_nodes
    completed_picks = []
    available_workers = WORKERS
    threads = []
    in_progress = True
    elapsed = 0
    output = ''

    console.log('Graph', build_graph(root_node))

    while in_progress:
        console.header('working')
        while available_workers > 0 and len(available_picks) > 0 and len(threads) < WORKERS:
            console.log('Task', 'Creating worker thread ({} workers available)'.format(available_workers))

            available_workers -= 1
            pick = best(available_picks)
            node = find(pick, nodes)
            console.log('Info', 'Picking {} from {{ {} }}'.format(pick, ', '.join(set([n.name for n in available_picks]))))

            execution_time = get_step_execution_time(node.name)
            console.log('Info', 'Executing Step {} in {} seconds'.format(node.name, execution_time))
            threads.append(get_thread(node, execution_time))

            available_picks = list(filter(lambda n: n.name != pick, available_picks))

        console.log('Task', 'Update thread times')

        for thread in threads:
            if thread is not None:
                thread.remaining -= 1

        console.log('Task', 'Checking status')
        console.log('Info', 'Working thread count: {}'.format(str(len([n for n in threads if n is not None]))))
        for thread in threads:
            if thread is None:
                continue

            if thread.remaining < 1:
                console.log('Info', 'Completing step {}'.format(thread.node.name))
                console.log('Info', 'Child nodes: {} ( {} )'.format(len(thread.node.child_nodes), ''.join([n.name for n in thread.node.child_nodes])))
                thread.node.triggered = True
                output += thread.node.name
                completed_picks.append(thread.node.name)
                available_picks = available_picks + list(set([n for n in thread.node.child_nodes if n.can_trigger()]))
                available_picks = list(filter(lambda p: p not in [t.node.name for t in threads]and p not in completed_picks, available_picks))
                available_workers += 1
                if available_workers > WORKERS:
                    available_workers = WORKERS

        threads = list(filter(lambda t: t is not None and t.remaining > 0, threads))

        elapsed += 1

        console.header('status report')
        console.log('Info', 'Elapsed time: {}'.format(elapsed))
        console.log('Info', 'Active Thread Count: {}'.format(len([t for t in threads if t is not None])))
        console.log('Info', 'Available Workers: {}'.format(available_workers))
        console.log('Info', 'Available Picks: {{ {} }}'.format(', '.join([n.name for n in available_picks])))

        if not available_picks:
            if threads:
                in_progress = reduce(lambda t, i: t is not None or i, threads)
            else:
                in_progress = False

    timer.end()

    console.header('output')
    console.log('Order', output)
    console.log('Time', str(elapsed))
    timer.output()
