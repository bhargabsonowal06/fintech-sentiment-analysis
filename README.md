Fintech App Sentiment & Risk Analysis Using NLP
Overview

This project performs large-scale sentiment and risk analysis of user reviews across three major Indian fintech applications:

Google Pay

PhonePe

Paytm

Using Natural Language Processing (NLP) and machine learning, the project analyzes 183,000+ real app reviews to identify dissatisfaction patterns and potential churn signals.

The goal is to automatically detect at-risk users (negative sentiment) and uncover product improvement opportunities from user feedback.

Problem Statement

Fintech apps receive thousands of user reviews daily across app stores. Manually analyzing this feedback is impractical.

This project builds an automated NLP pipeline to:

Classify user sentiment

Detect dissatisfied users likely to churn

Benchmark sentiment across competing apps

Extract key complaint themes driving negative feedback

Dataset

Source: Google Play Store user reviews

The dataset contains 183,876 reviews across three fintech apps.

Main fields used:

Column	Description
content	User review text
score	Star rating (1–5)
app_name	App name (Google Pay, PhonePe, Paytm)
thumbsUpCount	Helpful votes

After preprocessing, additional fields were engineered:

cleaned_text

processed_text

sentiment

binary_sentiment

Methodology
1. Text Preprocessing

The following NLP pipeline was applied:

Lowercasing

URL and punctuation removal

Tokenization

Stopword removal

Lemmatization

Libraries used:

NLTK

Pandas

Regex

2. Feature Engineering

Text data was converted into numerical features using TF-IDF Vectorization.

Configuration:

10,000 features

Unigrams + Bigrams

Minimum document frequency = 5

This representation captures meaningful keywords while reducing noise.

3. Model Development

Several models were tested:

Model	Purpose
Naive Bayes	Baseline classifier
Logistic Regression	Linear classification
Linear SVM	Final production model

Due to strong class imbalance, class weighting was applied.

4. Binary Risk Classification

The original three-class sentiment labels were simplified into:

Label	Meaning
Positive	Satisfied user
Negative	At-risk / dissatisfied user

Neutral reviews were removed to improve classification clarity.

Final Model Performance

Balanced Linear SVM

Metric	Score
Accuracy	90.1%
Negative F1 Score	0.75
Positive F1 Score	0.94

The model effectively identifies dissatisfied users who may churn.

Key Product Insights
Sentiment Benchmark

Paytm shows the highest positive sentiment (~82%)

Google Pay shows the highest negative proportion (~30%)

PhonePe lies between the two competitors

Complaint Themes by App
Google Pay

Primary issues:

App reliability problems

Card/payment failures

Transaction execution issues

Example keywords:

cant, work, card, doesnt, use

PhonePe

Primary issues:

Recharge/payment failures

Incorrect transaction charges

Example keywords:

charge, recharge, money

Paytm

Primary issues:

Account-related problems

Customer service dissatisfaction

Example keywords:

account, customer, service

Visual Insights
Sentiment Distribution

Sentiment by App

Model Confusion Matrix

Negative Complaint WordCloud

Project Structure
fintech-sentiment-analysis/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   └── sentiment_analysis.ipynb
│
├── src/
│   ├── preprocessing.py
│   └── modeling.py
│
├── outputs/
│   └── figures/
│
├── requirements.txt
└── README.md
Tech Stack

Python

Pandas

NLTK

Scikit-learn

Matplotlib

Seaborn

WordCloud

Business Impact

This approach can help fintech product teams:

Detect churn-risk users automatically

Monitor sentiment trends across product releases

Identify reliability issues early

Prioritize product and UX improvements

Future Improvements

Potential extensions:

BERT-based sentiment modeling

Topic modeling for complaint clustering

Real-time sentiment monitoring pipeline

Dashboard visualization for product teams

Author

Bhargab Sonowal

Data Analytics | Product Analytics | Machine Learning