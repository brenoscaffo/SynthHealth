# SynthHealth
Programa que produz dados sintéticos para área da saúde
=======
# SynthHealth - EN
### Synthetic Healthcare Data Generator & Analytics Toolkit

**An open-source framework for synthetic healthcare data generation and statistical fidelity assessment.**

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Status](https://img.shields.io/badge/Status-Development-orange)
![License](https://img.shields.io/badge/License-MIT-green)
![Domain](https://img.shields.io/badge/Domain-Data%20Science-purple)

---

## 1. Overview

SynthHealth is an open-source software project designed to generate synthetic healthcare datasets using statistical and probabilistic methods.

The framework aims to support data science research, statistical experimentation, machine learning development, and educational applications in healthcare analytics.

SynthHealth generates artificial patient-level records with configurable demographic, clinical, healthcare utilization, and financial characteristics.

The software also provides statistical tools to assess the fidelity of synthetic datasets through distributional comparisons, statistical distances, and correlation analysis.

**SynthHealth does not require real patient-level data to generate its demonstration datasets.**

## 2. Objectives

The main objectives of SynthHealth are:

- Generate reproducible synthetic healthcare datasets.
- Simulate demographic and clinical characteristics.
- Model probabilistic relationships between healthcare variables.
- Generate healthcare utilization and cost variables.
- Evaluate statistical fidelity between reference and synthetic datasets.
- Provide accessible tools for data science experimentation.
- Support the development and testing of machine learning models without requiring identifiable patient records.

## 3. Main Features

### 3.1 Synthetic Data Generation

The framework supports the generation of artificial healthcare populations with variables such as:

| Variable | Description |
|---|---|
| patient_id | Synthetic patient identifier |
| age | Patient age |
| sex | Sex category |
| bmi | Body Mass Index |
| hypertension | Hypertension indicator |
| diabetes | Diabetes indicator |
| smoking_status | Smoking category |
| chronic_conditions | Number of chronic conditions |
| outpatient_visits | Outpatient healthcare utilization |
| emergency_visits | Emergency department utilization |
| hospitalizations | Hospital admissions |
| annual_cost | Annual healthcare expenditure |
| risk_score | Synthetic risk indicator |

### 3.2 Statistical Distributions

The statistical module includes functions for:

- Normal distribution.
- Binomial distribution.
- Poisson distribution.
- Lognormal distribution.
- Categorical distribution.
- Conditional binary generation.
- Conditional Poisson generation.
- Multivariate normal generation with specified correlations.

### 3.3 Statistical Fidelity Assessment

The evaluation module includes:

- Descriptive statistics.
- Kolmogorov-Smirnov statistic.
- Wasserstein distance.
- Total Variation Distance.
- Jensen-Shannon distance.
- Pearson correlation comparison.
- Mean Absolute Error between correlation matrices.

These metrics provide complementary information about the statistical similarities and differences between datasets.

### 3.4 Data Export

Generated datasets can be exported in CSV format for subsequent analysis using Python, R, or other statistical software.

## 4. Software Architecture

```text
SynthHealth/
│
├── src/
│   ├── __init__.py
│   ├── generator.py
│   ├── distributions.py
│   └── evaluation.py
│
├── app.py
├── test_synthhealth.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

### Main Components

| Component | Responsibility |
|---|---|
| generator.py | Synthetic healthcare population generation |
| distributions.py | Statistical distributions and probabilistic functions |
| evaluation.py | Statistical fidelity assessment |
| app.py | Interactive Streamlit application |
| test_synthhealth.py | Initial software validation |

## 5. Installation

### Requirements

- Python 3.10 or later.
- pip package manager.
- Git (optional, for repository cloning).

### Step 1: Clone the repository

```bash
git clone https://github.com/USERNAME/SynthHealth.git

cd SynthHealth
```

Replace `USERNAME` with the GitHub account name hosting the project.

### Step 2: Create a virtual environment

**Windows**

```bash
py -m venv .venv

.venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv .venv

source .venv/bin/activate
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

## 6. Usage

### 6.1 Generate a synthetic population

```python
from src.generator import generate_synthetic_population

dataset = generate_synthetic_population(
    n=5000,
    seed=42
)

print(dataset.head())
```

### 6.2 Export the generated dataset

```python
dataset.to_csv(
    "synthhealth_dataset.csv",
    index=False
)
```

### 6.3 Evaluate statistical fidelity

```python
from src.generator import generate_synthetic_population
from src.evaluation import evaluate_synthetic_data

reference_data = generate_synthetic_population(
    n=5000,
    seed=42
)

synthetic_data = generate_synthetic_population(
    n=5000,
    seed=123
)

results = evaluate_synthetic_data(
    reference_data,
    synthetic_data
)

print(results["distribution_metrics"])

print(
    results["correlation_metrics"]["mean_absolute_error"]
)
```

**Note:** This example compares independent samples from the same synthetic generation mechanism. It is an initial reproducibility and stability experiment, not a validation against real healthcare data.

### 6.4 Run the interactive application

```bash
streamlit run app.py
```

The application will be available locally through the browser, usually at:

`http://localhost:8501`

## 7. Methodological Approach

SynthHealth follows a modular statistical generation approach.

The initial implementation uses probabilistic relationships between demographic, clinical, utilization, and financial variables.

The framework is designed to support future extensions, including:

- Multivariate Gaussian Copula models.
- Advanced conditional probability models.
- Alternative synthetic data generation methods.
- Statistical benchmarking.
- Privacy risk assessment.
- Machine learning utility evaluation.

Future methods will be documented and evaluated independently.

## 8. Validation and Limitations

The current implementation is an initial software prototype.

The generation parameters are illustrative and are not calibrated to represent a validated healthcare population.

Statistical similarity does not necessarily imply clinical validity, population representativeness, or privacy protection.

In particular:

- Synthetic records should not be interpreted as real patient records.
- Generated healthcare costs are illustrative.
- Risk scores are mathematical demonstration variables, not clinical risk assessments.
- Statistical fidelity metrics must be interpreted jointly.
- Privacy guarantees cannot be inferred solely from the use of synthetic data.

Further validation against appropriate independent reference datasets and dedicated privacy assessments will be necessary before making stronger scientific claims.

## 9. Reproducibility

SynthHealth supports reproducible generation through configurable random seeds.

Example:

```python
dataset_a = generate_synthetic_population(
    n=1000,
    seed=42
)

dataset_b = generate_synthetic_population(
    n=1000,
    seed=42
)
```

Using the same configuration and software environment should reproduce the same generated dataset.

## 10. Scientific and Research Applications

Potential applications include:

- Healthcare data science education.
- Statistical simulation.
- Machine learning prototyping.
- Healthcare cost modeling experiments.
- Testing data processing pipelines.
- Statistical method benchmarking.
- Research on synthetic data generation.

SynthHealth is intended as a research and analytical tool, not as a clinical decision support system.


## 11. License

SynthHealth is distributed under the MIT License.

See the `LICENSE` file for details.

## 12. Citation

If you use SynthHealth in academic research, software development, or scientific experimentation, please cite the corresponding archived software version.

**Suggested citation:**

Breno [SURNAME]. (2026). *SynthHealth: An Open-Source Framework for Synthetic Healthcare Data Generation and Statistical Fidelity Assessment* (Version 1.0.0). Zenodo. DOI: [DOI TO BE ASSIGNED].

The DOI and final citation metadata should be updated after the software is archived and published.

## 13. Author

**Breno Scaffo de Andrade Costa**

Software development, statistical methodology, and data science.

## 14. Acknowledgments

SynthHealth is developed as an open-source initiative to support reproducible research and experimentation in healthcare data science.

Contributions, suggestions, and improvements are welcome.

---

**Project:** SynthHealth  
**Version:** 0.1.0 — Development  
**License:** MIT  
**Repository:**   
**DOI:** To be assigned after Zenodo publication

# SynthHealth - PTBR

**Uma estrutura de código aberto para geração de dados sintéticos em saúde e avaliação de fidelidade estatística.**

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-orange)
![License](https://img.shields.io/badge/license-MIT-green)
![Data Science](https://img.shields.io/badge/foco-Ci%C3%AAncia%20de%20Dados-purple)

## Sobre o projeto

O **SynthHealth** é um projeto de código aberto desenvolvido para gerar conjuntos de dados sintéticos relacionados à área da saúde e avaliar sua fidelidade estatística.

A ferramenta foi concebida para apoiar atividades de Ciência de Dados, análise estatística, desenvolvimento de modelos de aprendizado de máquina e experimentação com dados de saúde, especialmente em contextos nos quais o acesso a bases de dados reais pode ser limitado.

O projeto utiliza métodos estatísticos e computacionais para simular características demográficas, clínicas, padrões de utilização de serviços de saúde e custos assistenciais.

**Importante:** os dados gerados pelo SynthHealth são artificiais e possuem finalidade demonstrativa e experimental. Eles não representam necessariamente uma população real e não devem ser utilizados para decisões clínicas.

## Objetivos

- Desenvolver uma ferramenta aberta para geração de dados sintéticos em saúde.
- Implementar mecanismos de simulação de variáveis demográficas e clínicas.
- Representar padrões de utilização de serviços de saúde e custos assistenciais.
- Avaliar a similaridade estatística entre conjuntos de dados.
- Facilitar experimentos em Ciência de Dados e aprendizado de máquina.
- Disponibilizar uma ferramenta reproduzível, extensível e de fácil utilização.

## Funcionalidades

### 1. Geração de dados sintéticos

O SynthHealth permite gerar populações artificiais com variáveis relacionadas à saúde, incluindo:

- Idade;
- Sexo;
- Índice de Massa Corporal (IMC);
- Hipertensão;
- Diabetes;
- Tabagismo;
- Número de condições crônicas;
- Consultas ambulatoriais;
- Atendimentos de emergência;
- Hospitalizações;
- Custos anuais de saúde;
- Indicador sintético de risco.

A geração utiliza distribuições estatísticas e relações probabilísticas entre variáveis.

### 2. Avaliação da fidelidade estatística

O projeto inclui métodos para comparar distribuições e características estatísticas de conjuntos de dados.

As métricas implementadas incluem:

- Estatística de Kolmogorov-Smirnov (KS);
- Valor-p do teste de Kolmogorov-Smirnov;
- Distância de Wasserstein;
- Distância de Jensen-Shannon;
- Distância de variação total;
- Comparação de matrizes de correlação;
- Erro absoluto médio entre matrizes de correlação.

Essas métricas permitem examinar diferentes aspectos da semelhança estatística entre os dados.

### 3. Interface interativa

O projeto utiliza Streamlit para disponibilizar uma interface simples e interativa, permitindo:

- Definir o tamanho da população sintética;
- Configurar a semente aleatória;
- Definir a faixa etária;
- Gerar conjuntos de dados;
- Visualizar estatísticas e gráficos;
- Exportar os dados gerados em formato CSV.

## Tecnologias utilizadas

| Tecnologia | Finalidade |
|---|---|
| Python | Linguagem principal |
| NumPy | Operações numéricas e simulações |
| Pandas | Manipulação de dados |
| SciPy | Métodos estatísticos |
| Scikit-learn | Recursos para Ciência de Dados e aprendizado de máquina |
| Plotly | Visualização interativa |
| Streamlit | Interface web |
| GitHub | Controle de versão e colaboração |
| Zenodo | Arquivamento e obtenção de DOI para versões publicadas |

## Estrutura do projeto

```text
SynthHealth/
│
├── src/
│   ├── __init__.py
│   ├── generator.py
│   ├── distributions.py
│   └── evaluation.py
│
├── app.py
├── test_synthhealth.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

### Descrição dos arquivos

- `generator.py`: responsável pela geração da população sintética.
- `distributions.py`: reúne funções para geração de variáveis utilizando distribuições estatísticas.
- `evaluation.py`: implementa métricas e procedimentos de avaliação estatística.
- `app.py`: disponibiliza a interface interativa desenvolvida com Streamlit.
- `test_synthhealth.py`: contém um exemplo de execução e avaliação do gerador.
- `requirements.txt`: lista as dependências necessárias para executar o projeto.

## Instalação

### 1. Clonar o repositório

```bash
git clone https://github.com/USERNAME/SynthHealth.git
```

### 2. Acessar a pasta do projeto

```bash
cd SynthHealth
```

### 3. Criar um ambiente virtual

```bash
python -m venv venv
```

Ativar o ambiente virtual:

**Windows:**

```bash
venv\Scripts\activate
```

**Linux e macOS:**

```bash
source venv/bin/activate
```

### 4. Instalar as dependências

```bash
pip install -r requirements.txt
```

## Como utilizar

### Executar a interface interativa

Na pasta principal do projeto, execute:

```bash
streamlit run app.py
```

A aplicação será disponibilizada localmente no navegador.

### Gerar dados sintéticos utilizando Python

Também é possível utilizar o gerador diretamente em um script Python:

```python
from src.generator import generate_synthetic_population

data = generate_synthetic_population(
    n=1000,
    seed=42
)

print(data.head())
```

O parâmetro `n` define o número de registros gerados, enquanto `seed` permite reproduzir a mesma geração quando os parâmetros são mantidos.

### Executar o exemplo de avaliação

```bash
python test_synthhealth.py
```

Esse exemplo gera duas amostras sintéticas com sementes diferentes e demonstra a aplicação das métricas de comparação.

## Metodologia

O SynthHealth utiliza métodos estatísticos e probabilísticos para simular variáveis relacionadas à saúde.

A metodologia atual contempla:

1. Definição de distribuições estatísticas para as variáveis.
2. Geração de características demográficas.
3. Simulação de condições clínicas por meio de relações probabilísticas.
4. Simulação da utilização de serviços de saúde.
5. Geração de custos assistenciais com distribuição assimétrica.
6. Cálculo de métricas estatísticas para comparação entre conjuntos de dados.

A avaliação estatística permite investigar diferenças entre distribuições, dispersões e relações entre variáveis.

Na versão atual, o exemplo de avaliação compara amostras independentes produzidas pelo próprio gerador. Portanto, essa análise permite observar a consistência e a estabilidade estatística do processo de geração, mas não representa uma validação de fidelidade em relação a uma base de dados real.

## Limitações

O SynthHealth encontra-se em desenvolvimento. Algumas limitações importantes da versão atual são:

- Os parâmetros utilizados na geração são hipotéticos e ilustrativos.
- As distribuições não foram calibradas para representar uma população específica.
- Os dados gerados não possuem validação clínica.
- O indicador de risco é sintético e não representa um instrumento clínico validado.
- A avaliação atual não demonstra equivalência com dados reais.
- A geração de dados sintéticos, por si só, não garante privacidade ou proteção contra reidentificação.

Os resultados devem ser interpretados considerando essas limitações.

## Reprodutibilidade

O projeto utiliza sementes aleatórias configuráveis para permitir a reprodução das simulações.

Exemplo:

```python
data = generate_synthetic_population(
    n=5000,
    seed=42
)
```

Utilizar os mesmos parâmetros e a mesma versão do código permite reproduzir a geração, desde que o ambiente e as dependências sejam compatíveis.

## Aplicações potenciais

O SynthHealth pode apoiar atividades como:

- Ensino de estatística aplicada à saúde;
- Experimentação em Ciência de Dados;
- Desenvolvimento e teste de algoritmos de aprendizado de máquina;
- Estudos metodológicos sobre dados sintéticos;
- Demonstrações de técnicas de simulação;
- Avaliação de métodos de comparação estatística;
- Prototipagem de aplicações analíticas em saúde.

O projeto não substitui bases de dados clínicas validadas nem deve ser utilizado como fonte de evidências para decisões assistenciais.

## Licença

Este projeto está disponibilizado sob a licença **MIT**.

Consulte o arquivo [LICENSE](LICENSE) para obter os termos completos de utilização, modificação e distribuição.

## Como citar

Caso o projeto seja utilizado em trabalhos acadêmicos, pesquisas ou aplicações técnicas, recomenda-se citar a versão correspondente do software.

Modelo de referência:

> Breno Scaffo de Andrade Costa. SynthHealth: An Open-Source Framework for Synthetic Healthcare Data Generation and Statistical Fidelity Assessment. Versão 1.0.0. Zenodo, 2026. DOI: [DOI A SER ATRIBUÍDO].

O DOI será incluído após a publicação de uma versão arquivada no Zenodo.

## Autor

**Breno Scaffo de Andrade Costa**

Projeto desenvolvido na área de Ciência de Dados, com foco em geração de dados sintéticos, métodos estatísticos e aplicações em saúde.

## Repositório

GitHub: https://github.com/USERNAME/SynthHealth

## DOI

A ser atribuído após o registro da versão publicada no Zenodo.

---

**SynthHealth — Dados sintéticos, métodos estatísticos e Ciência de Dados aplicados à saúde.**
>>>>>>> 68f34c1 (Initial release of SynthHealth)
