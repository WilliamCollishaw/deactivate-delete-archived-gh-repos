import os
import re
import sys

def _get_token_from_env(token_name: str) -> str:
    """Retrieve token from environment variable."""
    print(f"Checking for {token_name} environment variable")
    token = os.getenv(token_name)
    if not token:
        print(f"{token_name} does not exist")
        sys.exit()
    print(f"Found {token_name}")
    return token

def get_snyk_token():
    SNYK_TOKEN = _get_token_from_env('SNYK_TOKEN')
    
    pattern = re.compile(r'snyk_uat\.\S+')
    if pattern.fullmatch(SNYK_TOKEN) == None:
        print("Snyk token is not defined or not valid.")
        sys.exit()
    else:
        return SNYK_TOKEN

def get_gitlab_token():
    GITLAB_TOKEN = _get_token_from_env('GITLAB_TOKEN')

    pattern = re.compile(r'glpat-\w{20}')
    if pattern.fullmatch(GITLAB_TOKEN) == None:
        print("GitLab token is not defined or not valid.")
        sys.exit()
    else:
        return GITLAB_TOKEN

def get_github_token():
    GITHUB_TOKEN = _get_token_from_env('GITHUB_TOKEN')

    pattern = re.compile(r'(ghp_|github_pat_)\w+')
    if pattern.fullmatch(GITHUB_TOKEN) == None:
        print("GitHub token is not defined or not valid.")
        sys.exit()
    else:
        return GITHUB_TOKEN