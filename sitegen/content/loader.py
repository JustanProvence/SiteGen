from pathlib import Path


def load_page(path: Path | str) -> str:
    """Read and return the raw markdown content of a page file."""
    return Path(path).read_text(encoding="utf-8")
