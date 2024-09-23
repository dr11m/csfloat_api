import aiohttp
from .models.listing import Listing
from .models.buy_orders import BuyOrders
from .models.me import Me
from typing import Iterable, Union, Optional

__all__ = "Client"

_API_URL = 'https://csfloat.com/api/v1'


class Client:
    _SUPPORTED_METHODS = ['GET', 'POST']
    ERROR_MESSAGES = {
        401: 'Unauthorized -- Your API key is wrong.',
        403: 'Forbidden -- The requested resource is hidden for administrators only.',
        404: 'Not Found -- The specified resource could not be found.',
        405: 'Method Not Allowed -- You tried to access a resource with an invalid method.',
        406: 'Not Acceptable -- You requested a format that isn\'t json.',
        410: 'Gone -- The requested resource has been removed from our servers.',
        418: 'I\'m a teapot.',
        429: 'Too Many Requests -- You\'re requesting too many resources! Slow down!',
        500: 'Internal Server Error -- We had a problem with our server. Try again later.',
        503: 'Service Unavailable -- We\'re temporarily offline for maintenance. Please try again later.',
    }

    __slots__ = (
        "API_KEY",
        "_headers"
    )

    def __init__(self, api_key: str) -> None:
        self.API_KEY = api_key
        self._headers = {
            'Authorization': self.API_KEY
        }

    async def _request(self, method: str, parameters: str, json_data=None) -> Optional[dict]:
        if method not in self._SUPPORTED_METHODS:
            raise ValueError('Unsupported HTTP method.')

        url = f'{_API_URL}{parameters}'

        async with aiohttp.ClientSession(headers=self._headers) as session:
            async with session.request(method=method, url=url, ssl=False, json=json_data) as response:
                if response.status in self.ERROR_MESSAGES:
                    raise Exception(self.ERROR_MESSAGES[response.status])
                if response.status != 200:
                    raise Exception(f'Error: {response.status}')
                if response.content_type != 'application/json':
                    raise Exception(f"Expected JSON, got {response.content_type}")

                return await response.json()

    def _validate_category(self, category: int) -> None:
        if category not in (0, 1, 2, 3):
            raise ValueError(f'Unknown category parameter "{category}"')

    def _validate_sort_by(self, sort_by: str) -> None:
        valid_sort_by = (
            'lowest_price', 'highest_price', 'most_recent', 'expires_soon',
            'lowest_float', 'highest_float', 'best_deal', 'highest_discount',
            'float_rank', 'num_bids'
        )
        if sort_by not in valid_sort_by:
            raise ValueError(f'Unknown sort_by parameter "{sort_by}"')

    def _validate_type(self, type_: str) -> None:
        if type_ not in ('buy_now', 'auction'):
            raise ValueError(f'Unknown type parameter "{type_}"')

    async def get_exchange_rates(self) -> Optional[dict]:
        parameters = "/meta/exchange-rates"
        method = "GET"

        response = await self._request(method=method, parameters=parameters)
        return response

    async def get_me(self, *, raw_response: bool = False) -> Optional[Me]:
        parameters = "/me"
        method = "GET"

        response = await self._request(method=method, parameters=parameters)

        if raw_response:
            return response

        return Me(data=response)

    async def get_location(self) -> Optional[dict]:
        parameters = "/meta/location"
        method = "GET"

        response = await self._request(method=method, parameters=parameters)
        return response

    async def get_pending_trades(
            self, limit: int = 500, page: int = 0
    ) -> Optional[dict]:
        parameters = f"/me/trades?state=pending&limit={limit}&page={page}"
        method = "GET"

        response = await self._request(method=method, parameters=parameters)
        return response

    async def get_similar(
            self, *, listing_id: int, raw_response: bool = False
    ) -> Union[Iterable[Listing], dict]:
        parameters = f"/listings/{listing_id}/similar"
        method = "GET"

        response = await self._request(method=method, parameters=parameters)

        if raw_response:
            return response

        listings = [
            Listing(data=item) for item in response
        ]

        return listings

    async def get_buy_orders(
            self, *, listing_id: int, limit: int = 10, raw_response: bool = False
    ) -> Optional[list[BuyOrders]]:
        parameters = f"/listings/{listing_id}/buy-orders?limit={limit}"
        method = "GET"

        response = await self._request(method=method, parameters=parameters)

        if raw_response:
            return response

        listings = [
            BuyOrders(data=item) for item in response
        ]

        return listings

    async def get_all_listings(
            self,
            *,
            min_price: Optional[int] = None,
            max_price: Optional[int] = None,
            page: int = 0,
            limit: int = 50,
            sort_by: str = 'best_deal',
            category: int = 0,
            def_index: Optional[Union[int, Iterable[int]]] = None,
            min_float: Optional[float] = None,
            max_float: Optional[float] = None,
            rarity: Optional[str] = None,
            paint_seed: Optional[int] = None,
            paint_index: Optional[int] = None,
            user_id: Optional[str] = None,
            collection: Optional[str] = None,
            market_hash_name: Optional[str] = None,
            type_: str = 'buy_now',
            raw_response: bool = False
    ) -> Union[Iterable[Listing], dict]:
        """
        :param min_price: Only include listings have a price higher than this (in cents)
        :param max_price: Only include listings have a price lower than this (in cents)
        :param page: Which page of listings to start from
        :param limit: How many listings to return. Max of 50
        :param sort_by: How to order the listings
        :param category: Can be one of: 0 = any, 1 = normal, 2 = stattrak, 3 = souvenir
        :param def_index: Only include listings that have one of the given def index(es)
        :param min_float: Only include listings that have a float higher than this
        :param max_float: Only include listings that have a float lower than this
        :param rarity: Only include listings that have this rarity
        :param paint_seed: Only include listings that have this paint seed
        :param paint_index: Only include listings that have this paint index
        :param user_id: Only include listings from this SteamID64
        :param collection: Only include listings from this collection
        :param market_hash_name: Only include listings that have this market hash name
        :param type_: Either buy_now or auction
        :param raw_response: Returns the raw response from the API
        :return:
        """
        self._validate_category(category)
        self._validate_sort_by(sort_by)
        self._validate_type(type_)

        parameters = (
            f'/listings?page={page}&limit={limit}&sort_by={sort_by}'
            f'&category={category}&type={type_}'
        )

        if min_price is not None:
            parameters += f'&min_price={min_price}'
        if max_price is not None:
            parameters += f'&max_price={max_price}'
        if def_index is not None:
            if isinstance(def_index, Iterable):
                def_index = ','.join(map(str, def_index))
            parameters += f'&def_index={def_index}'
        if min_float is not None:
            parameters += f'&min_float={min_float}'
        if max_float is not None:
            parameters += f'&max_float={max_float}'
        if rarity is not None:
            parameters += f'&rarity={rarity}'
        if paint_seed is not None:
            parameters += f'&paint_seed={paint_seed}'
        if paint_index is not None:
            parameters += f'&paint_index={paint_index}'
        if user_id is not None:
            parameters += f'&user_id={user_id}'
        if collection is not None:
            parameters += f'&collection={collection}'
        if market_hash_name is not None:
            parameters += f'&market_hash_name={market_hash_name}'

        method = 'GET'

        response = await self._request(method=method, parameters=parameters)

        if raw_response:
            return response

        listings = [
            Listing(data=item) for item in response
        ]

        return listings

    async def get_specific_listing(
            self, listing_id: int, *, raw_response: bool = False
    ) -> Union[Listing, dict]:
        parameters = f'/listings/{listing_id}'
        method = 'GET'

        response = await self._request(method=method, parameters=parameters)

        if raw_response:
            return response

        return Listing(data=response)

    async def create_listing(
        self,
        *,
        asset_id: str,
        price: float,
        type_: str = "buy_now",
        max_offer_discount: Optional[int] = None,
        reserve_price: Optional[float] = None,
        duration_days: Optional[int] = None,
        description: str = "",
        private: bool = False,
    ) -> Optional[dict]:
        """
        :param asset_id: The ID of the item to list
        :param price: The buy_now price or the current bid or reserve price on an auction
        :param type_: Either 'buy_now' or 'auction' (default: 'buy_now')
        :param max_offer_discount: The max discount for an offer (optional)
        :param reserve_price: The starting price for an auction (required if type is 'auction')
        :param duration_days: The auction duration in days (required if type is 'auction')
        :param description: User-defined description (optional)
        :param private: If true, will hide the listing from public searches (optional)
        :return: The response from the API
        """
        self._validate_type(type_)

        parameters = "/listings"
        method = "POST"

        json_data = {
            "asset_id": asset_id,
            "price": price,
            "type": type_,
            "description": description,
            "private": private
        }

        # Add optional parameters if provided
        if max_offer_discount is not None:
            json_data["max_offer_discount"] = max_offer_discount
        if reserve_price is not None:
            json_data["reserve_price"] = reserve_price
        if duration_days is not None:
            json_data["duration_days"] = duration_days

        response = await self._request(method=method, parameters=parameters, json_data=json_data)
        return response

    async def make_offer(
            self, *, listing_id: int, price: int
    ) -> Optional[dict]:
        parameters = "/offers"
        method = "POST"
        json_data = {
            "contract_id": str(listing_id),
            "price": price,
            "cancel_previous_offer": False
        }
        response = await self._request(method=method, parameters=parameters, json_data=json_data)
        return response
