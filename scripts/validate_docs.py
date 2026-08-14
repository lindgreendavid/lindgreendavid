"""Dependency-free quality and credential checks for Markdown-only repositories."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
SECRET_PATTERNS = {
    "Cloudflare API token": re.compile(r"cfat_[A-Za-z0-9_-]{20,}"),
    "GitHub personal access token": re.compile(r"gh[pousr]_[A-Za-z0-9]{20,}"),
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
}


def main() -> None:
    documents = sorted(ROOT.glob("*.md"))
    if not documents:
        raise SystemExit("No root Markdown documents found")

    errors: list[str] = []
    for path in documents:
        text = path.read_text(encoding="utf-8")
        if not text.strip():
            errors.append(f"{path.name}: empty document")
        for number, line in enumerate(text.splitlines(), start=1):
            if line.rstrip() != line:
                errors.append(f"{path.name}:{number}: trailing whitespace")
        for target in LINK.findall(text):
            destination = target.split(maxsplit=1)[0].strip("<>")
            if not destination:
                errors.append(f"{path.name}: empty Markdown link")
            if destination.startswith("http://"):
                errors.append(f"{path.name}: external link must use HTTPS: {destination}")
        for label, pattern in SECRET_PATTERNS.items():
            if pattern.search(text):
                errors.append(f"{path.name}: possible {label}")

    if errors:
        raise SystemExit("\n".join(errors))
    print(f"Validated {len(documents)} Markdown documents.")


if __name__ == "__main__":
    main()
