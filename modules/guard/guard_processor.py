import re
from modules import Container, console
from modules.config.enums import Actions

class GuardProcessor:
    REGEX = r'\[(\d{4}-\d{2}-\d{2}) (\d{2}):(\d{2})\] (falls asleep|wakes up|.*?#(\d.) begins shift)'

    @staticmethod
    def parse_line(line) -> Container:
        try:
            [date, hour, minute, action, guard] = re.match(GuardProcessor.REGEX, line).group(1,2,3,4,5)
        except Exception as e:
            return None

        parsed = Container()

        if guard is not None and hour == 23:
            hour = 00
            minute = 00
            [y,m,d] = date.split('-')
            d = '{:02}'.format(int(d) + 1)
            date = '{}-{}-{}'.format(y, m, d)

        parsed.date = date
        parsed.hour = hour
        parsed.minute = minute
        parsed.guard = guard

        if action.endswith('begins shift'):
            parsed.action = Actions.WORKING
        else:
            parsed.action = {
                'falls asleep': Actions.SLEEPING,
                'wakes up': Actions.WAKING,
            }.get(action, Actions.NONE)

        console.table('Date', parsed.date)
        console.table('Time', '{}:{}'.format(parsed.hour, parsed.minute))
        console.table('Guard', '{}'.format(parsed.guard))
        console.table('Action', '{}'.format(parsed.action))
        return parsed
