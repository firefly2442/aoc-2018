import click, numpy

from modules import console, Timer, Claim, DataProvider

@click.command()
def executor():
    console.header('day 3, part 1')

    max_x = 1000
    max_y = 1000
    elements = DataProvider.load('day3')
    claim_ids = []
    timer = Timer()

    timer.start()
    claims = numpy.zeros([max_x, max_y])
    for element in elements:
        claim = Claim(element)
        claims = claim.fill_claim(claims)

    for element in elements:
        claim = Claim(element)
        if claim.claim_is_alone(claims):
            claim_ids.append(claim.claim_id)
    timer.end()

    console.log(' ', 'Claim Ids', fg='cyan', bold=True, color_status=True, include_brackets=True)
    print(claim_ids)
    timer.output()
