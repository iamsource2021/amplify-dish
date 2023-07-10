from urllib.parse import urlparse
import asyncio
from gql import Client
from gql.transport.aiohttp import AIOHTTPTransport
from gql.transport.appsync_auth import AppSyncApiKeyAuthentication
from client_graphql.client_graphql_exception import ClientGraphqlException

async def execute_query(query,variables,endpoint,api_key):
  if not endpoint or not api_key:
    raise ClientGraphqlException("Missing environment variables")

  host = str(urlparse(endpoint).netloc)
  auth = AppSyncApiKeyAuthentication(host=host, api_key=api_key)
  transport = AIOHTTPTransport(url=endpoint, auth=auth)

  async with Client(transport=transport, fetch_schema_from_transport=False,) as session:
    return await session.execute(query, variable_values={"input":variables})


async def execute_query_by_param(query,param,endpoint,api_key):
  if not endpoint or not api_key:
    raise ClientGraphqlException("Missing environment variables")

  host = str(urlparse(endpoint).netloc)
  auth = AppSyncApiKeyAuthentication(host=host, api_key=api_key)
  transport = AIOHTTPTransport(url=endpoint, auth=auth)

  async with Client(transport=transport, fetch_schema_from_transport=False,) as session:
    return await session.execute(query, variable_values=param)    