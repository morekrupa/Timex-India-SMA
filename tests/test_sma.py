import sys
from pathlib import Path

import pandas as pd

sys.path.append(str(Path(__file__).resolve().parents[1]))

from analysis import load_data, facebook_engagement, instagram_engagement  # noqa: E402


def test_facebook_dataset():
    data = pd.read_csv("data/fb_cleaned_data.csv")

    assert len(data) > 0
    assert "likes" in data.columns


def test_instagram_dataset():
    data = pd.read_csv("data/insta_cleaned_data.csv")

    assert len(data) > 0
    assert "likesCount" in data.columns
    assert "commentsCount" in data.columns


def test_website_dataset():
    data = pd.read_csv("data/website_cleaned_data.csv")

    assert len(data) > 0
    assert "Product ID" in data.columns
    assert "Category" in data.columns
    assert "Selling Price" in data.columns
    assert "MRP" in data.columns


def test_all_datasets():
    datasets = load_data()

    assert len(datasets) == 8


def test_facebook_engagement():
    data = pd.read_csv("data/fb_cleaned_data.csv")

    result = facebook_engagement(data)

    assert result >= 0


def test_instagram_engagement():
    data = pd.read_csv("data/insta_cleaned_data.csv")

    result = instagram_engagement(data)

    assert result >= 0


def test_website_prices():
    data = pd.read_csv("data/website_cleaned_data.csv")

    assert (data["Selling Price"] >= 0).all()
    assert (data["MRP"] >= 0).all()


def test_website_categories():
    data = pd.read_csv("data/website_cleaned_data.csv")

    assert "Category" in data.columns
    assert data["Category"].notna().sum() > 0
    