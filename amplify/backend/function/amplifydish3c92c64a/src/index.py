import json
from client_graphql.index import execute_query
from client_graphql.query import listProjects
from client_graphql.client_graphql_exception import ClientGraphqlException
from gql.transport.exceptions import TransportQueryError
import os
import asyncio

def HttpResponse(status, body):
  return {
      'statusCode': status,
      'headers': {
          'Access-Control-Allow-Headers': '*',
          'Access-Control-Allow-Origin': '*',
          'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
      },
      'body': json.dumps(body)
  } 

async def query():
    
    try:
        endpoint = os.getenv('API_AMPLIFYDISH_GRAPHQLAPIENDPOINTOUTPUT')
        api_key = os.getenv('API_AMPLIFYDISH_GRAPHQLAPIKEYOUTPUT')
        return await execute_query(
            listProjects(),
            {},
            endpoint,
            api_key
        )

    except Exception as e:
        raise ClientGraphqlException(str(e.args))

    except TransportQueryError as e:
        raise ClientGraphqlException(str(e.args))
    
async def main(event):
    print('received event:')
    print(event)


    result = await query()
    # return await is_valid_signature_stripe(result,event)
    return HttpResponse(200,{})   

def handler(event, context):
    # Handle the event
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(main(event)) 