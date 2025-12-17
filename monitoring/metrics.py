import time
from collections import defaultdict

class MetricsTracker:
    def __init__(self):
        self.request_count = 0
        self.escalation_count = 0
        self.total_latency = 0.0
        self.total_confidence = 0.0
        self.priority_counts = defaultdict(int)

    def record(
        self,
        latency: float,
        confidence: float,
        priority: str,
        escalated: bool
    ):
        self.request_count += 1
        self.total_latency += latency
        self.total_confidence += confidence
        self.priority_counts[priority] += 1

        if escalated:
            self.escalation_count += 1

    def snapshot(self):
        if self.request_count == 0:
            return {}

        return {
            "requests": self.request_count,
            "avg_latency_ms": round((self.total_latency / self.request_count) * 1000, 2),
            "avg_confidence": round(self.total_confidence / self.request_count, 2),
            "escalation_rate": round(self.escalation_count / self.request_count, 2),
            "priority_distribution": dict(self.priority_counts)
        }


# singleton-style tracker
metrics = MetricsTracker()
