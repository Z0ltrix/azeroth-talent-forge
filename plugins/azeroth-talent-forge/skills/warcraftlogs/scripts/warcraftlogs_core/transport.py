"""GraphQL document loading and HTTP transport foundation."""

from ._legacy import GRAPHQL_URL, WarcraftLogsClient, load_query, make_envelope, sanitize_graphql_errors

__all__ = ["GRAPHQL_URL", "WarcraftLogsClient", "load_query", "make_envelope", "sanitize_graphql_errors"]
