from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .operator_result_error import OperatorResult_error
    from .operator_result_rows_affected import OperatorResult_rows_affected
    from .operator_status import OperatorStatus

@dataclass
class OperatorResult(AdditionalDataHolder, Parsable):
    """
    Result of executing a single AP operator.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The error property
    error: Optional[OperatorResult_error] = None
    # The operator_id property
    operator_id: Optional[str] = None
    # The operator_labels property
    operator_labels: Optional[list[str]] = None
    # The operator_name property
    operator_name: Optional[str] = None
    # The rows_affected property
    rows_affected: Optional[OperatorResult_rows_affected] = None
    # Status of a single operator execution.
    status: Optional[OperatorStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OperatorResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OperatorResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OperatorResult()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .operator_result_error import OperatorResult_error
        from .operator_result_rows_affected import OperatorResult_rows_affected
        from .operator_status import OperatorStatus

        from .operator_result_error import OperatorResult_error
        from .operator_result_rows_affected import OperatorResult_rows_affected
        from .operator_status import OperatorStatus

        fields: dict[str, Callable[[Any], None]] = {
            "error": lambda n : setattr(self, 'error', n.get_object_value(OperatorResult_error)),
            "operator_id": lambda n : setattr(self, 'operator_id', n.get_str_value()),
            "operator_labels": lambda n : setattr(self, 'operator_labels', n.get_collection_of_primitive_values(str)),
            "operator_name": lambda n : setattr(self, 'operator_name', n.get_str_value()),
            "rows_affected": lambda n : setattr(self, 'rows_affected', n.get_object_value(OperatorResult_rows_affected)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(OperatorStatus)),
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
        writer.write_object_value("error", self.error)
        writer.write_str_value("operator_id", self.operator_id)
        writer.write_collection_of_primitive_values("operator_labels", self.operator_labels)
        writer.write_str_value("operator_name", self.operator_name)
        writer.write_object_value("rows_affected", self.rows_affected)
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

