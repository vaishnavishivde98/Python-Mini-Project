# Program to demonstrate integration with GitHub API
# This script fetches active pull requests from the Kubernetes repository
# and counts how many PRs each user has created.

import requests  # Import requests module to make HTTP API calls

# URL to fetch pull requests from the GitHub API
url = 'https://api.github.com/repos/kubernetes/kubernetes/pulls'

# Make a GET request to fetch pull request data
# (You can add authentication headers if needed for higher rate limits)
response = requests.get(url)

# Check if the request was successful (status code 200 = OK)
if response.status_code == 200:
    
    # Convert the JSON response into Python data (list of dictionaries)
    pull_requests = response.json()

    # Dictionary to store PR creators and their PR counts
    pr_creators = {}

    # Loop through each pull request in the response
    for pull in pull_requests:
        # Extract the username of the PR creator
        creator = pull['user']['login']
        
        # Count occurrences of each creator
        if creator in pr_creators:
            pr_creators[creator] += 1  # Increment count if already exists
        else:
            pr_creators[creator] = 1  # Initialize count for new creator

    # Display the results
    print("PR Creators and Counts:")
    for creator, count in pr_creators.items():
        print(f"{creator}: {count} PR(s)")

else:
    # If the request failed, print the status code
    print(f"Failed to fetch data. Status code: {response.status_code}")
