import click
from MEOWro import MEOWro

@click.group()
def cli():
    pass

#healthcheck
@cli.command()
@click.argument('--format')
@click.argument('--apikey')
def healthcheck():
    """Health Check. Testing end-to-end connectivity between user and db"""
    click.echo("Ola kala manito mou")

#resetsessions
@cli.command()
@click.argument('--format')
@click.argument('--apikey')
def resetsessions():
    """Den exw idea"""
    click.echo("Opws ta leei i epe3igisi")

#login
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

#logout
@cli.command()
@click.argument('--format')
@click.argument('--apikey')
def logout():
    """User Logout"""
    click.echo('User xxx Successfully logged out')

#SessionsPerPoint
@cli.command()
@click.argument('--format')
@click.argument('--apikey')
def SessionsPerPoint():
    """Returning Charging Sessions of a Selected Point for a specific period"""
    click.echo('User xxx Successfully logged out')

#SessionsPerStation
@cli.command()
@click.argument('--format')
@click.argument('--apikey')
def SessionsPerStation():
    """Returning Charging Sessions of a Selected Station for a specific period"""
    click.echo('User xxx Successfully logged out')

#SessionsPerEV
@cli.command()
@click.argument('--format')
@click.argument('--apikey')
def SessionsPerEV():
    """Returning Charging Sessions of a Selected Electric Vechicle for a specific period"""
    click.echo('User xxx Successfully logged out')

#SessionsPerProvider
@cli.command()
@click.argument('--format')
@click.argument('--apikey')
def SessionsPerProvider():
    """Returning Charging Sessions of a Selected Provider for a specific period"""
    click.echo('User xxx Successfully logged out')


#Admin
#https://stackoverflow.com/questions/55584012/python-click-dependent-options-on-another-option
@cli.command()
@click.option("--usermod",
            flag_value=True,
            cls=MEOWro,
            help='Create new user or change password',
            required_options=['username', 'password'],
            mutually_exclusive=['users', 'sessionsupd', 'healthcheck', 'resetsessions'])
@click.option('--username',
            cls=MEOWro,
            required_options=['usermod'])
@click.option('--password',
            cls=MEOWro,
            required_options=['usermod'])
@click.option("--users",
            cls=MEOWro,
            help='Show state of user',
            mutually_exclusive=['usermod', 'sessionsupd', 'healthcheck', 'resetsessions'])
@click.option("--sessionsupd",
            flag_value=True,
            cls=MEOWro,
            help='Add new sessions from csv file.',
            required_options=['source'],
            mutually_exclusive=['usermod', 'users', 'healthcheck', 'resetsessions'])
@click.option("--healthcheck",
            flag_value=True,
            cls = MEOWro,
            mutually_exclusive=['usermod', 'users', 'sessionsupd', 'resetsessions'])
@click.option("--resetsessions",
            flag_value=True,
            cls = MEOWro,
            mutually_exclusive=['usermod', 'users', 'sessionsupd', 'healthcheck'])
def Admin(usermod, users, sessionsupd, healthcheck, resetsessions):
    """Advanced Commands for Admins"""
    click.echo('User xxx Successfully logged out')

