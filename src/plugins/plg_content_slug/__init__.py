from __future__ import annotations

import re
import unicodedata
from typing import TYPE_CHECKING

from src.core.hooks import hooks

if TYPE_CHECKING:
    from src.core.registry import ComponentRegistry

_INVALID_RE = re.compile(r"[^a-z0-9\s-]")
_SEPARATOR_RE = re.compile(r"[\s_-]+")


def _slugify(text: str) -> str:
    normalized = unicodedata.normalize("NFKD", text)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii")
    cleaned = _INVALID_RE.sub("", ascii_text.lower().strip())
    return _SEPARATOR_RE.sub("-", cleaned).strip("-")


async def ensure_article_slug(*, article: object, db: object | None = None, **_: object) -> None:
    current = str(getattr(article, "slug", "") or "").strip()
    if current:
        return
    title = str(getattr(article, "title", "") or "").strip()
    if not title:
        return
    setattr(article, "slug", _slugify(title))
    if db is not None and hasattr(db, "commit"):
        await db.commit()


def setup(registry: "ComponentRegistry") -> None:
    hooks.on("content.article.saved", ensure_article_slug)
