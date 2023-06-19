#!/usr/bin/python3
"""
Update release note before bump-version in main branch
"""
import subprocess
from collections import defaultdict
from pathlib import Path
from typing import List


def get_commit_logs(vs: str):
    return (
        subprocess.check_output(
            ["git", "log", f"{vs}..HEAD", "--oneline", "--no-merges"]
        )
        .decode("ascii")
        .strip()
        .split("\n")
    )


def prepare_commit_logs(logs: List[str]):
    result = defaultdict(list)
    _logs = [_.split(" ", maxsplit=1)[1] for _ in logs]
    _logs.reverse()
    for log in _logs:
        split_log = [_.strip() for _ in log.split(":", maxsplit=1)]
        if split_log[1]:
            result[split_log[0]].append(split_log[1])
    print(result)


def main() -> int:
    version: str = "v0.0.3.post1"

    try:
        commit_logs: List[str] = get_commit_logs(vs=version)
        prepare_commit_logs(commit_logs)
    except subprocess.CalledProcessError as err:
        print(err)
        return 1

    with open(
        Path("./docs/en/docs/CHANGELOG.md").resolve(),
        encoding="utf-8",
    ) as f_md:
        lines = f_md.readlines()

    writer = open(
        Path("./docs/en/docs/CHANGELOG.md").resolve(),
        mode="w",
        encoding="utf-8",
    )

    skip_line: bool = True
    for line in lines:
        if line.startswith("## Unreleased"):
            skip_line = False

        if line.startswith(f"## Version {version.lstrip('v')}"):
            print(f"Line start with: ## Version {version}")
            skip_line = True

        if skip_line:
            writer.write(line)
            continue
        else:
            print(line, end="")
            for _, message in (_.split(" ", maxsplit=1) for _ in commit_logs):
                writer.write(f"{message}\n")
            skip_line = True

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
