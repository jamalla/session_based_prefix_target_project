# Mandarine Dataset Review for Session-Based Recommendation

## EDA Review & Findings

1.  **Dataset Overview**:
    *   **Volume**: The dataset contains **3,659 interactions**, **822 unique users**, and **776 unique items**.
    *   **Timeframe**: Data spans from **September 2018 to September 2021** (~3 years).
    *   **Features**: `user_id`, `item_id`, `watch_percentage`, `created_at`, `rating`.

2.  **Data Distribution**:
    *   **Interactions per User**: On average, each user has only **~4.45 interactions** over the entire 3-year period.
    *   **Sparsity**: The data is extremely sparse (99.4%).
    *   **Ratings**: The ratings are heavily skewed towards positive values, with a mean of **8.57/10**. Most ratings are likely 10.
    *   **Watch Percentage**: The distribution is likely bimodal, with most values clustered around 100% (completed) or 0% (started but dropped).

3.  **Session Characteristics**:
    *   Since the average user history is only ~4.5 items long, splitting this into sessions (e.g., using a 30-minute inactivity gap) will likely result in **extremely short sessions** (mostly length 1 or 2).
    *   There is very little sequential signal to learn from.

## Suitability for Session-Based Models

**Verdict: NOT SUITABLE for training robust Deep Learning models.**

This dataset is **too small** to effectively train modern session-based recommendation models (like GRU4Rec, SASRec, or BERT4Rec), which typically require tens or hundreds of thousands of interactions to learn meaningful item transition patterns.

*   **Pros**:
    *   Clean data structure (User, Item, Time).
    *   Contains explicit signals (`watch_percentage`) which could be useful for weighting.
*   **Cons**:
    *   **Insufficient Volume**: 3.6k rows is insufficient for deep learning. The model will likely overfit immediately or fail to converge.
    *   **Short Sequences**: With < 5 interactions per user on average, there are almost no long sequences to model.
    *   **Low Density**: The item co-occurrence patterns will be very weak.

## Recommendation

1.  **Use for Debugging Only**: You can use this dataset to **test your code pipeline** (e.g., ensuring your data loader, preprocessing, and training loop work without errors) because it will run very fast.
2.  **Switch Datasets**: For actual model training and evaluation, you should use a standard benchmark dataset like:
    *   **RecSys Challenge 2015 (Yoochoose)**
    *   **Diginetica**
    *   **MovieLens 1M** (treated as sequential)
    *   **Amazon Reviews** (Beauty or Electronics categories)
3.  **Alternative Modeling**: If you *must* use this specific dataset, consider simpler approaches like **Association Rules (Apriori)** or **Item-KNN**, which work better with small data than deep neural networks.
