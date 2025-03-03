# Breast-Cancer-Analysis-and-ML

## Overview

This project focuses on the analysis of breast cancer data and the application of machine learning techniques to predict the presence of breast cancer. The goal is to build a predictive model that can assist in early detection and diagnosis.

## Dataset

The dataset used in this project is the Breast Cancer Wisconsin (Diagnostic) dataset, which is available from the UCI Machine Learning Repository. It contains features computed from a digitized image of a fine needle aspirate (FNA) of a breast mass.

## Features

The dataset includes the following features:
- Radius
- Texture
- Perimeter
- Area
- Smoothness
- Compactness
- Concavity
- Concave points
- Symmetry
- Fractal dimension

## Installation

To run this project, you need to have Python installed along with the following libraries:
- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn
- fastapi
- uvicorn

You can install the required libraries using pip:
```bash
pip install pandas numpy scikit-learn matplotlib seaborn fastapi uvicorn
```

## Usage

1. Clone the repository:
```bash
git clone /g:/depi/technical/projects/Breast-Cancer-Analysis-and-ML
```
2. Navigate to the project directory:
```bash
cd Breast-Cancer-Analysis-and-ML
```
3. Run the FastAPI server:
```bash
uvicorn main:app --reload
``` 

To run this project, you need to have Python installed along with the following libraries:
- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn

You can install the required libraries using pip:
```bash
pip install pandas numpy scikit-learn matplotlib seaborn
```

## Project Structure

- `data/`: Contains the dataset.
- `notebooks/`: Jupyter notebooks for data exploration and model building.
- `scripts/`: Python scripts for data preprocessing, model training, and evaluation.
- `results/`: Directory to save model results and plots.

## Methodology

1. **Data Preprocessing**: Handle missing values, normalize features, and split the data into training and testing sets.
2. **Exploratory Data Analysis (EDA)**: Visualize the data to understand the distribution and relationships between features.
3. **Model Building**: Train various machine learning models such as Logistic Regression, Decision Trees, Random Forest, and Support Vector Machines.
4. **Model Evaluation**: Evaluate the models using metrics like accuracy, precision, recall, and F1-score. Use cross-validation to ensure robustness.

## Results

The best performing model achieved an accuracy of X% on the test set. The confusion matrix and ROC curve are provided in the results directory.

## Conclusion

This project demonstrates the application of machine learning techniques to predict breast cancer. The models built can assist in early detection, potentially leading to better patient outcomes.

## References

- [UCI Machine Learning Repository: Breast Cancer Wisconsin (Diagnostic) Data Set](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic))
- [Scikit-learn Documentation](https://scikit-learn.org/stable/)