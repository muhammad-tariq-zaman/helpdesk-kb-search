# helpdesk-kb-search

Search local Markdown knowledge-base files by keyword and rank results by
number of matches, with the first line of each file as a snippet.

## How to run

```bash
python3 main.py --kb ./kb vpn password reset
```

## Example output (sample from test fixture data)

```text
4  vpn.md  # VPN fix
1  printer.md  # Printer
```

Standard library only. No network access.
