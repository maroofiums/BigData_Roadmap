# Day4_Pandas_Selection_Filtering

Perfect, Maroof.
Chalo **Day 4 — Pandas Data Exploration & Handling Missing Data** ka professional **README.md** bana dete hain. Easy English, GitHub-ready, notebook-ready structure.

Save as:
👉 `Day4_Pandas_Exploration.md`

---

````markdown
# Day 4 — Pandas Data Exploration & Handling Missing Data

## Overview
Day 4 focuses on **exploring datasets** in Pandas and **handling missing or incorrect data**.  
Before analysis or visualization, understanding the dataset and cleaning it is critical.

---

## Learning Objectives
- Explore dataset structure
- Identify missing or null values
- Understand basic statistics
- Filter and select relevant data

---

## Step 1 — Inspect the Dataset

### Key Pandas Methods
- `df.head()` — First 5 rows
- `df.tail()` — Last 5 rows
- `df.shape` — Rows and columns
- `df.columns` — Column names
- `df.info()` — Column data types and non-null counts
- `df.describe()` — Summary statistics (numeric columns)

> Tip: Always start by inspecting your dataset before analysis.

---

## Step 2 — Handling Missing Data

### Identify Missing Values
```python
df.isnull().sum()
````

### Options to Handle Missing Values

1. **Remove missing rows**

```python
df.dropna(inplace=True)
```

2. **Fill missing values**

```python
df['Column'].fillna(value=0, inplace=True)
```

3. **Keep missing values** (if relevant for analysis)

> Mentor Tip: Don’t blindly drop missing data — think about impact.

---

## Step 3 — Data Exploration

### Filtering and Selecting Data

* Select columns:

```python
df['Rating']
```

* Select multiple columns:

```python
df[['Title','Rating']]
```

* Filter rows:

```python
df[df['Rating'] > 7]
```

### Aggregation & Grouping

* Group by a column to calculate average:

```python
df.groupby('Genre')['Rating'].mean()
```

> Tip: `groupby` is very useful for exploring trends in data.

---

## Step 4 — Practice Tasks

1. Explore the **IMDB dataset**:

   * Check first 10 rows
   * Check missing values
   * Column types and unique values
2. Handle missing data:

   * Drop or fill missing values
3. Filter movies with rating > 8
4. Find average rating per genre

---