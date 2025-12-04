import pandas as pd
import numpy as np

def analyze_sessions(file_path):
    print(f"Loading {file_path}...")
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print("File not found.")
        return

    # Convert created_at to datetime
    df['created_at'] = pd.to_datetime(df['created_at'])
    
    # Sort
    df = df.sort_values(['user_id', 'created_at'])
    
    # Calculate time difference
    df['time_diff'] = df.groupby('user_id')['created_at'].diff()
    
    # Define session threshold (e.g., 30 minutes)
    SESSION_THRESHOLD = pd.Timedelta(minutes=30)
    
    # Identify session breaks: New user OR time gap > threshold
    # The first row for each user is always a new session (time_diff is NaT)
    df['is_new_session'] = (df['time_diff'].isna()) | (df['time_diff'] > SESSION_THRESHOLD)
    
    # Assign session IDs
    df['session_id'] = df['is_new_session'].cumsum()
    
    # Stats
    num_users = df['user_id'].nunique()
    num_items = df['item_id'].nunique()
    num_interactions = len(df)
    num_sessions = df['session_id'].max()
    
    session_lengths = df.groupby('session_id').size()
    avg_session_length = session_lengths.mean()
    median_session_length = session_lengths.median()
    
    print("-" * 30)
    print("DATASET STATISTICS")
    print("-" * 30)
    print(f"Users: {num_users}")
    print(f"Items: {num_items}")
    print(f"Interactions: {num_interactions}")
    print(f"Total Sessions (30m gap): {num_sessions}")
    print(f"Avg Session Length: {avg_session_length:.2f}")
    print(f"Median Session Length: {median_session_length}")
    print(f"Max Session Length: {session_lengths.max()}")
    print("-" * 30)
    print("Session Length Distribution:")
    print(session_lengths.value_counts().sort_index().head(10))
    print("-" * 30)
    
    # Check suitability
    short_sessions = (session_lengths <= 1).sum()
    print(f"Sessions with length 1: {short_sessions} ({short_sessions/num_sessions:.2%})")
    
    if num_interactions < 10000:
        print("WARNING: Dataset is extremely small (< 10k interactions).")
    if avg_session_length < 2:
        print("WARNING: Average session length is very short.")
    if short_sessions / num_sessions > 0.5:
        print("WARNING: Majority of sessions are single interactions.")

if __name__ == "__main__":
    analyze_sessions('notebooks/data/mandarine-dataset/explicit_ratings_en.csv')
