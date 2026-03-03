from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .analytical_pattern import AnalyticalPattern
    from .resolve_ap_response_score import ResolveApResponse_score

@dataclass
class ResolveApResponse(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The ap property
    ap: Optional[AnalyticalPattern] = None
    # Cosine similarity score; None when the AP was generated
    score: Optional[ResolveApResponse_score] = None
    # "found" if an existing AP matched, "generated" if a new one was created
    source: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ResolveApResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ResolveApResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ResolveApResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .analytical_pattern import AnalyticalPattern
        from .resolve_ap_response_score import ResolveApResponse_score

        from .analytical_pattern import AnalyticalPattern
        from .resolve_ap_response_score import ResolveApResponse_score

        fields: dict[str, Callable[[Any], None]] = {
            "ap": lambda n : setattr(self, 'ap', n.get_object_value(AnalyticalPattern)),
            "score": lambda n : setattr(self, 'score', n.get_object_value(ResolveApResponse_score)),
            "source": lambda n : setattr(self, 'source', n.get_str_value()),
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
        writer.write_object_value("ap", self.ap)
        writer.write_object_value("score", self.score)
        writer.write_str_value("source", self.source)
        writer.write_additional_data_value(self.additional_data)
    

