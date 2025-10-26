"""Service layer for the economics education prototype."""
from __future__ import annotations

from datetime import datetime, timedelta
from typing import Dict, Iterable, List, Optional
from uuid import uuid4

from . import data
from .schemas import (
    BookingConfirmation,
    BookingRequest,
    Concept,
    Expert,
    LearningModule,
)

# In-memory booking store for prototype purposes only.
BOOKINGS: List[Dict] = []


def _concept_modules(concept_id: str) -> List[LearningModule]:
    return [
        LearningModule(**module)
        for module in data.MODULES
        if module["concept_id"] == concept_id
    ]


def list_concepts() -> List[Concept]:
    """Return each concept with its associated learning modules."""
    return [
        Concept(**concept_dict, modules=_concept_modules(concept_id))
        for concept_id, concept_dict in data.CONCEPTS.items()
    ]


def get_concept(concept_id: str) -> Optional[Concept]:
    concept_info = data.CONCEPTS.get(concept_id)
    if not concept_info:
        return None
    return Concept(**concept_info, modules=_concept_modules(concept_id))


def list_experts(concept_id: Optional[str] = None) -> List[Expert]:
    experts: Iterable[Dict] = data.EXPERTS.values()
    if concept_id:
        concept_id = concept_id.strip().lower()
        experts = [
            expert
            for expert in experts
            if concept_id in {area.lower() for area in expert["focus_areas"]}
        ]
    return [Expert(**expert_dict) for expert_dict in experts]


def _slot_overlaps(existing_start: datetime, existing_end: datetime, start: datetime, end: datetime) -> bool:
    return existing_start < end and start < existing_end


def _is_within_availability(expert: Expert, start: datetime, end: datetime) -> bool:
    weekday_name = start.strftime("%A").lower()
    for window in expert.availability:
        window_weekday = getattr(window, "weekday", None)
        if window_weekday is None and isinstance(window, dict):
            window_weekday = str(window.get("weekday", "")).strip().lower()
        elif window_weekday is not None:
            window_weekday = str(window_weekday).strip().lower()

        window_start = getattr(window, "start", None)
        if window_start is None and isinstance(window, dict):
            window_start = window.get("start")

        window_end = getattr(window, "end", None)
        if window_end is None and isinstance(window, dict):
            window_end = window.get("end")

        if window_weekday != weekday_name:
            continue
        if window_start is None or window_end is None:
            continue
        if window_start <= start.time() and end.time() <= window_end:
            return True
    return False


def _has_conflict(expert_id: str, start: datetime, end: datetime) -> bool:
    for booking in BOOKINGS:
        if booking["expert_id"] != expert_id:
            continue
        if _slot_overlaps(booking["start"], booking["end"], start, end):
            return True
    return False


def _calculate_price(expert: Expert, duration_minutes: int, group_size: int) -> float:
    hours = duration_minutes / 60
    base = expert.rate_per_hour * hours
    if group_size > 1:
        return round(base * expert.group_discount, 2)
    return round(base, 2)


def create_booking(request: BookingRequest) -> Optional[BookingConfirmation]:
    concept = get_concept(request.concept_id)
    if not concept:
        return None

    expert_dict = data.EXPERTS.get(request.expert_id)
    if not expert_dict:
        return None
    expert = Expert(**expert_dict)

    if request.concept_id not in expert.focus_areas:
        return None

    start_time = request.start_time
    end_time = start_time + timedelta(minutes=request.duration_minutes)

    if not _is_within_availability(expert, start_time, end_time):
        return None

    if _has_conflict(expert.id, start_time, end_time):
        return None

    booking_id = str(uuid4())
    group_size = request.group_size or 1
    price = _calculate_price(expert, request.duration_minutes, group_size)

    BOOKINGS.append(
        {
            "booking_id": booking_id,
            "expert_id": expert.id,
            "concept_id": concept.id,
            "start": start_time,
            "end": end_time,
            "group_size": group_size,
            "price": price,
        }
    )

    return BookingConfirmation(
        booking_id=booking_id,
        expert=expert,
        concept=concept,
        start_time=start_time,
        end_time=end_time,
        group_size=group_size,
        price=price,
    )
