"""
order-cancellation-predictor-skill: Client SDK
Estimates cancellation risk probabilities based on historical customer order triggers.
"""
from __future__ import annotations
from typing import Optional


class OrderCancellationPredictorClient:
    """
    SDK for cancellation predictive analysis.
    """

    def predict_risk(
        self,
        payment_status: str,
        days_since_first_order: int,
        total_item_qty: int,
    ) -> dict:
        score = 0.1  # base risk

        # Rule triggers
        if payment_status.lower() in ("failed", "pending"):
            score += 0.4
        if days_since_first_order < 3:  # brand new guest account
            score += 0.2
        if total_item_qty > 20:  # bulk order hoarding risk
            score += 0.15

        prob = min(0.99, score)
        
        if prob >= 0.6:
            tier = "high"
        elif prob >= 0.3:
            tier = "medium"
        else:
            tier = "low"

        return {
            "cancellation_probability": round(prob, 2),
            "risk_tier": tier,
            "review_recommended": tier == "high"
        }
