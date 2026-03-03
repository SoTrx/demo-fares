from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .execution_result_ap_name import ExecutionResult_ap_name
    from .execution_result_error import ExecutionResult_error
    from .execution_status import ExecutionStatus
    from .operator_result import OperatorResult

@dataclass
class ExecutionResult(AdditionalDataHolder, Parsable):
    """
    Full result of executing an Analytical Pattern.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The ap_name property
    ap_name: Optional[ExecutionResult_ap_name] = None
    # The database_name property
    database_name: Optional[str] = None
    # The error property
    error: Optional[ExecutionResult_error] = None
    # The operators property
    operators: Optional[list[OperatorResult]] = None
    # The schema_name property
    schema_name: Optional[str] = None
    # Overall status of the AP execution.
    status: Optional[ExecutionStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ExecutionResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ExecutionResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ExecutionResult()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .execution_result_ap_name import ExecutionResult_ap_name
        from .execution_result_error import ExecutionResult_error
        from .execution_status import ExecutionStatus
        from .operator_result import OperatorResult

        from .execution_result_ap_name import ExecutionResult_ap_name
        from .execution_result_error import ExecutionResult_error
        from .execution_status import ExecutionStatus
        from .operator_result import OperatorResult

        fields: dict[str, Callable[[Any], None]] = {
            "ap_name": lambda n : setattr(self, 'ap_name', n.get_object_value(ExecutionResult_ap_name)),
            "database_name": lambda n : setattr(self, 'database_name', n.get_str_value()),
            "error": lambda n : setattr(self, 'error', n.get_object_value(ExecutionResult_error)),
            "operators": lambda n : setattr(self, 'operators', n.get_collection_of_object_values(OperatorResult)),
            "schema_name": lambda n : setattr(self, 'schema_name', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(ExecutionStatus)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("ap_name", self.ap_name)
        writer.write_str_value("database_name", self.database_name)
        writer.write_object_value("error", self.error)
        writer.write_collection_of_object_values("operators", self.operators)
        writer.write_str_value("schema_name", self.schema_name)
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

