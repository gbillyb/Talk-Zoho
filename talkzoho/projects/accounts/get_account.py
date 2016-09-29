from talkzoho.regions import US
from talkzoho.projects.get_record import get_record

from talkzoho.projects.accounts import MODULE


async def get_account(*,
                      id,
                      portal_id,
                      auth_token=None,
                      region=US,
                      columns=None):
    return get_record(
        id=id,
        moudle=MODULE,
        portal_id=portal_id,
        auth_token=auth_token,
        region=region,
        columns=columns)