# Sentiment Analysis on US 2020 Elections using Twitter Data on Apache Spark

## Description

This repository contains code and Notebooks used for discerning sentiment from tweets for predicting the results of the
US 2020 elections.

## Repository Structure

The Repository has three primary directories:

1. **data/** - This directory contains additional datasets used. Primary datasets needed to run code were removed for space but can be accessed via link below.
2. **notebooks/** - this directory contains Jupyter notebooks that were used for analysing sentiment from twitter
   records. The directory has the following contents:
   1. _Sentiment Classifier.ipynb_ - Primary notebook containing a compilation of analysis done from the other
      notebooks.
   2. _EDA.ipynb_ - Notebook containing Exploratory Data Analysis steps.
   3. _Sentiment Classifier_LR.ipynb_ - Notebook exploring the PySpark Logistic Regression model.
   4. _Sentiment Classifier_NB.ipynb_ - Notebook exploring the PySpark Naive Bayes model.
   5. _k-Means.ipynb_ - Notebook exploring the PySpark k-Means model.
   6. _Scalability Metrics.ipynb_ - Notebook exploring scalability metrics: Speed-Up, Scale-Up, Size-Up.
   7. _scaleup.csv_, _sizeup.csv_, _speedup.csv_ - These are the outputs generated from notebook _Scalability
      Metrics.ipynb_ which are used for plotting these runtimes.
   8. **metrics/** - this directory contains the code for calculating the various scalability metrics from notebook
      _Scalability Metrics.ipynb_.
   9. **data/** - this directory contains intermediate data output from notebook  _Scalability Metrics.ipynb_ for
      calculaing the various metrics.
3. **src/** - this directory contains utility functions and custom transformers that are used across different Jupyter
   Notebooks in notebooks/. The directory has the following contents:
   1. **jobs/** and **utils/** - these directories contain the utility functions used across Jupyter Notebooks.
   2. **transforms/** - this directory contains custom Transformers we've implemented.

## Authors and acknowledgment

[Abel Johny](mailto:psxaj3@nottingham.ac.uk),
[Mathew Aniyan](mailto:psxma18@nottingham.ac.uk),
[Jacob Aniyan](mailto:psxja14@nottingham.ac.uk),
[Jui Ting Tsai](mailto:psxjt6@nottingham.ac.uk),
[Brendan Ezekiel Agnelo Vaz](mailto:psxbv1@nottingham.ac.uk),
[Kwabena Asafo-Adjei](mailto:psxka11@nottingham.ac.uk)

## Gitlab

Link: https://projects.cs.nott.ac.uk/psxaj3/PB02.git

## Primary US elections tweet dataset

Link: https://www.kaggle.com/datasets/manchunhui/us-election-2020-tweets

## Additional dataset link

Link: https://www.kaggle.com/datasets/callummacpherson14/2020-us-presidential-election-results-by-state

