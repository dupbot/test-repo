import json
import requests

# Authentication info

with open('./input/authParams.txt') as f:
    USERNAME, TOKEN = f.read().splitlines()

# The repository to add this issue to

with open('./input/prParams.txt') as f:
    REPO_NAME, REPO_OWNER, PR_NUMBER = f.read().splitlines()
    PR_NUMBER = int(PR_NUMBER, 10)

def make_github_comment(body=None):
    '''Create a comment on github.com using the given parameters.'''
    # Our url to create comments via POST
    url = 'https://api.github.com/repos/%s/%s/issues/%i/comments' % (REPO_OWNER, REPO_NAME, PR_NUMBER)
    # Create an authenticated session to create the comment
    headers = {
        "Authorization": "token %s" % TOKEN,
    }
    # Create our comment
    data = {'body': body}

    r = requests.post(url, json.dumps(data), headers=headers)
    if r.status_code == 201:
        print('Successfully created comment "%s"' % body)
    else:
        print('Could not create comment "%s"' % body)
        print('Response:', r.content)

make_github_comment("""__Hi there! This pull request looks like it might be a duplicate of #2.__

Please help us out by clicking one of the options below:
- This comment was [__useful__](https://pages.github.com/).
- This pull request is __not a duplicate__, so this comment was [__not useful__](https://pages.github.com/).
- I do not need this service, so this comment was [__not useful__](https://pages.github.com/).
                    """)
