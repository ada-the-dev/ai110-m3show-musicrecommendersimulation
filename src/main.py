"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    # Starter example profile
    user_prefs = {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.80,
        "target_acousticness": 0.2,
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\n" + "=" * 60)
    print(f"  Top {len(recommendations)} Recommendations")
    print(f"  Profile: genre={user_prefs['genre']} | mood={user_prefs['mood']} | energy={user_prefs['energy']} | acousticness={user_prefs['target_acousticness']}")
    print("=" * 60)

    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"\n#{rank}  {song['title']}  (Score: {score:.3f})")
        print(f"    Artist : {song['artist']}")
        print(f"    Genre  : {song['genre']}  |  Mood: {song['mood']}")
        print(f"    Why:")
        for reason in explanation.split("; "):
            print(f"      • {reason}")
    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
