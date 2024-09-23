from typing import Optional, Dict, Any


class Statistics:
    __slots__ = (
        "_total_sales",
        "_total_purchases",
        "_median_trade_time",
        "_total_avoided_trades",
        "_total_failed_trades",
        "_total_verified_trades",
        "_total_trades"
    )

    def __init__(self, *, data: Dict[str, Any]):
        self._total_sales = data.get("total_sales")
        self._total_purchases = data.get("total_purchases")
        self._median_trade_time = data.get("median_trade_time")
        self._total_avoided_trades = data.get("total_avoided_trades")
        self._total_failed_trades = data.get("total_failed_trades")
        self._total_verified_trades = data.get("total_verified_trades")
        self._total_trades = data.get("total_trades")

    @property
    def total_sales(self) -> Optional[int]:
        return self._total_sales

    @property
    def total_purchases(self) -> Optional[int]:
        return self._total_purchases

    @property
    def median_trade_time(self) -> Optional[int]:
        return self._median_trade_time

    @property
    def total_avoided_trades(self) -> Optional[int]:
        return self._total_avoided_trades

    @property
    def total_failed_trades(self) -> Optional[int]:
        return self._total_failed_trades

    @property
    def total_verified_trades(self) -> Optional[int]:
        return self._total_verified_trades

    @property
    def total_trades(self) -> Optional[int]:
        return self._total_trades


class Preferences:
    __slots__ = (
        "_offers_enabled",
        "_max_offer_discount"
    )

    def __init__(self, *, data: Dict[str, Any]):
        self._offers_enabled = data.get("offers_enabled")
        self._max_offer_discount = data.get("max_offer_discount")

    @property
    def offers_enabled(self) -> Optional[bool]:
        return self._offers_enabled

    @property
    def max_offer_discount(self) -> Optional[int]:
        return self._max_offer_discount


class FirebaseMessaging:
    __slots__ = (
        "_platform",
        "_last_updated"
    )

    def __init__(self, *, data: Dict[str, Any]):
        self._platform = data.get("platform")
        self._last_updated = data.get("last_updated")

    @property
    def platform(self) -> Optional[int]:
        return self._platform

    @property
    def last_updated(self) -> Optional[str]:
        return self._last_updated


class User:
    __slots__ = (
        "_steam_id",
        "_username",
        "_flags",
        "_avatar",
        "_background_url",
        "_email",
        "_balance",
        "_pending_balance",
        "_stall_public",
        "_away",
        "_trade_token",
        "_payment_accounts",
        "_api_key",
        "_statistics",
        "_preferences",
        "_know_your_customer",
        "_extension_setup_at",
        "_firebase_messaging",
        "_stripe_connect",
        "_has_valid_steam_api_key",
        "_obfuscated_id",
        "_online",
        "_fee",
        "_withdraw_fee",
        "_subscriptions",
        "_has_2fa"
    )

    def __init__(self, *, data: Dict[str, Any]):
        self._steam_id = data.get("steam_id")
        self._username = data.get("username")
        self._flags = data.get("flags")
        self._avatar = data.get("avatar")
        self._background_url = data.get("background_url")
        self._email = data.get("email")
        self._balance = data.get("balance")
        self._pending_balance = data.get("pending_balance")
        self._stall_public = data.get("stall_public")
        self._away = data.get("away")
        self._trade_token = data.get("trade_token")
        self._payment_accounts = data.get("payment_accounts")
        self._api_key = data.get("api_key", "")
        self._statistics = data.get("statistics")
        self._preferences = data.get("preferences")
        self._know_your_customer = data.get("know_your_customer")
        self._extension_setup_at = data.get("extension_setup_at")
        self._firebase_messaging = data.get("firebase_messaging")
        self._stripe_connect = data.get("stripe_connect")
        self._has_valid_steam_api_key = data.get("has_valid_steam_api_key")
        self._obfuscated_id = data.get("obfuscated_id")
        self._online = data.get("online")
        self._fee = data.get("fee")
        self._withdraw_fee = data.get("withdraw_fee")
        self._subscriptions = data.get("subscriptions")
        self._has_2fa = data.get("has_2fa")

    @property
    def steam_id(self) -> Optional[str]:
        return self._steam_id

    @property
    def username(self) -> Optional[str]:
        return self._username

    @property
    def flags(self) -> Optional[int]:
        return self._flags

    @property
    def avatar(self) -> Optional[str]:
        return self._avatar

    @property
    def background_url(self) -> Optional[str]:
        return self._background_url

    @property
    def email(self) -> Optional[str]:
        return self._email

    @property
    def balance(self) -> Optional[int]:
        return self._balance

    @property
    def pending_balance(self) -> Optional[int]:
        return self._pending_balance

    @property
    def stall_public(self) -> Optional[bool]:
        return self._stall_public

    @property
    def away(self) -> Optional[bool]:
        return self._away

    @property
    def trade_token(self) -> Optional[str]:
        return self._trade_token

    @property
    def payment_accounts(self) -> Optional[dict]:
        return self._payment_accounts

    @property
    def api_key(self) -> Optional[str]:
        return self._api_key

    @property
    def statistics(self) -> Optional[Statistics]:
        return Statistics(data=self._statistics)

    @property
    def preferences(self) -> Optional[Preferences]:
        return Preferences(data=self._preferences)

    @property
    def know_your_customer(self) -> Optional[str]:
        return self._know_your_customer

    @property
    def extension_setup_at(self) -> Optional[str]:
        return self._extension_setup_at

    @property
    def firebase_messaging(self) -> Optional[FirebaseMessaging]:
        return FirebaseMessaging(data=self._firebase_messaging)

    @property
    def stripe_connect(self) -> Optional[set]:
        return self._stripe_connect

    @property
    def has_valid_steam_api_key(self) -> Optional[bool]:
        return self._has_valid_steam_api_key

    @property
    def obfuscated_id(self) -> Optional[str]:
        return self._obfuscated_id

    @property
    def online(self) -> Optional[bool]:
        return self._online

    @property
    def fee(self) -> Optional[float]:
        return self._fee

    @property
    def withdraw_fee(self) -> Optional[float]:
        return self._withdraw_fee

    @property
    def subscriptions(self) -> Optional[list]:
        return self._subscriptions

    @property
    def has_2fa(self) -> Optional[bool]:
        return self._has_2fa


class Me:
    __slots__ = (
        "_user",
        "_pending_offers",
        "_actionable_trades"
    )

    def __init__(self, *, data: Dict[str, Any]):
        self._user = data.get("user")
        self._pending_offers = data.get("pending_offers")
        self._actionable_trades = data.get("actionable_trades")

    @property
    def user(self) -> Optional[User]:
        return User(data=self._user)

    @property
    def pending_offers(self) -> Optional[int]:
        return self._pending_offers

    @property
    def actionable_trades(self) -> Optional[int]:
        return self._actionable_trades
