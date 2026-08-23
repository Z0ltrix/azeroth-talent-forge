"""Stable talents error codes and JSON-safe exceptions."""

from __future__ import annotations


class TalentError(RuntimeError):
    def __init__(self, code: str, message: str, **details):
        super().__init__(message)
        self.code = code
        self.message = message
        self.details = details

    def as_dict(self) -> dict:
        return {"code": self.code, "message": self.message, "details": self.details}
