Session-Based Prefix-Target Modeling
===================================

Colab-first pipeline for turning the RecSys 2015 / YOOCHOOSE click log into prefix→target training pairs. Everything happens inside `notebooks/session_based_prefix_target_datasets.ipynb`, which you can rerun end-to-end to recreate `data/processed/`.

## Notebook in a nutshell

1. **Setup & download** – mounts Drive, installs Kaggle CLI, pulls the 33M-row `yoochoose-clicks.dat`, and prints file sizes for quick checks.
2. **EDA & sorting** – loads the clicks table, reports key stats (sessions, items, session-length histogram), and globally sorts events by `session_id` + timestamp.
3. **Temporal split** – derives session end-times and slices train/valid/test by chronology (80/10/10) to avoid leakage.
4. **Filtering & remapping** – keeps train items with ≥5 interactions, drops sessions <2 events, optional session-length cap, and remaps `item_id` to contiguous ids.
5. **Pair generation** – streams prefix lists and next-item targets into Parquet (`train|valid|test_pairs.parquet`) plus an accompanying `item_map.json`.
6. **Validation & viz** – reloads the Parquet files, checks prefix length distributions/ID bounds, and includes optional Plotly timelines for sampled sessions.

## Outputs

| Artifact | Purpose |
| --- | --- |
| `data/processed/train_pairs.parquet` | Training prefixes/targets post-filtering |
| `data/processed/valid_pairs.parquet` | Chronological validation split |
| `data/processed/test_pairs.parquet` | Held-out evaluation split |
| `data/processed/item_map.json` | Original item → contiguous id lookup |

## Quick start

1. `pip install -r requirements.txt`
2. Open the notebook (locally or in Colab), upload your `kaggle.json`, run all cells.
3. Consume the Parquet outputs:
   ```python
   import pandas as pd
   train_pairs = pd.read_parquet("data/processed/train_pairs.parquet")
   ```

## Repo overview

```
├── data/        # external/raw/interim/processed
├── notebooks/   # notebook named session_based_prefix_target_datasets (1).ipynb
├── src/         # placeholder package for downstream code
├── requirements.txt
└── README.md
```

---

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
