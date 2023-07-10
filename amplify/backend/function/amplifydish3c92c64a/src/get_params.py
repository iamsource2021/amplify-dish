from aiobotocore.session import get_session
import asyncio
import os


async def get_params_from_ssm(path):
    session = get_session()
    async with session.create_client("ssm") as client:
        next_token = ''
        while True:
            response = await client.get_parameters_by_path(Path=path, Recursive=True, WithDecryption=True, NextToken=next_token)

            for param in response['Parameters']:
                key = get_variable_name(param['Name'])
                os.environ[key] = param['Value']

            if 'NextToken' not in response:
                break

            next_token = response['NextToken']


def get_variable_name(path):
    parts = path.rsplit('/', 1)
    return parts[-1]