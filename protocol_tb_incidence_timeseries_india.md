# Time Series Analysis of Tuberculosis Incidence in India (2000-2024): Trends, Forecasting, and Policy Impact Assessment

## Study Title
**Time Series Analysis of Tuberculosis Occurrence in India: Epidemiological Trends, Forecasting Models, and Policy Impact Assessment (2000-2024)**

## Background
India accounts for nearly one-quarter of the global tuberculosis (TB) burden, with an estimate of 2.8 million new TB cases annually and 220,000 TB deaths per year (WHO, 2022). As the world's largest TB epidemic, India's TB control efforts have significant global implications. This study employs advanced time series analysis to understand long-term TB incidence trends, forecast future burden, and assess the impact of national TB control programs.

## Research Objectives

### Primary Objectives
1. **Epidemiological Trend Analysis**: Characterize TB incidence patterns in India from 2000-2024
2. **Seasonal and Cyclical Assessment**: Identify seasonality patterns and cyclical variations
3. **Forecasting**: Generate 5-year TB incidence forecasts (2025-2029)
4. **Policy Impact Evaluation**: Assess effectiveness of National TB Elimination Program (2019-2025)
5. **Public Health Policy Formulation**: Provide evidence-based recommendations for TB control

### Secondary Objectives
1. **Structural Break Analysis**: Identify critical intervention points and policy changes
2. **Model Performance Evaluation**: Compare statistical and machine learning approaches
3. **Uncertainty Quantification**: Provide confidence intervals for forecasts
4. **Interactive Visualization**: Develop web-based dashboard for policy makers

## Methodology

### Study Design
Longitudinal epidemiological time series analysis (24 years, 2000-2024)

### Data Sources
1. **World Health Organization (WHO)**: Annual TB incidence reports (2000-2023)
2. **Ministry of Health & Family Welfare, India**: National TB Control Program data
3. **Central TB Division (CTD)**: Annual TB reports and surveillance data
4. **Indian Council of Medical Research (ICMR)**: Epidemiological research data
5. **National TB Elimination Program (NTEP)**: Comprehensive reporting (2019-present)
6. **WHO Global TB Report**: Annual statistical publications

### Time Series Models

#### Statistical Approach
- **ARIMA (AutoRegressive Integrated Moving Average)**: Classical time series methodology
- **SARIMA (Seasonal ARIMA)**: Accounting for seasonal patterns
- Parameter Estimation: BIC/AIC minimization for optimal p,d,q parameters

#### Machine Learning Approach
- **Prophet (Meta/Facebook)**: Bayesian additive model with trend, seasonality, holidays
- **LSTM Neural Networks**: Deep learning sequence modeling
  - Architecture: 50 units, lookback=24 months, training samples=200 epochs
  - Features: Multiple timestep inputs, sequence predictions

#### Comparative Performance Metrics
- Mean Squared Error (MSE)
- Root Mean Square Error (RMSE)
- Mean Absolute Error (MAE)
- Akaike Information Criterion (AIC)
- Bayesian Information Criterion (BIC)

### Statistical Analysis

#### Stationarity Testing
- Augmented Dickey-Fuller (ADF) test
- KPSS test
- First-order differences (d=1) for non-stationary series
- Seasonal decomposition (STL decomposition)

#### Seasonal Analysis
- Periodogram analysis (monthly incidence patterns)
- Seasonal decomposition
- Autocorrelation function (ACF) analysis
- Partial autocorrelation function (PACF) analysis

#### Forecasting Horizons
- 1-year forecasts (tactical planning)
- 3-year forecasts (strategic planning)
- 5-year forecasts (long-term policy)
- 95% confidence intervals for all forecasts

### Data Management

#### Inclusion Criteria
- National-level incidence rates (per 100,000 population)
- Annual data points (2000-2024)
- WHO and Government of India verified sources
- Complete case analysis (no imputation)

#### Data Cleaning
- Outlier detection and validation
- Consistency checks across sources
- Population denominator adjustments
- Missing data assessment

### Policy Intervention Analysis

#### Program Evaluation Periods
- **Pre-NTEP Era** (2000-2018): Revised National TB Control Program
- **NTEP Era** (2019-2025): National TB Elimination Program
- **COVID-19 Impact Period** (2020-2022): Lockdown and healthcare disruption effects

#### Intervention Points
- TB drug sales regulation (2012)
- Universal access to diagnostics (2013)
- TB-cough hotline implementation (2013)
- Nikshay Poshan Yojana (2018 nutritional support)
- National TB Elimination Programme (2019)

### Ethical Considerations
- Public health surveillance data (no individual patient identifiers)
- Epidemiological research (exempt from formal ethics review)
- WHO and Government of India data usage permissions
- Standard research ethics compliance

## Expected Outcomes

### Research Outputs
1. **Peer-reviewed Manuscript**: 25-30 page research paper
2. **Interactive Dashboard**: Web-based visualization platform
3. **Policy Brief**: Executive summary for decision makers
4. **Data Package**: Complete datasets and code repository
5. **Technical Appendices**: Methodological details and validation

### Policy Recommendations
1. **Strategic Planning**: Evidence-based intervention targeting
2. **Resource Allocation**: Forecast-driven budget planning
3. **Evaluation Framework**: Program effectiveness monitoring
4. **Future Scenarios**: Multiple forecasting scenarios for policy planning
5. **Sanctions Monitoring**: Track progress toward elimination goals

### Innovation Elements
- **Real-time Forecasting**: Operational forecasting dashboard
- **Multi-model Ensemble**: Combined statistical and ML approaches
- **Interactive Policy Tools**: Web-based decision support system
- **Open Data Integration**: Automated WHO database integration

## Timeline
- **Phase 1**: Data acquisition and preprocessing (Week 1-2)
- **Phase 2**: Exploratory analysis and modeling (Week 3-6)
- **Phase 3**: Forecasting and validation (Week 7-8)
- **Phase 4**: Policy analysis and manuscript development (Week 9-12)
- **Phase 5**: Dashboard development and validation (Week 13-14)

## Resources Required

### Data Sources
- WHO Global Health Observatory API
- Ministry of Health & Family Welfare India
- National TB Elimination Programme database
- Academic and research literature

### Computing Resources
- Time series analysis software (Python/R)
- Statistical computing environment
- Interactive dashboard platform (Streamlit/Shiny)
- High-performance computing for neural network training

### Team Expertise
- Epidemiologist/TB expert
- Statistical modeling specialist
- Data scientist/machine learning engineer
- Public health policy advisor

This comprehensive time series analysis will provide critical insights into India's TB epidemiology and inform national TB elimination strategies for the next decade.
