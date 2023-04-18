import requests
import json
import sys
import re

current_pr_number = sys.argv[1]
headers = {'Accept': 'application/vnd.github.v3+json'}
open_pull_requests = requests.get('https://api.github.com/repos/gka038/buffer-repo/pulls?state=open', headers=headers).json()

for obj in open_pull_requests:
    pr_num = obj['number']
    print("PR is open on buffer repo: ", str(pr_num))
    url='https://api.github.com/repos/gka038/buffer-repo/pulls/'+ str(pr_num) +'/files'
    pr_details = requests.get(url).json()
    for item in pr_details:
        file_changed = item["filename"]
        print("files changes on PR ", str(pr_num) , " for file ", file_changed)
        if file_changed.startswith('customer2'):
            pr_source = str(obj['title'])
            pr_title = "source PR: https://github.com/gka038/customer2/pull/"+ str(current_pr_number)
            if pr_title == pr_source:
                print("Ignoring the PR on buffer created due to this PR on customer2 repo")
            else:
                sys.exit('There is an open PRs on Buffer repo for this customer. Please close that to proceed')


print("No file conflicts on this customer in buffer repo PRs")

