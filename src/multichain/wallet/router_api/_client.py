# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Body,
    Omit,
    Query,
    Headers,
    Timeout,
    NoneType,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
    make_request_options,
)

if TYPE_CHECKING:
    from .resources import evm, health, solana, wallet, bitcoin
    from .resources.health import HealthResource, AsyncHealthResource
    from .resources.wallet import WalletResource, AsyncWalletResource
    from .resources.evm.evm import EvmResource, AsyncEvmResource
    from .resources.solana.solana import SolanaResource, AsyncSolanaResource
    from .resources.bitcoin.bitcoin import BitcoinResource, AsyncBitcoinResource

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "MultichainWalletRouterAPI",
    "AsyncMultichainWalletRouterAPI",
    "Client",
    "AsyncClient",
]


class MultichainWalletRouterAPI(SyncAPIClient):
    # client options
    api_key: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous MultichainWalletRouterAPI client instance.

        This automatically infers the `api_key` argument from the `MULTICHAIN_WALLET_ROUTER_API_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("MULTICHAIN_WALLET_ROUTER_API_API_KEY")
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("MULTICHAIN_WALLET_ROUTER_API_BASE_URL")
        if base_url is None:
            base_url = f"https://wallet.api-router.paxeer.app/api"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def health(self) -> HealthResource:
        from .resources.health import HealthResource

        return HealthResource(self)

    @cached_property
    def wallet(self) -> WalletResource:
        from .resources.wallet import WalletResource

        return WalletResource(self)

    @cached_property
    def evm(self) -> EvmResource:
        from .resources.evm import EvmResource

        return EvmResource(self)

    @cached_property
    def solana(self) -> SolanaResource:
        from .resources.solana import SolanaResource

        return SolanaResource(self)

    @cached_property
    def bitcoin(self) -> BitcoinResource:
        from .resources.bitcoin import BitcoinResource

        return BitcoinResource(self)

    @cached_property
    def with_raw_response(self) -> MultichainWalletRouterAPIWithRawResponse:
        return MultichainWalletRouterAPIWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MultichainWalletRouterAPIWithStreamedResponse:
        return MultichainWalletRouterAPIWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if headers.get("Authorization") or isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected the api_key to be set. Or for the `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    def get_info(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """API info and supported chains"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self.get(
            "/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncMultichainWalletRouterAPI(AsyncAPIClient):
    # client options
    api_key: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncMultichainWalletRouterAPI client instance.

        This automatically infers the `api_key` argument from the `MULTICHAIN_WALLET_ROUTER_API_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("MULTICHAIN_WALLET_ROUTER_API_API_KEY")
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("MULTICHAIN_WALLET_ROUTER_API_BASE_URL")
        if base_url is None:
            base_url = f"https://wallet.api-router.paxeer.app/api"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def health(self) -> AsyncHealthResource:
        from .resources.health import AsyncHealthResource

        return AsyncHealthResource(self)

    @cached_property
    def wallet(self) -> AsyncWalletResource:
        from .resources.wallet import AsyncWalletResource

        return AsyncWalletResource(self)

    @cached_property
    def evm(self) -> AsyncEvmResource:
        from .resources.evm import AsyncEvmResource

        return AsyncEvmResource(self)

    @cached_property
    def solana(self) -> AsyncSolanaResource:
        from .resources.solana import AsyncSolanaResource

        return AsyncSolanaResource(self)

    @cached_property
    def bitcoin(self) -> AsyncBitcoinResource:
        from .resources.bitcoin import AsyncBitcoinResource

        return AsyncBitcoinResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncMultichainWalletRouterAPIWithRawResponse:
        return AsyncMultichainWalletRouterAPIWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMultichainWalletRouterAPIWithStreamedResponse:
        return AsyncMultichainWalletRouterAPIWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if headers.get("Authorization") or isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected the api_key to be set. Or for the `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    async def get_info(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """API info and supported chains"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self.get(
            "/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class MultichainWalletRouterAPIWithRawResponse:
    _client: MultichainWalletRouterAPI

    def __init__(self, client: MultichainWalletRouterAPI) -> None:
        self._client = client

        self.get_info = to_raw_response_wrapper(
            client.get_info,
        )

    @cached_property
    def health(self) -> health.HealthResourceWithRawResponse:
        from .resources.health import HealthResourceWithRawResponse

        return HealthResourceWithRawResponse(self._client.health)

    @cached_property
    def wallet(self) -> wallet.WalletResourceWithRawResponse:
        from .resources.wallet import WalletResourceWithRawResponse

        return WalletResourceWithRawResponse(self._client.wallet)

    @cached_property
    def evm(self) -> evm.EvmResourceWithRawResponse:
        from .resources.evm import EvmResourceWithRawResponse

        return EvmResourceWithRawResponse(self._client.evm)

    @cached_property
    def solana(self) -> solana.SolanaResourceWithRawResponse:
        from .resources.solana import SolanaResourceWithRawResponse

        return SolanaResourceWithRawResponse(self._client.solana)

    @cached_property
    def bitcoin(self) -> bitcoin.BitcoinResourceWithRawResponse:
        from .resources.bitcoin import BitcoinResourceWithRawResponse

        return BitcoinResourceWithRawResponse(self._client.bitcoin)


class AsyncMultichainWalletRouterAPIWithRawResponse:
    _client: AsyncMultichainWalletRouterAPI

    def __init__(self, client: AsyncMultichainWalletRouterAPI) -> None:
        self._client = client

        self.get_info = async_to_raw_response_wrapper(
            client.get_info,
        )

    @cached_property
    def health(self) -> health.AsyncHealthResourceWithRawResponse:
        from .resources.health import AsyncHealthResourceWithRawResponse

        return AsyncHealthResourceWithRawResponse(self._client.health)

    @cached_property
    def wallet(self) -> wallet.AsyncWalletResourceWithRawResponse:
        from .resources.wallet import AsyncWalletResourceWithRawResponse

        return AsyncWalletResourceWithRawResponse(self._client.wallet)

    @cached_property
    def evm(self) -> evm.AsyncEvmResourceWithRawResponse:
        from .resources.evm import AsyncEvmResourceWithRawResponse

        return AsyncEvmResourceWithRawResponse(self._client.evm)

    @cached_property
    def solana(self) -> solana.AsyncSolanaResourceWithRawResponse:
        from .resources.solana import AsyncSolanaResourceWithRawResponse

        return AsyncSolanaResourceWithRawResponse(self._client.solana)

    @cached_property
    def bitcoin(self) -> bitcoin.AsyncBitcoinResourceWithRawResponse:
        from .resources.bitcoin import AsyncBitcoinResourceWithRawResponse

        return AsyncBitcoinResourceWithRawResponse(self._client.bitcoin)


class MultichainWalletRouterAPIWithStreamedResponse:
    _client: MultichainWalletRouterAPI

    def __init__(self, client: MultichainWalletRouterAPI) -> None:
        self._client = client

        self.get_info = to_streamed_response_wrapper(
            client.get_info,
        )

    @cached_property
    def health(self) -> health.HealthResourceWithStreamingResponse:
        from .resources.health import HealthResourceWithStreamingResponse

        return HealthResourceWithStreamingResponse(self._client.health)

    @cached_property
    def wallet(self) -> wallet.WalletResourceWithStreamingResponse:
        from .resources.wallet import WalletResourceWithStreamingResponse

        return WalletResourceWithStreamingResponse(self._client.wallet)

    @cached_property
    def evm(self) -> evm.EvmResourceWithStreamingResponse:
        from .resources.evm import EvmResourceWithStreamingResponse

        return EvmResourceWithStreamingResponse(self._client.evm)

    @cached_property
    def solana(self) -> solana.SolanaResourceWithStreamingResponse:
        from .resources.solana import SolanaResourceWithStreamingResponse

        return SolanaResourceWithStreamingResponse(self._client.solana)

    @cached_property
    def bitcoin(self) -> bitcoin.BitcoinResourceWithStreamingResponse:
        from .resources.bitcoin import BitcoinResourceWithStreamingResponse

        return BitcoinResourceWithStreamingResponse(self._client.bitcoin)


class AsyncMultichainWalletRouterAPIWithStreamedResponse:
    _client: AsyncMultichainWalletRouterAPI

    def __init__(self, client: AsyncMultichainWalletRouterAPI) -> None:
        self._client = client

        self.get_info = async_to_streamed_response_wrapper(
            client.get_info,
        )

    @cached_property
    def health(self) -> health.AsyncHealthResourceWithStreamingResponse:
        from .resources.health import AsyncHealthResourceWithStreamingResponse

        return AsyncHealthResourceWithStreamingResponse(self._client.health)

    @cached_property
    def wallet(self) -> wallet.AsyncWalletResourceWithStreamingResponse:
        from .resources.wallet import AsyncWalletResourceWithStreamingResponse

        return AsyncWalletResourceWithStreamingResponse(self._client.wallet)

    @cached_property
    def evm(self) -> evm.AsyncEvmResourceWithStreamingResponse:
        from .resources.evm import AsyncEvmResourceWithStreamingResponse

        return AsyncEvmResourceWithStreamingResponse(self._client.evm)

    @cached_property
    def solana(self) -> solana.AsyncSolanaResourceWithStreamingResponse:
        from .resources.solana import AsyncSolanaResourceWithStreamingResponse

        return AsyncSolanaResourceWithStreamingResponse(self._client.solana)

    @cached_property
    def bitcoin(self) -> bitcoin.AsyncBitcoinResourceWithStreamingResponse:
        from .resources.bitcoin import AsyncBitcoinResourceWithStreamingResponse

        return AsyncBitcoinResourceWithStreamingResponse(self._client.bitcoin)


Client = MultichainWalletRouterAPI

AsyncClient = AsyncMultichainWalletRouterAPI
