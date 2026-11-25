import numpy as np
import pandas as pd

from scipy.stats import ks_2samp, wasserstein_distance

from scipy.spatial.distance import jensenshannon

def validate_datasets(real_data, synthetic_data):
    """
    Validate the similarity between real and synthetic datasets using statistical tests.

    Parameters:
    - real_data: pd.DataFrame, the real dataset
    - synthetic_data: pd.DataFrame, the synthetic dataset
    - columns: list of str, the columns to compare

    Returns:
    - results: dict, containing the results of the statistical tests for each column
    """

    if not isinstance(real_data, pd.DataFrame):
        raise TypeError("real_data must be a pandas DataFrame.")

    if not isinstance(synthetic_data, pd.DataFrame):
        raise TypeError("synthetic_data must be a pandas DataFrame.")

    if real_data.empty or synthetic_data.empty:
        raise ValueError("Datasets cannot be empty.")

    common_columns = [col for col in real_data.columns if col in synthetic_data.columns]

    if not common_columns:
        raise ValueError("No common columns between datasets.")

    return common_columns

def descriptive_statistics(data):
    """
    Calculate descriptive statistics for a given dataset.

    Parameters:
    - data: pd.DataFrame, the dataset to analyze

    Returns:
    - stats: pd.DataFrame, containing descriptive statistics for each column
    """

    return data.describe(include='all').T

def numeric_distribution_metrics(real, synthetic):
    """
    Calculate distribution metrics for numeric columns between real and synthetic datasets.

    Parameters:
    - real: pd.DataFrame, the real dataset
    - synthetic: pd.DataFrame, the synthetic dataset

    Returns:
    - metrics: dict, containing KS statistic, Wasserstein distance, and Jensen-Shannon divergence for each numeric column
    """

    real = pd.to_numeric(real, errors="coerce").dropna()
    synthetic = pd.to_numeric(synthetic, errors="coerce").dropna()

    if len(real) < 2 or len(synthetic) < 2:
        return {
            "ks_statistic": np.nan,
            "ks_p_value": np.nan,
            "wasserstein_distance": np.nan
        }

    ks_result = ks_2samp(real, synthetic)

    return {
        "ks_statistic": float(ks_result.statistic),
        "ks_p_value": float(ks_result.pvalue),
        "wasserstein_distance": float(wasserstein_distance(real, synthetic))
    }

def categorical_distribution_metrics(real, synthetic):
    """
    Calculate distribution metrics for categorical columns between real and synthetic datasets.

    Parameters:
    - real: pd.Series, the real dataset column
    - synthetic: pd.Series, the synthetic dataset column

    Returns:
    - metrics: dict, containing Jensen-Shannon divergence for each categorical column
    """

    real = real.astype("object").fillna("MISSING").astype(str)
    synthetic = (
        synthetic.astype("object").fillna("MISSING").astype(str)
    )

    categories = sorted(set(real.unique()) | set(synthetic.unique()))

    real_proportions = (real.value_counts(normalize=True).reindex(categories, fill_value=0).values)

    synthetic_proportions = (synthetic.value_counts(normalize=True).reindex(categories, fill_value=0).values)

    total_variation = 0.5 * np.sum(np.abs(real_proportions - synthetic_proportions))

    js_distance = jensenshannon(real_proportions, synthetic_proportions)

    return {"total_variation_distance": float(total_variation),
            "jensen_shannon_distance": float(js_distance)}

def compare_distributions(real_data, synthetic_data):
    """
    Compare distributions of real and synthetic datasets.

    Parameters:
    - real_data: pd.DataFrame, the real dataset
    - synthetic_data: pd.DataFrame, the synthetic dataset

    Returns:
    - comparison_results: dict, containing distribution metrics for each column
    """

    columns = validate_datasets(real_data, synthetic_data)

    results = []

    for column in columns:

        real = real_data[column]
        synthetic = synthetic_data[column]

        if (pd.api.types.is_numeric_dtype(real) and pd.api.types.is_numeric_dtype(synthetic)):
            metrics = numeric_distribution_metrics(real, synthetic)

            variable_type = "numeric"

        else: 
            metrics = categorical_distribution_metrics(real, synthetic)

            variable_type = "categorical"

        results.append({
            "variable": column,
            "type": variable_type,
            **metrics})

        return pd.DataFrame(results)

def compare_correlations(real_data, synthetic_data):
    """
    Compare correlation matrices of real and synthetic datasets.

    Parameters:
    - real_data: pd.DataFrame, the real dataset
    - synthetic_data: pd.DataFrame, the synthetic dataset

    Returns:
    - correlation_comparison: dict, containing correlation matrices and their differences
    """

    columns = validate_datasets(real_data, synthetic_data)

    numeric_columns = [col for col in columns if pd.api.types.is_numeric_dtype(real_data[col]) and pd.api.types.is_numeric_dtype(synthetic_data[col])]

    if len(numeric_columns) < 2:
        raise ValueError("At least two numeric columns are required for correlation comparison.")

    real_corr = real_data[numeric_columns].corr(method='pearson')

    synthetic_corr = synthetic_data[numeric_columns].corr(method='pearson')

    difference = real_corr - synthetic_corr

    return {
        "real_correlation": real_corr,
        "synthetic_correlation": synthetic_corr,
        "difference": difference,
        "mean_absolute_error": float(np.abs(difference.values).mean())
    }

def evaluate_synthetic_data(real_data, synthetic_data):
    """
    Evaluate the quality of synthetic data by comparing it to real data.

    Parameters:
    - real_data: pd.DataFrame, the real dataset
    - synthetic_data: pd.DataFrame, the synthetic dataset

    Returns:
    - evaluation_results: dict, containing distribution and correlation comparison results
    """

    validate_datasets(real_data, synthetic_data)

    distribution_results = compare_distributions(real_data, synthetic_data)

    correlation_results = compare_correlations(real_data, synthetic_data)

    return {
        "real_summary": descriptive_statistics(real_data),
        "synthetic_summary": descriptive_statistics(synthetic_data),
        "distribution_metrics": distribution_results,
        "correlation_metrics": correlation_results
    }