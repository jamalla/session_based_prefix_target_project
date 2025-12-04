# Recommended E-Learning Datasets for Session-Based Recommendation

Following the review of the Mandarine dataset, which was found unsuitable for deep learning due to its small size, the following datasets are recommended. These datasets provide the volume, granularity, and sequential nature required to train robust session-based recommendation models (e.g., GRU4Rec, BERT4Rec, SASRec).

## 1. EdNet (Top Recommendation)

**EdNet** is the largest public dataset for AI in Education (AIEd), collected from the AI tutoring platform "Santa". It is hierarchical, allowing you to choose the level of granularity you need.

*   **Volume**: ~131 million interactions.
*   **Users**: ~784,000 students.
*   **Content**: ~13,000 problems, ~1,000 lectures.
*   **Structure**:
    *   **KT1**: Question-solving logs (User, Item, Time, Correctness). Most similar to standard session-based data.
    *   **KT2-KT4**: Includes richer interactions like watching lectures, purchasing items, and reading explanations.
*   **Why it's better**:
    *   **Massive Scale**: Enough data to train large transformers without overfitting.
    *   **Long Sequences**: Users engage over long periods, providing rich history for sequential modeling.
    *   **Granularity**: Captures exact timestamps, allowing for precise session segmentation.

## 2. MOOCCubeX

**MOOCCubeX** is a large-scale knowledge-centered repository for MOOCs, sourced from XuetangX (one of the largest MOOC platforms in China).

*   **Volume**: ~296 million behavioral data points.
*   **Users**: ~3.3 million students.
*   **Content**: ~4,200 courses, ~230,000 videos.
*   **Features**:
    *   Fine-grained concepts and prerequisite relations.
    *   Video watching behaviors (start, pause, seek) and exercise logs.
*   **Why it's better**:
    *   **Rich Context**: Excellent for content-aware or knowledge-aware recommendation models.
    *   **Real-world Behavior**: Captures actual learning behaviors (video consumption) rather than just ratings.

## 3. KDD Cup 2015 (XuetangX)

While older, this dataset from the KDD Cup 2015 competition focuses on predicting dropouts but contains valuable interaction logs.

*   **Volume**: ~39 courses, ~79,000 users.
*   **Interactions**: Logs of video watching, problem accessing, and wiki viewing.
*   **Why it's better**:
    *   **Benchmark Usage**: Frequently used in educational data mining research.
    *   **Event-Based**: Good for modeling "next-event" prediction in a session.

## Summary Comparison

| Feature | Mandarine (Current) | EdNet (Recommended) | MOOCCubeX (Recommended) |
| :--- | :--- | :--- | :--- |
| **Interactions** | ~3.6k | **~131M** | **~296M** |
| **Users** | ~800 | ~784k | ~3.3M |
| **Avg. Seq Length** | ~4.5 | **~441** | High |
| **Suitability** | Debugging only | **Production / Research** | **Production / Research** |

**Action Plan**:
1.  Download **EdNet-KT1** (simplest format) to start.
2.  Preprocess it similarly to the current pipeline (User, Item, Time).
3.  Train the session-based model on this larger corpus.
