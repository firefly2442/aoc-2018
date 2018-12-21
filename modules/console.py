import click

class console(object):
    @staticmethod
    def header(msg, width=80, fg='green', bold=True):
        msg = click.style(' {} '.format(str(msg).upper()), fg=fg, bold=bold)
        click.echo('\n{:-^{width}}'.format(msg, width=width))

    @staticmethod
    def log(status, msg=None, fg='white', bold=False, color_status=False, width=12, arrow=None, include_brackets=False):
        if not status and msg is None:
            click.echo('')
            return

        if arrow is None:
            arrow = ' -> '

        if msg is None:
            msg = str(status)
            status = ''

        if status:
            status_width = width - 2 if include_brackets else width
            status = '{:>{width}}'.format(str(status), width=status_width)

        if color_status:
            status = click.style(status, fg=fg, bold=bold)
        else:
            msg = click.style(str(msg), fg=fg, bold=bold)

        if status:
            if include_brackets:
                status = '[{}]'.format(status)
            click.echo('{}{}{}'.format(status, arrow, msg))
        else:
            click.echo('{}{}'.format(arrow, msg))

    @staticmethod
    def table(left, right, width=12, fg='white', bold=False, color_status=False, arrow=': ', include_brackets=False):
        console.log(left, right, fg=fg, bold=bold, color_status=color_status, width=width, arrow=arrow, include_brackets=include_brackets)

    @staticmethod
    def error(msg):
        console.log('ERROR', msg, fg='red', bold=True, color_status=True, arrow=' ! ', include_brackets=True)

    @staticmethod
    def warning(msg):
        console.log('WARN', msg, fg='yellow', bold=True, color_status=True, include_brackets=True)

    @staticmethod
    def info(msg):
        console.log('INFO', msg, fg='cyan', bold=True, color_status=True, include_brackets=True)

    @staticmethod
    def success(msg):
        console.log('SUCCESS', msg, fg='green', bold=True, color_status=True, include_brackets=True)
