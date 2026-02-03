# Day 2 — 3 V’s of Big Data & Data Types

## Overview
Day 2 focuses on understanding the **core characteristics of Big Data** and different **types of data**.
These concepts help in choosing the right tools and methods later.

---

## The 3 V’s of Big Data

Big Data is commonly defined using three main properties called the **3 V’s**.

---

### 1. Volume
Volume refers to the **amount of data**.

Examples:
- Millions of users data
- Billions of images and videos
- Large transaction records

Why it matters:
- A single computer cannot store or process very large data
- Distributed storage and processing are required

---

### 2. Velocity
Velocity refers to the **speed at which data is generated and processed**.

Examples:
- Live stock market prices
- Real-time GPS tracking
- Social media posts every second

Why it matters:
- Delayed processing can cause loss of value
- Real-time or near real-time systems are needed

---

### 3. Variety
Variety refers to the **different formats of data**.

Examples:
- Text data (reviews, comments)
- Images and videos
- Logs and JSON files

Why it matters:
- Not all data fits into tables
- Different processing methods are required

---

## Types of Data

---

### Structured Data
Structured data is:
- Organized in rows and columns
- Easy to store and query

Examples:
- CSV files
- Excel sheets
- SQL database tables

Used tools:
- Excel
- SQL
- Pandas DataFrames

---

### Unstructured Data
Unstructured data:
- Has no fixed format
- Is difficult to analyze directly

Examples:
- Text reviews
- Images
- Videos
- Audio files

Used tools:
- NLP libraries
- Computer Vision tools
- Deep Learning models

---

### Semi-Structured Data
Semi-structured data:
- Has some structure but not strict tables

Examples:
- JSON files
- XML files
- Log files

Commonly used in:
- APIs
- Web applications
- Cloud systems

---

## Real-World Example
A movie streaming platform stores:
- User details (structured)
- Watch history (structured)
- Reviews (unstructured text)
- Logs (semi-structured)

All these together form **Big Data**.

---

## Practice Task
- Write 5 examples of:
  - Structured data
  - Unstructured data
- Identify the 3 V’s for any one real application

---

## Key Takeaways
- Big Data is defined by Volume, Velocity, and Variety
- Data exists in different formats
- Not all data can be stored in tables
- Understanding data types helps in tool selection
