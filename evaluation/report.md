## Model Evaluation Summary

- Model: TF-IDF + Logistic Regression
- Accuracy: 82%
- Macro F1 Score: 0.79

### Observations
- Strong performance on Billing and Payment issues
- Confusion between Promo Missing and Billing
- Low-confidence predictions are escalated

### Risk Mitigation
- Confidence threshold prevents incorrect automation
- Human-in-the-loop escalation enabled
