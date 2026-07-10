# genpark-order-cancellation-predictor-skill

> **GenPark AI Agent Skill** -- Predictive cancellation risk analyzer.

## Quick Start

```python
from client import OrderCancellationPredictorClient
client = OrderCancellationPredictorClient()
res = client.predict_risk("authorized", 100, 2)
print(res["risk_tier"])
```
