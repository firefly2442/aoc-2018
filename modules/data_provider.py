import click

from os.path import dirname, join

class DataProvider:
    @staticmethod
    @click.pass_context
    def load(ctx, filename):
        lines = []
        with open(join(dirname(ctx.obj['BASE_PATH']), 'data', '{}.txt'.format(filename))) as handle:
            for line in handle:
                lines.append(line)

        return lines
