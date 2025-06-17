import os
import re
import subprocess
import sys


def detect_branch(repo_url: str) -> str:
    """Detect the branch to clone.

    Prefer 'work' if it exists. Otherwise return the remote default branch
    or 'main' if detection fails.
    """
    try:
        heads = subprocess.check_output(
            ["git", "ls-remote", "--heads", repo_url], stderr=subprocess.DEVNULL
        ).decode()
        if "refs/heads/work" in heads:
            return "work"
        # Get default branch
        symref = subprocess.check_output(
            ["git", "ls-remote", "--symref", repo_url, "HEAD"],
            stderr=subprocess.DEVNULL,
        ).decode()
        m = re.search(r"ref: refs/heads/(.+)\s+HEAD", symref)
        if m:
            return m.group(1)
    except Exception:
        pass
    return "main"


def clone_repo(repo_url: str, target_dir: str = None):
    branch = detect_branch(repo_url)
    print(f"Cloning branch '{branch}' from {repo_url}")
    cmd = ["git", "clone", "--depth", "1", "--branch", branch, repo_url]
    if target_dir:
        cmd.append(target_dir)
    subprocess.check_call(cmd)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python clone_repo.py <repo_url> [target_dir]")
        sys.exit(1)
    clone_repo(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
