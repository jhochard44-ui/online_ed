"""FastAPI router exposing the economics learning prototype."""
from __future__ import annotations

from fastapi import FastAPI, HTTPException

from .schemas import BookingRequest, BookingResponse, ConceptResponse, ExpertsResponse
from .services import create_booking, get_concept, list_concepts, list_experts

app = FastAPI(
    title="Economics Learning Prototype",
    description=(
        "Explore foundational economic concepts, practice with guided modules, "
        "and book time with industry experts."
    ),
)


@app.get("/concepts", response_model=ConceptResponse)
def read_concepts() -> ConceptResponse:
    return ConceptResponse(concepts=list_concepts())


@app.get("/concepts/{concept_id}", response_model=ConceptResponse)
def read_concept(concept_id: str) -> ConceptResponse:
    concept = get_concept(concept_id)
    if not concept:
        raise HTTPException(status_code=404, detail="Concept not found")
    return ConceptResponse(concepts=[concept])


@app.get("/experts", response_model=ExpertsResponse)
def read_experts(concept_id: str | None = None) -> ExpertsResponse:
    experts = list_experts(concept_id)
    if concept_id and not experts:
        raise HTTPException(status_code=404, detail="No experts cover this concept yet")
    return ExpertsResponse(experts=experts)


@app.post("/bookings", response_model=BookingResponse)
def create_booking_endpoint(request: BookingRequest) -> BookingResponse:
    confirmation = create_booking(request)
    if not confirmation:
        raise HTTPException(
            status_code=400,
            detail=(
                "Unable to schedule session. Check concept alignment, "
                "availability, and requested time."
            ),
        )
    return BookingResponse(confirmation=confirmation)
