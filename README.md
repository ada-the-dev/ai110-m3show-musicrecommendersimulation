# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Real-world recommendation systems have a lot of nuance in their workings and different types of data to make inferences from. For example, these systems may compare users to each other, so that similar users can receive similar recommendations, or so that the system can further reinforce that this recommendation is worth recommending to another similar user. 

There may also be factors like watch time, skips, paused, subscriptions/followed creators, time of day, location, and the device currently being used that can be utilized to provide a recommendation for the user. A collection of data based on the user's preferences, circumstances, and whims can be analyzed and extracted from to generate quantifiable results that determine whether a recommendation should be made to a user.

Now, for my particular music recommender simulation, a weighted proximity scoring algorithm will be used in which every song is scored against a user's profile, and then these songs will be ranked against each other on this scoring. The algorithm will be a  "mood-first" algorithm since this has the heaviest weight. The top three ranking songs will be recommended to the user. This algorithm will reward a song's closeness to a user's profile.

Each song will receive a score in the range [0.0, 1.0]. The score is a weighted sum of four sub-scores, and then this score is divided by the total possible points (8 points) to normalize it. In particular, the genre, mood, energy, and acousticness features of each song will scored against the user profile's genre, mood, energy, and acousticness.

While this recommendation system will be able to better recommend songs that match a user's mood and overall preference, one potential drawback to the weight decision, and, therefore the recommedation algorithm, is that users who greatly value genre over mood (a.k.a. "genre-loyalists") will have a higher chance of being exposed to song genres that do align with their preferences and music-related boundaries.

Here is a Mermaid Live that describes the data flow of my proposed and implemented music recommendation system:

flowchart TD
    A[(songs.csv)] -->|load_songs| B[Song List]
    C[User Profile\ngenre · mood · energy · target_acousticness] --> D

    B -->|one song at a time| D

    subgraph SCORE["score_song — repeats for every song"]
        D[Genre match?\n× WEIGHT_GENRE 2]
        D --> E[Mood match?\n× WEIGHT_MOOD 3]
        E --> F["Energy proximity\n1 - abs song.energy - target x 2"]
        F --> G["Acousticness proximity\n1 - abs song.acousticness - target x 1"]
        G --> H[Sum raw score / 8\nnormalized score 0.0 to 1.0]
    end

    H --> I["(song, score) pairs"]
    I --> J[Sort all pairs descending by score]
    J --> K[Slice top-k]
    K --> L[Top K Recommendations]

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this


---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}  

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

Give your recommender a name, for example:

> VibeFinder 1.0

---

## 2. Intended Use

- What is this system trying to do
- Who is it for

Example:

> This model suggests 3 to 5 songs from a small catalog based on a user's preferred genre, mood, and energy level. It is for classroom exploration only, not for real users.

---

## 3. How It Works (Short Explanation)

Describe your scoring logic in plain language.

- What features of each song does it consider
- What information about the user does it use
- How does it turn those into a number

Try to avoid code in this section, treat it like an explanation to a non programmer.

---

## 4. Data

Describe your dataset.

- How many songs are in `data/songs.csv`
- Did you add or remove any songs
- What kinds of genres or moods are represented
- Whose taste does this data mostly reflect

---

## 5. Strengths

Where does your recommender work well

You can think about:
- Situations where the top results "felt right"
- Particular user profiles it served well
- Simplicity or transparency benefits

---

## 6. Limitations and Bias

Where does your recommender struggle

Some prompts:
- Does it ignore some genres or moods
- Does it treat all users as if they have the same taste shape
- Is it biased toward high energy or one genre by default
- How could this be unfair if used in a real product

---

## 7. Evaluation

How did you check your system

Examples:
- You tried multiple user profiles and wrote down whether the results matched your expectations
- You compared your simulation to what a real app like Spotify or YouTube tends to recommend
- You wrote tests for your scoring logic

You do not need a numeric metric, but if you used one, explain what it measures.

---

## 8. Future Work

If you had more time, how would you improve this recommender

Examples:

- Add support for multiple users and "group vibe" recommendations
- Balance diversity of songs instead of always picking the closest match
- Use more features, like tempo ranges or lyric themes

---

## 9. Personal Reflection

A few sentences about what you learned:

- What surprised you about how your system behaved
- How did building this change how you think about real music recommenders
- Where do you think human judgment still matters, even if the model seems "smart"

