import click
import datetime
import requests
import json
import pandas as pd
from prettytable import PrettyTable

base_url="https://localhost:8765/evcharge/api

@click.group()
def cli():
    pass

#healthcheck (ready?)
@cli.command()
@click.option('--format', type=click.Choice(['json','csv']), default='json', help='This is the ooutput format', required=True)
@click.option('--apikey', help='This the API key', required=True)
def healthcheck(format, apikey):    
    """Checks if system is up and running"""

    res = json.loads(requests.get(base_url+"/healthcheck"))
    if res["status"] == "OK":
        print("System up and running")
    else:
        print("System down and drowning")  

#resetsessions
@cli.command()
@click.option('--apikey', help='This the API key', required=True)
def resetsessions(format, apikey):    
    """Clears all charge event entries, resets the default admin credentials"""

    res = json.loads(requests.get(base_url+"/resetsessions"))
    if res["status"] == "OK":
        print("All sessions have been reset. Default admin credentials have been reset.")
    else:
        print("Reset failed")



#login
@cli.command()
@click.option('--username',type=click.STRING, help='The user\'s username', required=True)
@click.option('--passw', ,type=click.STRING, help='The user\'s password', required=True)
@click.option('--apikey', help='This the API key', required=True)
def login(username, passw): 
    """Used to log a user into the system"""

    #needs implementation for un/pw encryption
    res = json.loads(requests.get(base_url+"/login?username="+username+"?passw="+passw))
    if "token" in res :
        #store token somewhere
        print("Login Successful")
        print("Welcome" +username)
    else:
        print("Login Failed") 






#logout
@cli.command()
@click.option('--apikey', help='This the API key', required=True)
def logout(): 
    """Used to log a user out of the system"""

    #something needs to be done here
    res = requests.get(base_url+"/logout?username="+username+"?passw="+passw)
    if res.status_code==200:
        print("Logout Successful")
    elif res.status_code=401:
        print("Unauthorized user")



#SessionsPerPoint
@cli.command()
@click.option('--point', help='The point in which we are interested', required=True)
@click.option('--datefrom',type=click.STRING, help='Starting date', required=True)
@click.option('--dateto',type=click.STRING, help='End date', required=True)
@click.option('--format', type=click.Choice(['json','csv']), default='json', help='This is the ooutput format', required=True)
@click.option('--apikey', help='This the API key', required=True)
def SessionsPerPoint(point, datefrom, dateto, format, apikey): 
    """Returns a summary of all charge events that have taken place on a single charging point POINT from
    DATEFROM until DATETO"""

    from_year=int(datefrom[0:4])
    from_month=int(datefrom[4:6])
    from_day=int(datefrom[6:8])
    to_year=int(dateto[0:4])
    to_month=int(dateto[4:6])
    to_day=int(dateto[6:8])

    from_date = datetime.date(from_year, from_month, from_day)
    to_date = datetime.date(to_year, to_month, to_day)

    if (len(datefrom) != 8) or (len(dateto) != 8):
        click.echo("Invalid date length!")
    
    elif from_day>31 or to_day>31 or to_month>12 or from_month>12:
        click.echo("Invalid date. Date  format must be YYYYMMDD")

    elif from_date > to_date:
        click.echo("Invalid dates input. FROM_DATE must not be later than TO_DATE")
    else:
        req_url = "/point/datefrom/dateto"
        res = requests.get(base_url+req_url)
        if format=='json':
            res = json.loads(res)
            #somehow print output
        else:
            df = pd.read_csv(res)
            #somehow print output




