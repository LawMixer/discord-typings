from __future__ import annotations

from typing import List

from typing_extensions import NotRequired, TypedDict, final

from .resources.application import ApplicationData
from .resources.user import UserData

__all__ = ('AccessTokenResponseData', 'AuthorizationInformationData')


# https://discord.com/developers/docs/topics/oauth2#authorization-code-grant-access-token-response


@final
class AccessTokenResponseData(TypedDict):
    access_token: str
    token_type: str
    expires_in: int
    refresh_token: str
    scope: str


# https://discord.com/developers/docs/topics/oauth2#get-current-authorization-information


@final
class AuthorizationInformationData(TypedDict):
    application: ApplicationData
    scopes: List[str]
    user: NotRequired[UserData]
    expires: str