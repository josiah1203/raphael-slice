"""API routes for raphael-slice."""

from __future__ import annotations

from fastapi import APIRouter

router = APIRouter(tags=["raphael-slice"])


@router.get("")
def list_root() -> dict[str, str]:
  return {"service": "raphael-slice", "status": "stub"}
