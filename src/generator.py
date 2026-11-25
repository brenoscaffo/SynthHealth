import numpy as np
import pandas as pd

def generate_synthetic_population(n=10000,
                                  seed=42,
                                  min_age=18,
                                  max_age=98):
    rng = np.random.default_rng(seed)

    age = rng.integers(min_age, max_age + 1, size=n)

    sex = rng.choice(['Male', 'Female'], size=n, p = [0.52, 0.48])

    # IMC: condicionada pela idade

    bmi = np.clip(rng.normal(27 + (age - 45) * 0.035, 5, n), 16, 55)

    # Probabilidade  de hipertensão condicionada pela idade

    p_hypertension = np.clip(0.08 + (age - 18)*0.006,
                             0.05, 
                             0.55)

    hypertension = rng.binomial(1, p_hypertension)

    # Diabetes: condicionada pela idade, hipertensão e imc

    logit_diabetes = (-4 + 0.035 * age
                      + 0.09 * (bmi - 25)
                      + 0.65 * hypertension)

    p_diabetes = 1 / (1 + np.exp(-logit_diabetes))
    diabetes = rng.binomial(1, p_diabetes)

    # Fumante

    smoking_status = rng.choice(['Never', 'Former', 'Current'], size=n, p=[0.58, 0.25, 0.17])

    # Condicoes cronicas

    chronic_conditions = (hypertension + diabetes
                          + rng.binomial(1, np.clip((age - 45) / 100, 0, 0.45))
                          + rng.binomial(1, 0.08, n))

    # Utilizacao de servicos de saude

    outpatient_visits = rng.poisson(2 + age / 25 + 1.2 * chronic_conditions)

    emergency_visits = rng.poisson(0.15 + 0.25 * chronic_conditions)

    hospitalization_probability = np.clip(0.02 + age / 500 + chronic_conditions * 0.06, 0.01, 0.65)

    hospitalizations = rng.binomial(1, hospitalization_probability)

    # Custo anual com assimetria e dependencia clinica

    annual_cost = (800 + age * 18
                   + chronic_conditions * 1200
                   + outpatient_visits * 180
                   + emergency_visits * 900
                   + hospitalizations * rng.lognormal(8.2, 0.65, n)
                   + rng.lognormal(6.5, 0.5, n))

    # score sintetico de risco
    risk_score = (age * 0.30
                  + chronic_conditions * 12
                  + hospitalizations * 15
                  + emergency_visits * 3
                  + diabetes * 8
                  + hypertension * 5)

    # Montando o DataFrame final
    df = pd.DataFrame({
        'patient_id': [f"SH{i:06d}" for i in range(1, n + 1)],
        'age': age,
        'sex': sex,
        'bmi': np.round(bmi, 2),
        'hypertension': hypertension,
        'diabetes': diabetes,
        'smoking_status': smoking_status,
        'chronic_conditions': chronic_conditions,
        'outpatient_visits': outpatient_visits,
        'emergency_visits': emergency_visits,
        'hospitalizations': hospitalizations,
        'annual_cost': np.round(annual_cost, 2),
        'risk_score': np.round(risk_score, 2)})

    return df