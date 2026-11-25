import pandas as pd

from src.generator import generate_synthetic_population
from src.evaluation import evaluate_synthetic_data

# Gerando a referencia de dados sintéticos

reference_data = generate_synthetic_population(n=5000, seed=42)

# Gerando uma nova população sintética para comparação

synthetic_data = generate_synthetic_population(n=5000, seed=123)

# Avaliando a qualidade dos dados sintéticos gerados
results = evaluate_synthetic_data(reference_data, synthetic_data)

print("\n Distibution Metrics:")
print(results['distribution_metrics'])

print("\n Correlation Metrics:")
print(results['correlation_metrics']['difference'])

print("\n Mean Absolute Error of Correlation Matrices:")
print(results['correlation_metrics']['mean_absolute_error'])