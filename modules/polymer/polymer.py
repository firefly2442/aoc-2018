from modules import console

class Polymer:
    @staticmethod
    def react_single_unit(polymer, unit):
        return polymer.replace('{}{}'.format(unit, unit.upper()), '').replace('{}{}'.format(unit.upper(), unit), '')

    @staticmethod
    def react(polymer):
        new_polymer = polymer
        for unit in 'abcdefghijklmnopqrstuvwxyz':
            new_polymer = Polymer.react_single_unit(new_polymer, unit)

        iterations = 0

        while polymer != new_polymer:
            iterations += 1

            polymer = new_polymer
            for unit in 'abcdefghijklmnopqrstuvwxyz':
                new_polymer = Polymer.react_single_unit(new_polymer, unit)

        console.log('Iterations', str(iterations), fg='cyan', bold=True, color_status=True, include_brackets=True)
        return new_polymer

    @staticmethod
    def get_best_score(polymer):
        units = set(list(polymer.lower()))
        print(units)

        shortest = None

        for unit in units:
            console.log('Removing', unit)
            polymerase = polymer.replace(unit, '').replace(unit.upper(), '')

            console.log('Reacting', '...')
            polymerase = Polymer.react(polymerase)

            console.log('Length', str(len(polymerase)))
            if shortest is not None and len(polymerase) >= len(shortest):
                continue

            shortest = polymerase

        return shortest
