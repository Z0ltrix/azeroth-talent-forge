"""Stable foundational types and public errors used by the CLI."""

from ._legacy import (ApiError, AuthenticationError, Credentials, DiscoveryFilters,
                      PartialGraphQLError, PublicReportError, ReportReference)

__all__ = ["ApiError", "AuthenticationError", "Credentials", "DiscoveryFilters",
           "PartialGraphQLError", "PublicReportError", "ReportReference"]
