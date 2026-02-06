# Day 5 — Pandas Grouping & Aggregations

## Overview
Day 5 focuses on **grouping and aggregating data using Pandas**.  
These are essential skills to summarize datasets, find trends, and prepare for visualizations.

We will use the **IMDB dataset** as an example.

---

## Learning Objectives
- Understand how to **group data** using `groupby()`
- Learn common **aggregations**: `mean()`, `sum()`, `count()`
- Sort and filter grouped data
- Handle missing values in numeric and categorical columns
- Practice analyzing trends in movies, genres, and directors

---

## Core Concepts

### 1. Grouping
- Use `groupby()` to group data by one or more columns.
- Common use cases: average rating per genre, total votes per director.

### 2. Aggregations
- Functions like `mean()`, `sum()`, `count()` summarize grouped data.
- Can combine with `sort_values()` to find top values.

### 3. Handling Missing Data
- Numeric columns: fill missing values with mean or median
- Categorical columns: fill missing values with 'Unknown' or 'Not Rated'

---

## Key Pandas Methods
- `df.groupby('Column')` — group by a column
- `agg()` — apply aggregation functions
- `sort_values()` — sort results
- `value_counts()` — count unique values
- `fillna()` — handle missing data
- `dropna()` — remove missing rows

---

## Example Analyses
- Average IMDB rating per Genre
- Number of movies per Genre
- Top 10 Directors by average Meta_score
- Top 10 Directors by total votes
- Top 10 highest rated movies
- Director with highest average rating (min 3 movies)

---

## Practice Tasks
1. Find average IMDB rating for movies released after 2010 by genre.
2. Count movies per Certificate type.
3. Identify the director with the highest average rating (consider only directors with at least 3 movies).

---

## Files
- `Day5_Pandas_Grouping_Aggregations.ipynb` — Notebook with all code examples and practice tasks
- `README.md` — Day 5 notes and explanations

---
