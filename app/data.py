"""Static seed data for the economics learning prototype."""
from __future__ import annotations

from datetime import time
from typing import Dict, List

# Concept data keyed by identifier for fast lookup.
CONCEPTS: Dict[str, Dict] = {
    "supply-demand": {
        "id": "supply-demand",
        "title": "Supply and Demand",
        "summary": (
            "How markets balance production and consumption through price signals."
        ),
        "why_it_matters": (
            "Supply and demand analysis guides pricing, inventory planning, and policy "
            "decisions across every industry."
        ),
    },
    "gdp-measurement": {
        "id": "gdp-measurement",
        "title": "GDP and Economic Growth",
        "summary": (
            "The accounting systems that track the value of goods and services over time."
        ),
        "why_it_matters": (
            "Understanding GDP allows leaders to interpret macroeconomic performance "
            "and benchmark business strategies."
        ),
    },
    "monetary-policy": {
        "id": "monetary-policy",
        "title": "Monetary Policy Mechanics",
        "summary": (
            "How central banks influence money supply, interest rates, and liquidity."
        ),
        "why_it_matters": (
            "Professionals use monetary policy insights to anticipate capital costs and "
            "market volatility."
        ),
    },
    "market-failures": {
        "id": "market-failures",
        "title": "Market Failures and Externalities",
        "summary": (
            "When markets misprice risk, information, or societal costs and how policy "
            "attempts to fix the gaps."
        ),
        "why_it_matters": (
            "Identifying market failures is essential for designing regulation and "
            "building sustainable business models."
        ),
    },
}

MODULES: List[Dict] = [
    {
        "id": "supply-demand-foundations",
        "concept_id": "supply-demand",
        "title": "Visualizing Supply and Demand Curves",
        "objectives": [
            "Interpret shifts versus movements along curves",
            "Calculate equilibrium price and quantity",
            "Identify factors that drive supply or demand shocks",
        ],
        "content_summary": (
            "Interactive walkthrough using historical commodities data to illustrate "
            "equilibrium adjustments."
        ),
        "resources": [
            {
                "type": "video",
                "title": "Crash course in supply-demand dynamics",
                "url": "https://example.com/videos/supply-demand",
            },
            {
                "type": "dataset",
                "title": "US wheat futures (2010-2020)",
                "url": "https://example.com/data/wheat-futures",
            },
        ],
    },
    {
        "id": "supply-demand-scenarios",
        "concept_id": "supply-demand",
        "title": "Scenario Planning for Pricing Teams",
        "objectives": [
            "Build simple elasticity calculators",
            "Simulate price floors and ceilings",
            "Discuss cross elasticity in bundled offerings",
        ],
        "content_summary": (
            "Spreadsheet driven workshop that explores how pricing teams test "
            "launch strategies using elasticity models."
        ),
        "resources": [
            {
                "type": "worksheet",
                "title": "Elasticity sensitivity template",
                "url": "https://example.com/resources/elasticity-template",
            }
        ],
    },
    {
        "id": "gdp-accounting",
        "concept_id": "gdp-measurement",
        "title": "Building a GDP Accounting Dashboard",
        "objectives": [
            "Compare expenditure and income approaches",
            "Identify leading and lagging GDP components",
            "Translate GDP releases into business indicators",
        ],
        "content_summary": (
            "Learners populate a dashboard that connects GDP releases to hiring "
            "and investment decisions."
        ),
        "resources": [
            {
                "type": "article",
                "title": "Guide to GDP data sources",
                "url": "https://example.com/articles/gdp-guide",
            }
        ],
    },
    {
        "id": "monetary-policy-tools",
        "concept_id": "monetary-policy",
        "title": "Central Bank Playbooks",
        "objectives": [
            "Differentiate between conventional and unconventional tools",
            "Model how rate decisions affect corporate finance",
            "Track communication strategies in policy signaling",
        ],
        "content_summary": (
            "Case-based module analyzing how the Federal Reserve and ECB respond "
            "to inflationary and deflationary pressures."
        ),
        "resources": [
            {
                "type": "podcast",
                "title": "Inside the FOMC",
                "url": "https://example.com/podcasts/inside-fomc",
            }
        ],
    },
    {
        "id": "market-failure-lab",
        "concept_id": "market-failures",
        "title": "Diagnosing Externalities in Emerging Markets",
        "objectives": [
            "Map information asymmetries",
            "Design public-private intervention frameworks",
            "Evaluate impact investing metrics",
        ],
        "content_summary": (
            "Collaborative workshop where learners design policy briefs for urban "
            "mobility and carbon trading."
        ),
        "resources": [
            {
                "type": "report",
                "title": "World Bank case studies on externalities",
                "url": "https://example.com/reports/externalities",
            }
        ],
    },
]

EXPERTS: Dict[str, Dict] = {
    "dr-rivera": {
        "id": "dr-rivera",
        "name": "Dr. Helena Rivera",
        "credentials": "Former World Bank chief economist, author of 'Resilient Markets'",
        "focus_areas": ["market-failures", "gdp-measurement"],
        "rate_per_hour": 650.0,
        "group_discount": 0.85,
        "availability": [
            {"weekday": "tuesday", "start": time(13, 0), "end": time(16, 0)},
            {"weekday": "thursday", "start": time(9, 0), "end": time(11, 30)},
        ],
    },
    "prof-chan": {
        "id": "prof-chan",
        "name": "Prof. Aaron Chan",
        "credentials": "MIT Sloan professor of managerial economics",
        "focus_areas": ["supply-demand", "monetary-policy"],
        "rate_per_hour": 500.0,
        "group_discount": 0.9,
        "availability": [
            {"weekday": "wednesday", "start": time(15, 0), "end": time(18, 0)},
            {"weekday": "friday", "start": time(8, 30), "end": time(12, 0)},
        ],
    },
    "dr-saito": {
        "id": "dr-saito",
        "name": "Dr. Naomi Saito",
        "credentials": "Senior advisor at the Bank for International Settlements",
        "focus_areas": ["monetary-policy"],
        "rate_per_hour": 720.0,
        "group_discount": 0.8,
        "availability": [
            {"weekday": "monday", "start": time(10, 0), "end": time(12, 30)},
            {"weekday": "thursday", "start": time(14, 0), "end": time(17, 30)},
        ],
    },
}
