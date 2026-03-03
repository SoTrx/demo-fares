from os import getenv

from kiota_abstractions.authentication.anonymous_authentication_provider import (
    AnonymousAuthenticationProvider,
)
from kiota_http.httpx_request_adapter import HttpxRequestAdapter
from kiota_serialization_json.json_serialization_writer import JsonSerializationWriter

from generated.ap_executor.ap_executor_client import ApExecutorClient
from generated.ap_executor.models.execution_result import ExecutionResult
from generated.ap_management.ap_management_client import ApManagementClient
from generated.ap_management.models.resolve_ap_request import ResolveApRequest
from generated.ap_management.models.resolve_ap_response import ResolveApResponse

AP_MANAGEMENT_URL = getenv("AP_MANAGEMENT_URL", "http://ap-management:5000")
AP_EXECUTOR_URL = getenv("AP_EXECUTOR_URL", "http://ap-executor:5000")


def _create_adapter(base_url: str) -> HttpxRequestAdapter:
    adapter = HttpxRequestAdapter(AnonymousAuthenticationProvider())
    adapter.base_url = base_url
    return adapter


def get_management_client() -> ApManagementClient:
    return ApManagementClient(_create_adapter(AP_MANAGEMENT_URL))


def get_executor_client() -> ApExecutorClient:
    return ApExecutorClient(_create_adapter(AP_EXECUTOR_URL))


async def resolve_ap(query: str) -> ResolveApResponse:
    client = get_management_client()
    return await client.api.v1.aps.resolve.post(
        ResolveApRequest(query=query)
    )


async def execute_ap(data: ResolveApResponse) -> ExecutionResult:
    client = get_executor_client()
    return await client.api.v1.execute.post(body=data.ap)


def serialize(model) -> dict:
    writer = JsonSerializationWriter()
    model.serialize(writer)
    return writer.get_serialized_content().decode("utf-8")
