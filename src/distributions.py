import numpy as np

def normal_distribution(n, mean, std, rng=None, min_value=None, max_value=None):
    """
    Generates a normal distribution of n samples with specified mean and standard deviation.
    Optionally, you can specify a random number generator (rng) and min/max values to clip the distribution.

    Parameters:
    - n: int, number of samples to generate
    - mean: float, mean of the normal distribution
    - std: float, standard deviation of the normal distribution
    - rng: np.random.Generator, optional random number generator for reproducibility
    - min_value: float, optional minimum value to clip the distribution
    - max_value: float, optional maximum value to clip the distribution

    Returns:
    - np.ndarray: array of generated samples
    """
    rng = rng or np.random.default_rng()

    values = rng.normal(mean, std, n)

    if min_value is not None or max_value is not None:
        values = np.clip(values, 
                         min_value if min_value is not None else -np.inf,
                         max_value if max_value is not None else np.inf)
    
    return values

def binomial_distribution(n, probability, rng=None):
    """
    Generates a binomial distribution of specified size with given number of trials and probability of success.
    Optionally, you can specify a random number generator (rng) for reproducibility.

    Parameters:
    - n: int, number of trials
    - p: float, probability of success on each trial
    - size: int, number of samples to generate
    - rng: np.random.Generator, optional random number generator for reproducibility

    Returns:
    - np.ndarray: array of generated samples
    """
    rng = rng or np.random.default_rng()

    probability = np.asarray(probability)
    
    return rng.binomial(1, probability, size=n)

def poisson_distribution(n, rate, rng=None):
    """
    Generates a Poisson distribution of specified size with given lambda (rate) parameter.
    Optionally, you can specify a random number generator (rng) for reproducibility.

    Parameters:
    - n: int, number of samples to generate
    - lam: float, lambda (rate) parameter of the Poisson distribution
    - rng: np.random.Generator, optional random number generator for reproducibility

    Returns:
    - np.ndarray: array of generated samples
    """
    rng = rng or np.random.default_rng()

    rate = np.asarray(rate)

    return rng.poisson(rate, size=n)

def lognormal_distribution(n, mean, sigma, rng=None):
    """
    Generates a log-normal distribution of specified size with given mean and sigma parameters.
    Optionally, you can specify a random number generator (rng) for reproducibility.

    Parameters:
    - n: int, number of samples to generate
    - mean: float, mean of the underlying normal distribution
    - sigma: float, standard deviation of the underlying normal distribution
    - rng: np.random.Generator, optional random number generator for reproducibility

    Returns:
    - np.ndarray: array of generated samples
    """
    rng = rng or np.random.default_rng()

    return rng.lognormal(mean=mean, sigma=sigma, size=n)

def categorical_distribution(n, categories, probabilities, rng=None):
    """
    Generates a categorical distribution of specified size with given categories and optional probabilities.
    Optionally, you can specify a random number generator (rng) for reproducibility.

    Parameters:
    - n: int, number of samples to generate
    - categories: list or array-like, the categories to sample from
    - probabilities: list or array-like, optional probabilities for each category (must sum to 1)
    - rng: np.random.Generator, optional random number generator for reproducibility

    Returns:
    - np.ndarray: array of generated samples
    """
    rng = rng or np.random.default_rng()

    probabilities = np.asarray(probabilities, dtype=float)

    if len(categories) != len(probabilities):
        raise ValueError("Length of categories and probabilities must match.")

    if np.any(probabilities < 0) or not np.isclose(probabilities.sum(), 1):
        raise ValueError("Probabilities must be non-negative and sum to 1.")
    
    return rng.choice(categories, size=n, p=probabilities)

def sigmoid(values):
    """
    Applies the sigmoid function to the input values.

    Parameters:
    - values: array-like, input values to apply the sigmoid function

    Returns:
    - np.ndarray: array of values after applying the sigmoid function
    """
    values = np.asarray(values)

    return 1 / (1 + np.exp(-np.clip(values, -30, 30)))

def conditional_binary(linear_predictor, rng=None):
    """
    Generates binary outcomes based on a linear predictor using the sigmoid function.
    Optionally, you can specify a random number generator (rng) for reproducibility.

    Parameters:
    - linear_predictor: array-like, input values to compute probabilities
    - rng: np.random.Generator, optional random number generator for reproducibility

    Returns:
    - np.ndarray: array of binary outcomes (0 or 1)
    """
    rng = rng or np.random.default_rng()

    probabilities = sigmoid(linear_predictor)

    return rng.binomial(1, probabilities)

def conditional_poisson(linear_predictor, rng=None):
    """
    Generates Poisson-distributed outcomes based on a linear predictor using the exponential function.
    Optionally, you can specify a random number generator (rng) for reproducibility.

    Parameters:
    - linear_predictor: array-like, input values to compute the rate parameter (lambda)
    - rng: np.random.Generator, optional random number generator for reproducibility

    Returns:
    - np.ndarray: array of Poisson-distributed outcomes
    """
    rng = rng or np.random.default_rng()

    rates = np.exp(np.clip(linear_predictor, -10, 10))

    return rng.poisson(rates)

def generate_correlated_normal(n, means, correlation_matrix, rng=None):
    """
    Generates correlated normal variables based on a specified correlation matrix.
    Optionally, you can specify a random number generator (rng) for reproducibility.

    Parameters:
    - n: int, number of samples to generate
    - mean: array-like, means of the normal distributions
    - std: array-like, standard deviations of the normal distributions
    - correlation_matrix: 2D array-like, correlation matrix specifying correlations between variables
    - rng: np.random.Generator, optional random number generator for reproducibility

    Returns:
    - np.ndarray: array of generated correlated normal samples
    """
    rng = rng or np.random.default_rng()

    means = np.asarray(means, dtype=float)
    
    correlation_matrix = np.asarray(correlation_matrix, dtype=float)

    # Validate dimensions
    if (len(means), len(means)) != correlation_matrix.shape:
        raise ValueError("Correlation matrix dimensions must match means.")

    if not np.allclose(correlation_matrix, correlation_matrix.T):
        raise ValueError("Correlation matrix must be symmetric.")

    if not np.allclose(np.diag(correlation_matrix), 1):
        raise ValueError("Correlation matrix must have 1s on the diagonal.")

    eigenvalues = np.linalg.eigvals(correlation_matrix)

    if np.min(eigenvalues) < -1e-8:
        raise ValueError("Correlation matrix must be positive semi-definite.")

    return rng.multivariate_normal(mean=means, cov=correlation_matrix, size=n)