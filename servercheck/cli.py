import click
import json 
import sys 
from .http import ping_servers

@click.command()
@click.option("--filename", "-f", default=None)
@click.option("--server", "-s", default=None, multiple=True)
def cli(filename, server):
    if not filename and not server:
        raise click.UsageError("must provide a JSON file or servers")
    
    servers = set()
    if filename:
        try:
            with open(filename) as f:
                json_servers = json.load(f)
                for s in json_servers:
                    servers.add(s)
        except:
            print("ERROR: Unable to open or read JSON File")
            sys.exit(1)
    
    if server:
        for s in server:
            servers.add(s)
    
    results = ping_servers(servers)
    
    print("Sucessfull servers")
    print("------------------")
    for server in results['success']:
        print(server)

    print("\nFailed Connections")
    print("------------------")
    for server in results['failure']:
        print(server)

if __name__ == "__main__":
    cli()