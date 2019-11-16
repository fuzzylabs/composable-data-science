# Introduction

In this repository you'll find some examples of how to write composable data science code using Python and [Jupyter](https://jupyter.org).

Jupyter is both a blessing and a curse to data science projects. While the notebook environment makes it very easy to experiment and explore data, it also makes productionising the finished product difficult because it encourages mixing together code responsible for data preparation, feature engineering, analysis, modelling and testing.

We need code that can be decomposed into simple components that function well together, but without giving up on notebooks. 

## Accompanying blog post

The Fuzzy Labs [Composable Data Science blog post](http://fuzzylabs.ai/blog/composable-data-science) explains the details and motivations behind this repository.

# Data

The data used for this example comes from a popular [Kaggle](https://kaggle.com) competition for predicting house prices. The original dataset is [here](https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data).

# Preparing your Python environment

You'll need to have Python 3 along with `pip` and `virtualenv` installed on your system. To initialise `virtualenv` and install dependencies including Jupyter, run the following:

```
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

Subsequently, to activate the environment run `source env/bin/activate` again.

# Running the notebook

Having set up `virtualenv` and installed dependencies, run `jupyter notebook` from the root of the repository. In the Jupyter web interface ([http://localhost:8888](http://localhost:8888)) navigate to one of the notebook files in the [notebooks](notebooks/) directory.

# How this repository is organised

## Notebooks

Both notebooks implement a solution to the [Kaggle house price competition](https://www.kaggle.com/c/house-prices-advanced-regression-techniques), which is solved with a Random Forest Regressor.

* [House Prices original](notebooks/house-prices-original.ipynb) - all code in one notebook.
* [House Prices refactored](notebooks/house-prices-refactored.ipynb) - the same notebook but with core logic refactored into composable functions.

## Data

The [data](data/) directory contains a training and test dataset in CSV format along with a data description file.

## Components

The [components](components/) directory contains Python code that is referenced in the refactored house price notebook.
