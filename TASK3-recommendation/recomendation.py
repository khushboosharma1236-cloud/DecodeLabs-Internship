import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Step 1: Dataset bana diya - 8 Movies with 3 categories
data = {
    'Movie': ['3 Idiots', 'Dangal', 'KKHH', 'Avengers', 'Hera Pheri', 
              'Titanic', 'Baahubali', 'Chup Chup Ke'],
    'Comedy': [1, 0, 1, 0, 1, 0, 0, 1],
    'Action': [0, 1, 0, 1, 0, 0, 1, 0],
    'Romance': [1, 0, 1, 0, 0, 1, 0, 1]
}

df = pd.DataFrame(data)
print("Available Movies Dataset:")
print(df)
print("\n" + "="*50 + "\n")

# Step 2: User se pasand pucho - 0 ya 1 dalna hai
print("Rate your preference 0 = No, 1 = Yes")
user_comedy = int(input("Do you like Comedy? "))
user_action = int(input("Do you like Action? "))
user_romance = int(input("Do you like Romance? "))

user_pref = np.array([[user_comedy, user_action, user_romance]])

# Step 3: Similarity nikal lo
movie_features = df[['Comedy', 'Action', 'Romance']]
similarity_scores = cosine_similarity(user_pref, movie_features)[0]

# Step 4: Score ko dataset me add kar do
df['Similarity'] = similarity_scores

# Step 5: Top 3 recommend kar do
recommended = df.sort_values(by='Similarity', ascending=False).head(3)

print("\n" + "="*50)
print("TOP 3 MOVIES RECOMMENDED FOR YOU:")
print("="*50)
for index, row in recommended.iterrows():
    print(f"{row['Movie']} - Match: {row['Similarity']*100:.1f}%")

print("\nProject 3 Complete!")