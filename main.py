"""Helpdesk KB search: search local Markdown KB files by keyword, ranked."""
import argparse
import os
import sys


def search(kb_dir, query):
    terms = [t.lower() for t in query.split() if t]
    results = []
    for name in sorted(os.listdir(kb_dir)):
        if not name.endswith(".md"):
            continue
        path = os.path.join(kb_dir, name)
        try:
            text = open(path, encoding="utf-8").read()
        except OSError:
            continue
        low = text.lower()
        score = sum(low.count(t) for t in terms)
        if score:
            first = next((l.strip() for l in text.splitlines() if l.strip()), "")
            results.append({"file": name, "score": score, "snippet": first})
    results.sort(key=lambda r: r["score"], reverse=True)
    return results


def main(argv=None):
    p = argparse.ArgumentParser(description="Search a Markdown knowledge base.")
    p.add_argument("--kb", required=True)
    p.add_argument("query", nargs="+")
    args = p.parse_args(argv)
    for r in search(args.kb, " ".join(args.query)):
        print(f"{r['score']}  {r['file']}  {r['snippet']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
