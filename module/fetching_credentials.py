from dotenv import dotenv_values
from collections import defaultdict

def fetching_credentials(secret_path:str)-> dict:
    """
    parse credentials details from secret file
    input  - secret_path:str
    output - credentails: dic(dic(str)) 
    output format - {name:{username:username,password:password}}
    """
    
    credentials = defaultdict(lambda: defaultdict(str))
    for key,value in dotenv_values(secret_path).items():
        user,info = key.lower().split('_')
        credentials[user][info] = value 
    return credentials