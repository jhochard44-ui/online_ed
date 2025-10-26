"""Schemas for the economics learning platform with optional Pydantic support."""
from __future__ import annotations

from datetime import datetime, time
from typing import List, Optional

try:  # pragma: no cover - exercised implicitly when pydantic is available
    from pydantic import BaseModel, Field, validator
except ImportError:  # pragma: no cover
    BaseModel = None  # type: ignore[assignment]
    Field = None  # type: ignore[assignment]
    validator = None  # type: ignore[assignment]


if BaseModel:  # pragma: no cover - executed in environments with pydantic

    class Resource(BaseModel):
        type: str
        title: str
        url: str


    class LearningModule(BaseModel):
        id: str
        concept_id: str
        title: str
        objectives: List[str]
        content_summary: str
        resources: List[Resource]


    class Concept(BaseModel):
        id: str
        title: str
        summary: str
        why_it_matters: str
        modules: List[LearningModule]


    class ExpertAvailability(BaseModel):
        weekday: str
        start: time
        end: time

        @validator("weekday")
        def normalize_weekday(cls, value: str) -> str:
            return value.strip().lower()


    class Expert(BaseModel):
        id: str
        name: str
        credentials: str
        focus_areas: List[str]
        rate_per_hour: float
        group_discount: float = Field(1.0, ge=0.0, le=1.0)
        availability: List[ExpertAvailability]


    class BookingRequest(BaseModel):
        expert_id: str
        concept_id: str
        start_time: datetime
        duration_minutes: int
        client_name: str
        group_size: Optional[int] = 1

        @property
        def is_group_session(self) -> bool:
            return self.group_size is not None and self.group_size > 1


    class BookingConfirmation(BaseModel):
        booking_id: str
        expert: Expert
        concept: Concept
        start_time: datetime
        end_time: datetime
        group_size: int
        price: float


    class ConceptResponse(BaseModel):
        concepts: List[Concept]


    class ExpertsResponse(BaseModel):
        experts: List[Expert]


    class BookingResponse(BaseModel):
        confirmation: BookingConfirmation

else:
    from dataclasses import dataclass, field

    @dataclass
    class Resource:
        type: str
        title: str
        url: str


    @dataclass
    class LearningModule:
        id: str
        concept_id: str
        title: str
        objectives: List[str]
        content_summary: str
        resources: List[Resource]


    @dataclass
    class Concept:
        id: str
        title: str
        summary: str
        why_it_matters: str
        modules: List[LearningModule]


    @dataclass
    class ExpertAvailability:
        weekday: str
        start: time
        end: time

        def __post_init__(self) -> None:
            self.weekday = self.weekday.strip().lower()


    @dataclass
    class Expert:
        id: str
        name: str
        credentials: str
        focus_areas: List[str]
        rate_per_hour: float
        group_discount: float = 1.0
        availability: List[ExpertAvailability] = field(default_factory=list)


    @dataclass
    class BookingRequest:
        expert_id: str
        concept_id: str
        start_time: datetime
        duration_minutes: int
        client_name: str
        group_size: Optional[int] = 1

        @property
        def is_group_session(self) -> bool:
            return self.group_size is not None and self.group_size > 1


    @dataclass
    class BookingConfirmation:
        booking_id: str
        expert: Expert
        concept: Concept
        start_time: datetime
        end_time: datetime
        group_size: int
        price: float


    @dataclass
    class ConceptResponse:
        concepts: List[Concept]


    @dataclass
    class ExpertsResponse:
        experts: List[Expert]


    @dataclass
    class BookingResponse:
        confirmation: BookingConfirmation
