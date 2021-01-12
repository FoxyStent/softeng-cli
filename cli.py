import click 

@click.group()
def cli():
    pass

@cli.command()
@click.argument('--format')
@click.argument('--apikey')
def healthcheck():
    """Health Check. Testing end-to-end connectivity between user and db"""
    click.echo("Ola kala manito mou")

@cli.command()
@click.argument('--format')
@click.argument('--apikey')
def resetsessions():
    """Den exw idea"""
    click.echo("Opws ta leei i epe3igisi")

@cli.command()
@click.argument('--username', metavar='<username>')
@click.argument('--passw', metavar='<password>')
@click.argument('--format')
@click.argument('--apikey')
def login(username, passw):
    """User Login.
    
    \b
    __FORMAT is the desired format. JSON or CSV
    __APIKEY is your API-key"""
    click.echo('User %s wants to login' % username)

@cli.command()
@click.argument('--format')
@click.argument('--apikey')
def logout():
    """User Logout"""
    click.echo('User xxx Successfully logged out')

@cli.command()
@click.argument('--format')
@click.argument('--apikey')
def SessionsPerPoint():
    """Returning Charging Sessions of a Selected Point for a specific period"""
    click.echo('User xxx Successfully logged out')

@cli.command()
@click.argument('--format')
@click.argument('--apikey')
def SessionsPerStation():
    """Returning Charging Sessions of a Selected Station for a specific period"""
    click.echo('User xxx Successfully logged out')

@cli.command()
@click.argument('--format')
@click.argument('--apikey')
def SessionsPerEV():
    """Returning Charging Sessions of a Selected Electric Vechicle for a specific period"""
    click.echo('User xxx Successfully logged out')

@cli.command()
@click.argument('--format')
@click.argument('--apikey')
def SessionsPerProvider():
    """Returning Charging Sessions of a Selected Provider for a specific period"""
    click.echo('User xxx Successfully logged out')


#https://stackoverflow.com/questions/55584012/python-click-dependent-options-on-another-option
@cli.command()
@click.option('--usermod')
@click.argument('--format')
@click.argument('--apikey')
def Admin():
    """Advanced Commands for Admins"""
    click.echo('User xxx Successfully logged out')

