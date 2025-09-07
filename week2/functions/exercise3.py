"""

Write a function normalize_scores(scores) that takes a list of numbers and
returns a new list scaled to 0–100 (divide by max and multiply by 100). Handle an
empty list by returning an empty list.
"""

# Function to normalize scores
def normalize_scores(scores):
    # If the input list is empty, return an empty list
    if not scores:
        return []
    
    # Find the maximum score
    max_score = scores[0]
    for score in scores:
        if score > max_score:
            max_score = score
            
    return [(score / max_score) * 100 for score in scores]

# Example scores list
scores = [50, 75, 100, 25]

print(normalize_scores(scores))
