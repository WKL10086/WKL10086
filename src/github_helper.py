from typing import Literal


def add_label_to_issue(context, repo, label_name: Literal["wkldle"]) -> None:
    issue = repo.get_issue(context.issue_number)
    issue.add_to_labels(label_name)

    return
