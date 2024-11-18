import os
import subprocess
from datetime import datetime, timedelta

# Define a repository name and path
repo_name = "fake-contributions"
repo_path = os.path.join(os.getcwd(), repo_name)

# Create a new Git repository
if not os.path.exists(repo_path):
    os.makedirs(repo_path)
    subprocess.run(["git", "init"], cwd=repo_path)
    print(f"Initialized empty Git repository in {repo_path}")

# Number of days to simulate commits
days_to_simulate = 100  # Adjust as needed
commits_per_day = 2     # Number of commits per day

start_date = datetime.now() - timedelta(days=days_to_simulate)

# Loop to create commits
for day in range(days_to_simulate):
    current_date = start_date + timedelta(days=day)
    for commit in range(commits_per_day):
        file_name = f"file_{day}_{commit}.txt"
        file_path = os.path.join(repo_path, file_name)

        # Create a file with some content
        with open(file_path, "w") as file:
            file.write(f"This is a commit for day {day}, commit {commit}.")

        # Add and commit the file
        subprocess.run(["git", "add", file_name], cwd=repo_path)
        subprocess.run(
            ["git", "commit", "-m", f"Add {file_name}", "--date", current_date.strftime("%Y-%m-%dT%H:%M:%S")],
            cwd=repo_path,
        )

        print(f"Committed {file_name} on {current_date.strftime('%Y-%m-%d')}")

print("Finished generating fake contributions!")

# Optionally push to GitHub
print("\nTo push the repository to GitHub, use:")
print(f"cd {repo_path}")
print("git remote add origin <your-repo-url>")
print("git branch -M main")
print("git push -u origin main")