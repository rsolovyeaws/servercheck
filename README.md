# Servercheck

We frequently have to check whether one of our servers has access to other servers on our internal network. To make this a little easier for ourselves, we've decided to use Python to write a CLI that can either take a JSON file with servers and ports to check or a list of host/port combinations to make requests to. The team has already created the CLI to collect information from the user. Now we're ready to use the server/port combinations to ensure that we receive successful HTTP responses to each request.

In this hands-on lab, we're going to write the code that can take a set of server/port combinations and concurrently make requests for each one. The server/port combinations will not contain the scheme, and we will utilize http. We want to return a dictionary that contains our results divided up into successful and failed responses. When we're done, it will look like this:
```
{
    'success': [
        'IP1:PORT1',
        'IP1:PORT2'
    ],
    'failure': {
        'IP1:PORT3',
        'IP2:PORT1'
    }
}
```
We'll be working in a project at ~/servercheck. Its virtualenv can be activated using pipenv shell from within the project.

If you'd like to follow along on your own development machine, you can clone this github project. To make test HTTP connections, you'll still be able to utilize the web nodes using their public IP addresses.
