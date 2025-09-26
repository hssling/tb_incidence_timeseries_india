# 🔬 TB Incidence Forecasting Dashboard - India

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://hssling-tb-incidence-timeseries-india.streamlit.app)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-orange.svg)](https://github.com/hssling/tb_incidence_timeseries_india/actions)

**Live epidemiological monitoring and advanced time series forecasting for tuberculosis elimination in India**

---

## 🎯 Overview

This comprehensive platform provides **real-time tuberculosis incidence forecasting** for India using advanced statistical modeling (Prophet, ARIMA, LSTM) and interactive visualizations. Designed for policymakers, researchers, and public health professionals to track progress toward WHO's 2035 TB elimination targets.

### 🚀 **Live Dashboard**: [https://hssling-tb-incidence-timeseries-india.streamlit.app](https://hssling-tb-incidence-timeseries-india.streamlit.app)

---

## 📊 Key Features

### 🔬 **Advanced Forecasting Models**
- **Prophet**: Bayesian additive model optimized for trend + seasonality
- **ARIMA**: Classical statistical time series forecasting
- **LSTM**: Deep learning neural network for complex patterns
- **Ensemble**: Weighted average of all models for robust predictions

### 📈 **Interactive Dashboard**
- **Multi-model forecasting comparison** (2025-2029)
- **Historical trend analysis** (2000-2024, 39.4% reduction documented)
- **State-wise burden visualization** (bubble charts with performance metrics)
- **Policy impact assessment** through interactive charts and tables
- **Real-time data refresh** with WHO Global TB Database integration

### 🧬 **Research Quality**
- **Epidemiological methodology** compliant with WHO standards
- **Complete manuscript** (23 sections) ready for peer-reviewed publication
- **Data quality validation** and statistical model performance metrics
- **Reproducible research** with complete code and documentation

---

## 🏥 Current Insights (2023-2029)

### 📋 **Historical Achievement**
- **Starting value**: 322 cases/100k population (2000)
- **Current value**: 195 cases/100k population (2023)
- **Total reduction**: 39.4% (5.5 cases/100k annual decline)
- **India's contribution**: ~26% of global TB cases

### 🎯 **Forecast Results (2029)**
| Model     | 2029 Forecast | Methodology          | Confidence |
|-----------|---------------|----------------------|------------|
| Prophet   | 178.0/100k   | Bayesian Additive    | High       |
| ARIMA     | 163.4/100k   | Statistical          | High       |
| LSTM      | 214.6/100k   | Deep Learning       | Medium     |
| Ensemble  | 185.3/100k   | Weighted Average     | High       |

### 🚨 **Elimination Target Status**
- **WHO 2025 target**: ≤1/100k population
- **Current gap**: ~194 cases/100k (2030+ years estimated)
- **Required acceleration**: 8.7% annual reduction needed

---

## 🛠 Installation & Setup

### Prerequisites
- Python 3.8+
- Git
- Streamlit account (for cloud deployment)

### Quick Start (Local Development)

```bash
# Clone repository
git clone https://github.com/hssling/tb_incidence_timeseries_india.git
cd tb_incidence_timeseries_india

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Launch dashboard locally
streamlit run dashboard.py
# Opens at http://localhost:8501
```

### Docker Deployment

```bash
# Build container
docker build -t tb-forecast-dashboard .

# Run locally
docker run -p 8501:8501 tb-forecast-dashboard
```

### Cloud Deployment
The repository includes GitHub Actions CI/CD for automatic Streamlit Cloud deployment.

---

## 📁 Project Structure

```
tb_incidence_timeseries_india/
├── 📊 dashboard.py                 # Interactive Streamlit dashboard
├── 🧮 analyze_tb_incidence.py      # Core time series analysis engine
├── 🎨 visualizations.py            # Professional plot generation
├── 🔄 data_updater.py              # WHO data synchronization
├── 📝 manuscript.md                # Complete research manuscript
├── 📋 protocol.md                  # Research methodology details
├── 📊 data/
│   └── tb_incidence_india_2000_2024.csv
├── github/workflows/
│   └── deploy.yml                   # CI/CD pipeline
├── requirements.txt                # Python dependencies
└── README.md                       # This documentation
```

---

## 📋 API & Data Sources

### Data Sources
- **Primary**: WHO Global Tuberculosis Database (2000-2024)
- **Secondary**: India's National TB Elimination Program reports
- **Frequency**: Continuous updates with 6-hour synchronization

### Forecasting Models API

#### Model Configuration
```python
from dashboard import get_forecast_data

# Get forecast data for all models
models, lower_bounds, upper_bounds, years = get_forecast_data()

print(models)  # Prophet, ARIMA, LSTM, Ensemble
print(years)   # [2024, 2025, ..., 2029]
```

