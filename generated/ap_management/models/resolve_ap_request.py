from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class ResolveApRequest(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Natural language description of the desired Analytical Pattern
    query: Optional[str] = None
    # Minimum cosine similarity to consider an AP a match
    threshold: Optional[float] = None
    # Number of candidates to retrieve before applying the threshold
    top_k: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ResolveApRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ResolveApRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ResolveApRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "query": lambda n : setattr(self, 'query', n.get_str_value()),
            "threshold": lambda n : setattr(self, 'threshold', n.get_float_value()),
            "top_k": lambda n : setattr(self, 'top_k', n.get_int_value()),
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
        writer.write_str_value("query", self.query)
        writer.write_float_value("threshold", self.threshold)
        writer.write_int_value("top_k", self.top_k)
        writer.write_additional_data_value(self.additional_data)
    

