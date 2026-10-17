"""Backend entry points. The frontend imports ONLY this module (via app/api.py).

Owner: P1. Signatures are frozen with core/contracts.py. Each function is
implemented as the pieces land; until then it raises NotImplementedError, and
the frontend uses app/mock_service.py (USE_MOCK_SERVICE=1).
"""
from __future__ import annotations

from core.contracts import (
    DeviceResult,
    LLMStatus,
    MappingIn,
    MappingSuggestion,
    UnmappedLine,
    UploadedFile,
)


def list_frameworks() -> list[str]:
    raise NotImplementedError


def audit_files(files: list[UploadedFile], framework: str) -> list[DeviceResult]:
    raise NotImplementedError


def get_review_queue(device_id: str) -> list[UnmappedLine]:
    raise NotImplementedError


def suggest_mapping(line: UnmappedLine) -> MappingSuggestion:
    raise NotImplementedError


def save_mapping(mapping: MappingIn) -> None:
    raise NotImplementedError


def reaudit(device_ids: list[str], framework: str) -> list[DeviceResult]:
    raise NotImplementedError


def generate_report(device_id: str) -> bytes:
    raise NotImplementedError


def llm_status() -> LLMStatus:
    from core.llm.client import LLMClient

    return LLMStatus(**LLMClient().status())
