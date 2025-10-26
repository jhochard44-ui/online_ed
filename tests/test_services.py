from __future__ import annotations

from datetime import datetime

from app.schemas import BookingRequest
from app.services import BOOKINGS, create_booking, get_concept, list_concepts, list_experts


def setup_function() -> None:
    BOOKINGS.clear()


def test_list_concepts_includes_modules() -> None:
    concepts = list_concepts()
    assert concepts, "Concept list should not be empty"
    first = concepts[0]
    assert first.modules, "Concept should include modules"


def test_get_concept_unknown_returns_none() -> None:
    assert get_concept("unknown") is None


def test_list_experts_filters_by_concept() -> None:
    experts = list_experts("supply-demand")
    assert experts
    assert all("supply-demand" in expert.focus_areas for expert in experts)


def test_booking_rejects_misaligned_concept() -> None:
    request = BookingRequest(
        expert_id="dr-rivera",
        concept_id="supply-demand",
        start_time=datetime.fromisoformat("2024-05-07T13:30:00"),
        duration_minutes=60,
        client_name="Test Learner",
    )
    assert create_booking(request) is None


def test_successful_booking_returns_confirmation() -> None:
    request = BookingRequest(
        expert_id="prof-chan",
        concept_id="supply-demand",
        start_time=datetime.fromisoformat("2024-05-08T15:30:00"),
        duration_minutes=60,
        client_name="Test Learner",
        group_size=3,
    )
    confirmation = create_booking(request)
    assert confirmation is not None
    assert confirmation.price < 500, "Group discount should reduce price"
    assert len(BOOKINGS) == 1


def test_booking_conflict_detected() -> None:
    base_request = BookingRequest(
        expert_id="prof-chan",
        concept_id="supply-demand",
        start_time=datetime.fromisoformat("2024-05-08T15:30:00"),
        duration_minutes=60,
        client_name="Learner One",
    )
    assert create_booking(base_request) is not None

    overlapping_request = BookingRequest(
        expert_id="prof-chan",
        concept_id="supply-demand",
        start_time=datetime.fromisoformat("2024-05-08T16:00:00"),
        duration_minutes=60,
        client_name="Learner Two",
    )
    assert create_booking(overlapping_request) is None


def test_booking_outside_availability() -> None:
    request = BookingRequest(
        expert_id="prof-chan",
        concept_id="supply-demand",
        start_time=datetime.fromisoformat("2024-05-07T15:30:00"),
        duration_minutes=60,
        client_name="Learner Late",
    )
    assert create_booking(request) is None
