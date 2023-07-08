from typing import List, Optional

from typing_extensions import NotRequired, TypedDict

import discord_typings

__all__ = (
    'ApplicationData',
    'InstallParams',
    'TeamData',
    'TeamMemberData',
)


# https://discord.com/developers/docs/resources/application#application-object-application-structure


class ApplicationData(TypedDict):
    id: 'discord_typings.Snowflake'
    name: str
    icon: Optional[str]
    description: str
    rpc_origins: NotRequired[List[str]]
    bot_public: bool
    bot_require_code_grant: bool
    terms_of_service_url: NotRequired[str]
    privacy_policy_url: NotRequired[str]
    owner: NotRequired['discord_typings.UserData']
    verify_key: str
    team: Optional['discord_typings.TeamData']
    guild_id: NotRequired['discord_typings.Snowflake']
    primary_sku_id: NotRequired['discord_typings.Snowflake']
    slug: NotRequired[str]
    cover_image: NotRequired[str]
    flags: NotRequired[int]
    tags: NotRequired[List[str]]
    install_params: NotRequired['discord_typings.InstallParams']
    custom_install_url: NotRequired[str]
    role_connections_verification_url: NotRequired[str]


# https://discord.com/developers/docs/resources/application#install-params-object-install-params-structure


class InstallParams(TypedDict):
    scopes: List['discord_typings.OAuth2Scopes']
    permissions: str


# https://discord.com/developers/docs/topics/teams#data-models-team-object


class TeamData(TypedDict):
    icon: Optional[str]
    id: 'discord_typings.Snowflake'
    members: List['discord_typings.TeamMemberData']
    name: str
    owner_user_id: 'discord_typings.Snowflake'


# https://discord.com/developers/docs/topics/teams#data-models-team-member-object


class TeamMemberData(TypedDict):
    membership_state: int
    permissions: List[str]
    team_id: 'discord_typings.Snowflake'
    user: 'discord_typings.UserData'
