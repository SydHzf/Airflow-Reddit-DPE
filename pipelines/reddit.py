import pandas as pd

from etl_functions.reddit import (
    connect,
    extract_posts,
    transform_data,
    load_data_to_csv,
)
from utils.constants import CLIENT_ID, SECRET, OUTPUT_PATH


def reddit_pipeline(file_name: str, subreddit: str, time_filter="day", limit=None):
    # connecting to reddit instance
    instance : Reddit = connect(CLIENT_ID, SECRET, "Reddit Pipeline Agent")
    # extraction
    posts :pd.DataFrame = extract_posts(instance, subreddit, time_filter, limit)
    post_df = pd.DataFrame(posts)
    # transformation
    post_df = transform_data(post_df)
    # loading to csv
    file_path = f"{OUTPUT_PATH}/{file_name}.csv"
    load_data_to_csv(post_df, file_path)

    return file_path