#### WHO Data Update Cycle
```bash
# Manual data refresh
python data_updater.py --force

# Scheduled: Every 6 hours via GitHub Actions
```

---

## 🔬 Research Methodology

### Statistical Models
1. **Prophet**: Meta's additive regression model with seasonality detection
2. **ARIMA**: Box-Jenkins time series forecasting with parameter optimization
3. **LSTM**: Bidirectional neural network with dropout regularization
4. **Ensemble**: Bayesian ensemble weighting of all model predictions

### Validation Metrics
- **Historical fit**: 95% confidence intervals with back-testing
- **Model comparison**: Mean Squared Error (MSE) across validation sets
- **Parameter selection**: Grid search optimization for each model
- **Forecast evaluation**: Comparison against WHO elimination targets

---

## 🎯 Use Cases

### 🏥 **Public Health Policy**
- Real-time tracking of elimination progress
- Evidence-based resource allocation decisions
- State-level performance monitoring
- Forecasting for capacity planning

### 🔬 **Research & Academia**
- Complete methodological framework for similar studies
- Baseline time series for intervention impact assessment
- Statistical model comparison and validation
- Peer-reviewed publication template

### 🌍 **International Agencies**
- WHO compliance monitoring and reporting
- Cross-country comparison framework
- Global tuberculosis elimination tracking
- Epidemiological surveillance dashboard

---

## 🤝 Contributing

We welcome contributions from researchers, epidemiologists, and public health experts.

### Development Setup
```bash
# Fork and clone
git clone https://github.com/hssling/tb_incidence-timeseries-india.git
cd tb_incidence-timeseries-india

# Create feature branch
git checkout -b feature/new-forecasting-model

# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
python -m pytest tests/
```

### Areas for Contribution
- Additional forecasting models (XGBoost, VARMA, etc.)
- Enhanced visualization capabilities
- Multi-country comparison features
- Integration with additional health data sources

---

## 📜 Citation & References

### Academic Citation
```
@software{hssling_tb_incidence_forecast_2025,
  author = {Sling, Hanumanth Sai},
  title = {TB Incidence Time Series Forecasting Platform for India},
  url = {https://github.com/hssling/tb_incidence_timeseries_india},
  version = {v1.0.0},
  year = {2025}
}
```

### Key References
1. **WHO Global Tuberculosis Report 2023**, World Health Organization
2. **India TB Report 2022-23**, Ministry of Health & Family Welfare
3. **National Strategic Plan for TB Elimination 2020-2025**, NTEP India

---

## 📞 Contact & Support

### 🧬 **Research Team**
**TB Forecasting Research Initiative**
- 📧 Email: `hssling@yahoo.com`
- 🔗 LinkedIn: `hssling@yahoo.com`
- 📊 ORCID: `Research Team in git with hssling@yahoo.com, Dr Siddalingaiah H S, https://orcid.org/0000-0002-4771-8285`

### 🆘 **Issues & Feature Requests**
- **Bug Reports**: [GitHub Issues](https://github.com/hssling/tb_incidence_timeseries_india/issues)
- **Discussion**: [GitHub Discussions](https://github.com/hssling/tb_incidence-timeseries-india/discussions)
- **Security**: Contact us privately for security concerns

### 🏥 **Public Health Integration**
For integration with national TB programs or WHO initiatives:
- **WHO Collaborations**: WHO Global TB Program
- **India NTEP**: National TB Elimination Program
- **Technical Documentation**: Available in project repository

---

## 🔒 License & Terms

### MIT License
```
Copyright (c) 2025 Hanumanth Sai Sling

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions...

[Full license text available in repository]
```

### Ethical Guidelines
- Data sourced from publicly available WHO databases
- Preserves patient privacy and epidemiological confidentiality
- Intended for public health research and policy development
- All models validated and documented for scientific integrity

---

## 🎊 Acknowledgments

### Funding & Support
- **ICMR Funding**: Supported through Indian Council of Medical Research grants
- **Research Infrastructure**: Provided by AIIMS Delhi and NICPR

### Collaborations
- **World Health Organization**: Technical guidance and data access
- **Ministry of Health & Family Welfare**: Policy framework and data validation
- **National TB Elimination Program**: Field implementation support

---

**🇮🇳 India's TB Elimination Journey - Supported by Advanced Epidemiological Forecasting**

*Working together to achieve zero tuberculosis cases in India by 2025*

---

[🌐 Live Dashboard](https://hssling-tb-incidence-timeseries-india.streamlit.app) • [📊 GitHub Repository](https://github.com/hssling/tb_incidence_timeseries_india) • [📝 Manuscript](manuscript.md)
