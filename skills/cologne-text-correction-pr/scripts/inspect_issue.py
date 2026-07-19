import json
import re
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")


def gh_issue(repo: str, number: str) -> dict:
    result = subprocess.run(
        [
            "gh",
            "issue",
            "view",
            number,
            "--repo",
            repo,
            "--json",
            "number,title,body,comments,labels,milestone,url",
        ],
        capture_output=True,
        encoding="utf-8",
    )
    if result.returncode != 0:
        raise SystemExit(result.stderr or result.stdout)
    return json.loads(result.stdout)


def snippets(text: str) -> list[str]:
    patterns = [
        r"v02/[A-Za-z0-9_-]+/[A-Za-z0-9_-]+\.txt:\d+:[^\n]+",
        r"^\s*\d+\s+(?:old|new|ins|del)\s+.+$",
        r"^\s*(?:old|new)\s*=.+$",
        r"\bID\s*=\s*\d+\b",
        r"\bL\s*=\s*\d+\b",
        r"<L>\d+[^`\n]*",
        r"<k1>[^`\n]+",
        r"Headword\s+[\"“][^\"”]+[\"”]",
    ]
    found: list[str] = []
    for pattern in patterns:
        found.extend(re.findall(pattern, text, flags=re.MULTILINE))
    return found[:40]


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit("usage: inspect_issue.py OWNER/REPO ISSUE_NUMBER")
    repo, number = sys.argv[1], sys.argv[2]
    issue = gh_issue(repo, number)
    combined = issue.get("body") or ""
    for comment in issue.get("comments") or []:
        combined += "\n\n" + (comment.get("body") or "")
    labels = [label["name"] for label in issue.get("labels") or []]
    print(f"{repo}#{issue['number']}: {issue['title']}")
    print(f"url: {issue['url']}")
    print(f"labels: {', '.join(labels) if labels else '(none)'}")
    milestone = issue.get("milestone")
    print(f"milestone: {milestone['title'] if milestone else '(none)'}")
    hits = snippets(combined)
    print(f"candidate clues: {len(hits)}")
    for hit in hits:
        print(f"- {hit[:500]}")


if __name__ == "__main__":
    main()
