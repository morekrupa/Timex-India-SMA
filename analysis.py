import pandas as pd


def load_data():
    facebook = pd.read_csv("data/fb_cleaned_data.csv")
    twitter = pd.read_csv("data/twitter_cleaned_data.csv")
    linkedin = pd.read_csv("data/linkedin_cleaned_data.csv")
    reddit = pd.read_csv("data/reddit_cleaned_data.csv")
    website = pd.read_csv("data/website_cleaned_data.csv")
    youtube = pd.read_csv("data/yt_cleaned_data.csv")
    instagram = pd.read_csv("data/insta_cleaned_data.csv")
    google_maps = pd.read_csv("data/gm_cleaned_data.csv")

    return {
        "facebook": facebook,
        "twitter": twitter,
        "linkedin": linkedin,
        "reddit": reddit,
        "website": website,
        "youtube": youtube,
        "instagram": instagram,
        "google_maps": google_maps
    }


def facebook_engagement(data):
    return data["likes"].sum()


def instagram_engagement(data):
    return (
        data["likesCount"].sum()
        + data["commentsCount"].sum()
    )


if __name__ == "__main__":
    datasets = load_data()

    print(
        "Facebook Engagement:",
        facebook_engagement(datasets["facebook"])
    )

    print(
        "Instagram Engagement:",
        instagram_engagement(datasets["instagram"])
    )
