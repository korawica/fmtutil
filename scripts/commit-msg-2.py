#!/usr/bin/python3
"""
The commit-msg Git hook to check the commit message.
docs: https://cbea.ms/git-commit/

- Rule 01: Separate subject from body with a blank line
- Rule 02: Limit the subject line to 50 characters
- Rule 03: Capitalize the subject line
- Rule 04: Do not end the subject line with a period
- Rule 05: Use the imperative mood in the subject line
- Rule 06: Wrap the body at 72 characters
- Rule 07: Use the body to explain what and why vs. how
"""
import sys
from enum import Enum
from typing import Dict, List


class Emoji(str, Enum):
    FIX = ":gear:"
    FEAT = ":dart:"
    DOCS = ":page_facing_up:"
    BUILD = ":toolbox:"


class Bcolors(str, Enum):
    """A Enum for colors using ANSI escape sequences.
    Reference:
    - https://stackoverflow.com/questions/287871
    """

    OK = "\033[92m"
    INFO = "\033[94m"
    WARNING = "\033[93m"
    ERROR = "\033[91m"
    BOLD = "\033[1m"
    ENDC = "\033[0m"


class Level(str, Enum):
    """An Enum for notification levels."""

    OK = "OK"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"


WORD_EMOJI: Dict[str, Emoji] = {
    "feat": Emoji.FEAT,
    "fix": Emoji.FIX,
    "docs": Emoji.DOCS,
    "build": Emoji.BUILD,
    "workflow": Emoji.BUILD,
}


def print_color(message: str, level: Level) -> None:
    """Print the message with a color for the corresponding level."""
    print(
        f"{Bcolors[level]}{Bcolors.BOLD}"
        f"{level}: [Policy] {message}{Bcolors.ENDC}",
    )


def prepare_subject(subject: str) -> str:
    sub_lists: List[str] = [
        x.strip().strip(".") for x in subject.split(":", maxsplit=1)
    ]
    if len(sub_lists) == 1:
        sub_lists = ["feat", sub_lists[0]]

    if (stype := sub_lists[0]) not in WORD_EMOJI:
        print_color(
            f"There should be set emoji for prefix {stype} of subject",
            Level.ERROR,
        )
        sys.exit(1)

    return f"{WORD_EMOJI[stype]} {stype}: {sub_lists[1]}"


def validate_for_warning(lines: List[str]) -> bool:
    has_warning: bool = False
    subject: str = lines[0]
    # RULE 02: Limit the subject line to 50 characters
    if len(subject) <= 20 or len(subject) > 50:
        has_warning = True
        print_color(
            "There should be between 21 and 50 characters in the commit title.",
            Level.WARNING,
        )

    if len(lines) > 1:
        if len(lines) <= 2:
            has_warning = True
            print_color(
                "There should at least 3 lines in your commit message.",
                Level.WARNING,
            )

        # RULE 01: Separate subject from body with a blank line
        if lines[1].strip() != "":
            has_warning = True
            print_color(
                "There should be an empty line between the commit title and body.",
                Level.WARNING,
            )

    lines[0] = prepare_subject(subject)

    return has_warning


def check_commit_msg_pattern():
    """Check the format of the commit message.
    The argument passed to the "commit-msg" hook is the path to a
    temporary file that contains the commit message written by the
    developer.
    """
    msg_temp_file = sys.argv[1]

    with open(msg_temp_file, encoding="utf-8") as f_msg:
        lines = f_msg.readlines()

    # Remove the comment lines in the commit message.
    lines: List[str] = [
        line for line in lines if not line.strip().startswith("#")
    ]
    if not lines:
        print_color(
            "Please supply commit message without start with ``#``.",
            Level.ERROR,
        )
        sys.exit(1)

    # Validate print warning message
    has_warning: bool = validate_for_warning(lines)

    has_story_id = False
    for line in lines[2:]:
        # RULE 06: Wrap the body at 72 characters
        if len(line) > 72:
            message = "The commit body should wrap at 72 characters."
            print_color(message, Level.WARNING)
            sys.exit(1)

        if line.startswith("["):
            has_story_id = True

    if not has_story_id:
        message = "Please add a Story ID in the commit message."
        print_color(message, Level.WARNING)
        has_warning = True

    if not has_warning:
        message = "The commit message has the required pattern."
        print_color(message, Level.OK)

    with open(msg_temp_file, mode="w", encoding="utf-8") as file:
        file.write("\n".join(lines))

    sys.exit(0)


if __name__ == "__main__":
    # TODO: change to `raise SystemExit(check_commit_msg_pattern())`
    check_commit_msg_pattern()
