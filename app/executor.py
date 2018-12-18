import click, os

from os.path import join, dirname, realpath, exists

BASE_PATH = dirname(realpath(__file__))

class AocExecutor(click.MultiCommand):
    def list_commands(self, ctx):
        rv = []
        for filename in os.listdir(join(BASE_PATH, 'plugins')):
            if filename.endswith('.py'):
                rv.append(filename[:-3])
        rv.sort()
        return rv

    def get_command(self, ctx, name):
        ns = {}
        ctx.obj = {
            'BASE_PATH': BASE_PATH,
        }

        fn = join(BASE_PATH, 'plugins', '{}.py'.format(name))
        if not exists(fn):
            raise click.ClickException('Cannot find plugin')
        with open(fn) as f:
            code = compile(f.read(), fn, 'exec')
            eval(code, ns, ns)

        return ns['executor']

cli = AocExecutor()

if __name__ == '__main__':
    cli()
