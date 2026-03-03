from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.default_query_parameters import QueryParameters
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from ....models.analytical_pattern import AnalyticalPattern
    from ....models.ap_search_result import ApSearchResult
    from ....models.create_payload import CreatePayload
    from ....models.h_t_t_p_validation_error import HTTPValidationError

class EmptyPathSegmentRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/aps/
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new EmptyPathSegmentRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/aps/?q={q}{&top_k*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[EmptyPathSegmentRequestBuilderGetQueryParameters]] = None) -> Optional[list[ApSearchResult]]:
        """
        Search Analytical Patterns using semantic similarity
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[list[ApSearchResult]]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.h_t_t_p_validation_error import HTTPValidationError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "422": HTTPValidationError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.ap_search_result import ApSearchResult

        return await self.request_adapter.send_collection_async(request_info, ApSearchResult, error_mapping)
    
    async def post(self,body: AnalyticalPattern, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[CreatePayload]:
        """
        Registers a new Analytical Pattern
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CreatePayload]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ....models.h_t_t_p_validation_error import HTTPValidationError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "422": HTTPValidationError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.create_payload import CreatePayload

        return await self.request_adapter.send_async(request_info, CreatePayload, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[EmptyPathSegmentRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Search Analytical Patterns using semantic similarity
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: AnalyticalPattern, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Registers a new Analytical Pattern
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, '{+baseurl}/api/v1/aps/', self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> EmptyPathSegmentRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: EmptyPathSegmentRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return EmptyPathSegmentRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class EmptyPathSegmentRequestBuilderGetQueryParameters():
        """
        Search Analytical Patterns using semantic similarity
        """
        # Natural language query matched against AP descriptions via vector similarity
        q: Optional[str] = None

        # Maximum number of results to return
        top_k: Optional[int] = None

    
    @dataclass
    class EmptyPathSegmentRequestBuilderGetRequestConfiguration(RequestConfiguration[EmptyPathSegmentRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class EmptyPathSegmentRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