@#SessionsPerStation
@cli.command()
@click.option('--station', help='The station in which we are interested', required=True)
@click.option('--datefrom', type=click.STRING, help='Starting date', required=True)
@click.option('--dateto', type=click.STRING, help='End date', required=True)
@click.option('--format', type=click.Choice(['json','csv']), default='json', help='This is the ooutput format', required=True)
@click.option('--apikey', help='This the API key', required=True)
def SessionsPerStation(point, datefrom, dateto, format, apikey): 
    """Returns a summary of all charge events that have taken place on single station STATION from
    DATEFROM until DATETO"""

    from_year=int(datefrom[0:4])
    from_month=int(datefrom[4:6])
    from_day=int(datefrom[6:8])
    to_year=int(dateto[0:4])
    to_month=int(dateto[4:6])
    to_day=int(dateto[6:8])

    from_date = datetime.date(from_year, from_month, from_day)
    to_date = datetime.date(to_year, to_month, to_day)


    if (len(datefrom) != 8) or (len(dateto) != 8):
        click.echo("Invalid date length!")
    
    elif from_day>31 or to_day>31 or to_month>12 or from_month>12:
        click.echo("Invalid date. Date  format must be YYYYMMDD")

    elif from_date > to_date:
        click.echo("Invalid dates input. FROM_DATE must not be later than TO_DATE")
    else:
        pass




#SessionsPerEV
@ev_group16.command()
@click.option('--ev', help='The electric veichle in which the user is interested', required=True)
@click.option('--datefrom',type=click.STRING, help='Starting date', required=True)
@click.option('--dateto',type=click.STRING, help='End date', required=True)
@click.option('--format', type=click.Choice(['json','csv']), default='json', help='This is the ooutput format', required=True)
@click.option('--apikey', help='This the API key', required=True)
def SessionsPerEV(ev, datefrom, dateto, format, apikey): 
    """Returns a summary of all charge events that have taken place regarding a single veichle EV from
    DATEFROM until DATETO"""
    from_year=int(datefrom[0:4])
    from_month=int(datefrom[4:6])
    from_day=int(datefrom[6:8])
    to_year=int(dateto[0:4])
    to_month=int(dateto[4:6])
    to_day=int(dateto[6:8])

    from_date = datetime.date(from_year, from_month, from_day)
    to_date = datetime.date(to_year, to_month, to_day)


    if (len(datefrom) != 8) or (len(dateto) != 8):
        click.echo("Invalid date length!")
    
    elif from_day>31 or to_day>31 or to_month>12 or from_month>12:
        click.echo("Invalid date. Date  format must be YYYYMMDD")

    elif from_date > to_date:
        click.echo("Invalid dates input. FROM_DATE must not be later than TO_DATE")
    else:
        pass

#SessionsPerProvider
@cli.command()
@click.option('--provider', help='The electric veichle in which the user is interested', required=True)
@click.option('--datefrom', type=click.STRING, help='Starting date', required=True)
@click.option('--dateto', type=click.STRING, help='End date', required=True)
@click.option('--format', type=click.Choice(['json','csv']), default='json', help='This is the ooutput format', required=True)
@click.option('--apikey', help='This the API key', required=True)
def SessionsPerProvider(provider, datefrom, dateto, format, apikey): 
    """Returns a summary of all charge events that have taken place consuming electic current provided by PROVIDER from
    DATEFROM until DATETO"""

    from_year=int(datefrom[0:4])
    from_month=int(datefrom[4:6])
    from_day=int(datefrom[6:8])
    to_year=int(dateto[0:4])
    to_month=int(dateto[4:6])
    to_day=int(dateto[6:8])

    


    if (len(datefrom) != 8) or (len(dateto) != 8):
        click.echo("Invalid date length!")
        pass
    
    elif from_day>31 or to_day>31 or to_month>12 or from_month>12:
        click.echo("Invalid date. Date  format must be YYYYMMDD")
        pass

    from_date = datetime.date(from_year, from_month, from_day)
    to_date = datetime.date(to_year, to_month, to_day)
    if from_date > to_date:
        click.echo("Invalid dates input. FROM_DATE must not be later than TO_DATE")
    
    else:
        pass


#https://stackoverflow.com/questions/55584012/python-click-dependent-options-on-another-option
@cli.command()
@click.option('--usermod')
@click.argument('--format')
@click.argument('--apikey')
def Admin():
    """Advanced Commands for Admins"""
    click.echo('User xxx Successfully logged out')

