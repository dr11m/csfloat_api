from typing import Dict, Any, Optional
from .statistics import Statistics


class Seller:
    __slots__ = (
        "_avatar",
        "_away",
        "_flags",
        "_has_valid_steam_api_key",
        "_obfuscated_id",
        "_online",
        "_stall_public",
        "_statistics",
        "_steam_id",
        "_username",
        "_verification_mode"
    )

    def __init__(self, *, data: Dict[str, Any]):
        self._avatar = data.get("avatar")
        self._away = data.get("away")
        self._flags = data.get("flags")
        self._has_valid_steam_api_key = data.get("has_valid_steam_api_key")
        self._obfuscated_id = data.get("obfuscated_id")
        self._online = data.get("online")
        self._stall_public = data.get("stall_public")
        self._statistics = data.get("statistics")
        self._steam_id = data.get("steam_id")
        self._username = data.get("username")
        self._verification_mode = data.get("verification_mode")

    @property
    def avatar(self) -> Optional[str]:
        return self._avatar

    @property
    def away(self) -> Optional[bool]:
        return self._away

    @property
    def flags(self) -> Optional[int]:
        return self._flags

    @property
    def has_valid_steam_api_key(self) -> Optional[bool]:
        return self._has_valid_steam_api_key

    @property
    def obfuscated_id(self) -> Optional[int]:
        return self._obfuscated_id

    @property
    def online(self) -> Optional[bool]:
        return self._online

    @property
    def stall_public(self) -> Optional[bool]:
        return self._stall_public

    @property
    def statistics(self) -> Optional[Statistics]:
        return Statistics(data=self._statistics)

    @property
    def steam_id(self) -> Optional[int]:
        return self._steam_id

    @property
    def username(self) -> Optional[str]:
        return self._username

    @property
    def verification_mode(self) -> Optional[str]:
        return self._verification_mode
