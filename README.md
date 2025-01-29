# Salary Prediction: a Data Science Sample Project

## About

This repository presents a supervised learning problem where the goal is to predict workers' salaries. It contains everything needed to make the project fully reproducible (data, code, results, publications) and also [generates a published website on GitHub Pages](https://mpru.github.io/salary_prediction/website/index.html)

[Please visit this link to explore this project.](https://mpru.github.io/salary_prediction/website/index.html)

## Repository Organization

- **Folder** `code`: 

  - `modulos.py`: some auxiliary functions created.
  - `.qmd` files: contain the code developed for all stages of the analysis, along with descriptive text and results. I chose to use Quarto instead of Jupyter Notebooks because Quarto provides greater flexibility in publishing or sharing files and facilitates version control integration. Each of these files is later converted into a webpage.

- **Folder** `data`: contains the three raw datasets, processed data, partitions for model validation, and other data-related files.

- **File** `environment.yml`: specifies the *conda environment* in which the project was executed.

- **Folder** `docs`, **Folder** `website`, **File** `_quarto.yml`, and **File** `.nojekyll`: files included for website creation and deployment.
