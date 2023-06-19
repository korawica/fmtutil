#!/usr/bin/python3

import pathlib
import re
import subprocess
import sys

PROJECT_IDS = ["SLO"]
BRANCH_TYPES = ["feature", "bug", "hot"]

REGEX_PROJECT_IDS = "|".join(PROJECT_IDS)
REGEX_BRANCH_TYPES = "|".join(BRANCH_TYPES)

# Should contain a capturing group to extract the reference:
REGEX_BRANCH = rf"^(?:{REGEX_BRANCH_TYPES})/((?:{REGEX_PROJECT_IDS})-[\d]{{1,5}})-[a-z]+(?:-[a-z]+)*$"

# Should contain a capturing group to extract the reference (note the dot at the end
# is optional as this script will add it automatically for us):
REGEX_MESSAGE = rf"^((?:{REGEX_PROJECT_IDS})-[\d]{{1,5}}): .+\.?$"

# No capturing group. Just checking for the bare minimum:
REGEX_BASIC_MESSAGE = "^.+$"

# These branch names are not validated with this same rules (permissions should be configured
# on the server if you want to prevent pushing to any of these):
BRANCH_EXCEPTIONS = [
    "development",
    "develop",
    "dev",
    "staging",
    "sta",
    "master",
    "production",
]


def getBranchName():
    return (
        subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"])
        .decode("ascii")
        .strip()
    )


def getBranchRef(branch):
    match = re.findall(REGEX_BRANCH, branch)

    return match[0] if match and match[0] else None


def getMessageRef(message):
    match = re.findall(REGEX_MESSAGE, message)

    return match[0] if match and match[0] else None


def isCommitValid(message):
    isValid = True
    messageOverride = None
    branch = getBranchName()
    isException = branch in BRANCH_EXCEPTIONS

    if isException:
        print(
            f"\nWARNING: You might not have permissions to push to `{branch}`."
        )

        if not message.startswith("HOT: "):
            print(
                "\n         Also, you might consider prefixing the commit message with `HOT:`"
            )

        print(
            "\n         Use `git reset HEAD~` to undo this commit, create a proper branch and/or commit message and commit the changes again."
        )
        print("")

        return True

    branchRef = getBranchRef(branch)
    messageRef = getMessageRef(message)

    if not re.match(REGEX_BRANCH, branch):
        isValid = False
        print("\nERROR: Invalid branch name:")
        print(f"\n       It should match {REGEX_BRANCH}")
        print(
            f"\n       Example: {BRANCH_TYPES[0]}/{PROJECT_IDS[0]}-42-whatever-this-is"
        )

    if not re.match(REGEX_MESSAGE, message):
        if not re.match(REGEX_BASIC_MESSAGE, message):
            # So wrong there's no way to fix it automatically:
            isValid = False
            print("\nERROR: Super invalid commit message (shame on you):")
            print(f"\n       It should match `{REGEX_MESSAGE}`")
            print(
                f'\n       Example: {branchRef if branchRef else f"{PROJECT_IDS[0]}-42"}: Your commit message (with a dot at the end).'
            )
        else:
            messageOverride = _extracted_from_isCommitValid_50(
                branchRef, message
            )
    elif isValid and not message.strip().endswith("."):
        # The dot is optional, so both branch & message might be valid and still miss it:
        messageOverride = message.strip() + ".\n"

        print(
            "\nWARNING: You forgot the dot at the end of your commit message:"
        )
        print("\n         We have added it for you (you are welcome):")
        print(f"         {messageOverride}")

    if not messageOverride and isValid and branchRef != messageRef:
        isValid = False
        print(
            f"\nERROR: Branch ({branchRef}) and commit ({messageRef}) references do not match."
        )

    if not isValid or messageOverride:
        print("")

    return isValid, messageOverride


# TODO Rename this here and in `isCommitValid`
def _extracted_from_isCommitValid_50(branchRef, message):
    # Let's make a guess about the branch type and reference:
    result = f"feature/{branchRef}: {message}"

    if not result.strip().endswith("."):
        # The dot might be present in the original (but mostly incorrect) message:
        result = result.strip() + ".\n"

    print("\nWARNING: Mostly invalid commit message:")
    print(f"\n         It should match `{REGEX_MESSAGE}`")
    print("\n         We have tried to fix it for you (no need to thank us):")
    print(f"\n         {result}")
    print("         Use `git reset HEAD~` to undo this commit if we fucked up.")
    return result


def main():
    messageFile = sys.argv[1]
    message = pathlib.Path(messageFile).read_text()
    isValid, messageOverride = isCommitValid(message)

    if messageOverride:
        try:
            with open(messageFile, "w") as file:
                file.write(messageOverride)
        except Exception:
            isValid = False

    sys.exit(0 if isValid else 1)


if __name__ == "__main__":
    main()
