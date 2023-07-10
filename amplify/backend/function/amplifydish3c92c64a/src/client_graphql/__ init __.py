"""
ioos_pkg_skeleton is not a real package, just a set of best practices examples.
"""

from client_graphql.index import execute_query
from client_graphql.query import listProjects
from client_graphql.client_graphql_exception import ClientGraphqlException

__all__ = [
    "execute_query",
    "listProjects",
    "ClientGraphqlException"
]