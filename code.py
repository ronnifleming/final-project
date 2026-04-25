##code.py
import random

#color questions and possible results

color_results = {
    "jewel": {
        "name": "Jewel Tones",
        "description": "Deep colors like sapphire, emerald, and ruby will best bring out your features!"
    },
    "earth": {
        "name": "Earth Tones",
        "description": "Colors like olive, caramel, and dusty pink best complement your coloring."
    },
    "pastel": {
        "name": "Pastel Tones",
        "description": "Light colors like lavender, baby blue, and light pink look great on you! "
    }
}

color_scores = {key: 0 for key in color_results.keys()}

color_questions = [
    {
        "question": "What color are your eyes?",
        "answers": [
            ("Blue", {"jewel": 1}),
            ("Green", {"earth": 1}),
            ("Brown", {"pastel": 1}),
        ]
    },
    {
        "question": "What color are your skin undertones? (Hint: if your veins look green, you are likely warm. If your veins look blue, you are likely cool.)",
        "answers": [
            ("Warm", {"earth": 1, "pastel": 1}),
            ("Cool", {"jewel": 1}),
            ("I'm not sure", {}), #see if that works
        ]
    },
    {
        "question": "What color is your hair?",
        "answers": [
            ("Brown", {"jewel": 1, "earth": 1}),
            ("Blonde", {"pastel": 1}),
            ("Red", {"earth": 1}),
            ("Black", {"jewel": 1}),
            ("Other/dyed", {}),
        ]
    }
]



#jewelry results and questions 

jewelry_results = {
    "chunky": {
        "name": "Chunky jewelry",
        "description": "You're a bold person, and you want your jewelry to reflect that. Go for statement pieces, like chunky rings, bangles of any style, long necklaces and dangly earrings."
    },
    "dainty": {
        "name": "Dainty jewelry",
        "description": "You want something classy and practical to add a bit of sparkle to your already stylish outfit. Go for slimmer rings, huggie hoop earrings, and consider layering one or two short necklaces."
    },
    "jewel-forward": {
        "name": "Jewel-forward jewelry",
        "description": "You want jewelry that adds a statement without feeling cumbersome. Go for jewel-forward options that allow you to customize the color that adds the most fitting sparkle to the rest of your look. "
    },
    "pearl-forward": {
        "name": "Pearl-forward jewelry",
        "description": "You're a busy person who likes to complete their look with something elegant and timeless. Look for pearl necklaces (they can be choker-style or have pendants) and dangly pearl earrings.'"
    }
}

jewelry_scores = {key: 0 for key in jewelry_results.keys()}

jewelry_questions = [
    {
        "question": "How important is it to you that you can wear your jewelry for physical activities, including swimming or exercising?",
        "answers": [
            ("Very", {"dainty": 1}),
            ("Somewhat", {"pearl-forward": 1}),
            ("Not at all", {"jewel-forward": 1, "chunky": 1}),
        ]
    },
    {
        "question": "Do you want your jewelry to make a statement or simply complement the rest of your outfit?",
        "answers": [
            ("Make a statement!", {"jewel-forward": 1, "chunky": 1}),
            ("Just add a little razzle-dazzle to the rest of my outfit.", {"dainty": 1}),
            ("Maybe add a bit of elegance, nothing too bold.", {"pearl-forward": 1}),
        ]
    },
    {
        "question": "Which do you like better, the beach or the mountains?",
        "answers": [
            ("The beach", {"pearl-forward": 1}),
            ("The mountains", {"jewel-forward": 1}),
            ("Neither", {"chunky": 1}),
        ]
    },
    {
       "question": "How do you feel about jewelry that makes noise?",
        "answers": [
            ("I want it to announce my arrival.", {"chunky": 1}),
            ("I'm not about it.", {"dainty": 1}),
            ("A bit of jangling is fine.", {"jewel-forward": 1, "pearl-forward": 1}),
        ]
    }
]



#style results and questions


style_results = {
    "chic": {
        "name": "Chic",
        "description": "Look into sophisticated styles like slip dresses, dark wash jeans, and blazers."
    },
    "boho": {
        "name": "Boho",
        "description": "Look into flowy, colorful clothing with unique patterns."
    },
    "vintage": {
        "name": "Vintage",
        "description": "Vintage clothing can be whatever catches your eye at the thrift store, but if you're looking for guidance, start by searching for patterns like polka-dots, stripes, and plaid."
    },
    "beachy": {
        "name": "Beachy",
        "description": "Go for sundresses, flowy tops, and linens."
    },
    "streetwear": {
        "name": "Streetwear",
        "description": "You'd look fabulous in varsity-style jackets with baggy jeans or cargos and some platform boots or Nike Jordans."
    },
    "sporty": {
        "name": "Sporty",
        "description": "Try styling some of your sports jerseys with a pair of ripped jeans chunky sneakers. Consider investing in a signature headband."
    }
}


# 2. Set up a structure to hold scores for each result
style_scores = {key: 0 for key in style_results.keys()}

# 3. Define the quiz questions.
# Each answer now maps to a dict of {result_key: points}.
style_questions = [
    {
        "question": "What's your ideal day off?",
        "answers": [
            ("Getting brunch and going shopping", {"chic": 1}),
            ("Surfing and getting smoothies", {"beachy": 1}),
            ("Visiting secondhand bookstores", {"vintage": 1}),
            ("Watching a sports game", {"sporty": 1})
        ]
    },
    {
        "question": "Which item do you/would you collect?",
        "answers": [
            ("Records", {"vintage": 1}),
            ("Pressed flowers", {"boho": 1}),
            ("Seashells", {"beachy": 1}),
            ("Team merchandise", {"sporty": 1}),
        ]
    },
    {
        "question": "Which physical activity would you go for?",
        "answers": [
            ("Basketball", {"sporty": 1}),
            ("Pilates", {"chic": 1}),
            ("Skateboarding", {"streetwear": 1}),
            ("Volleyball", {"beachy": 1}),
        ]
    },
    {
       "question": "Which concert would you attend?",
        "answers": [
            ("Stevie Nicks", {"boho": 1}),
            ("Kendrick Lamar", {"streetwear": 1}),
            ("Sublime", {"beachy": 1}),
            ("SZA", {"chic": 1}),
        ]
    },
    {
        "question": "Which pair of shoes are you picking?",
        "answers": [
            ("Strappy sandals", {"boho": 1}),
            ("Ankle boots", {"chic": 1}),
            ("Mary Janes", {"vintage": 1}),
            ("Air Jordans", {"streetwear": 1}),
        ]
    }
]


#asking and collecting input on each question
def ask_question(q_data, q_number, scores_dict):
    """Ask one question and update the given scores_dict."""
    print(f"\nQuestion {q_number}: {q_data['question']}")
    for i, (answer_text, result_mapping) in enumerate(q_data["answers"], start=1):
        print(f"  {i}. {answer_text}")

    while True:
        choice = input("Enter the number of your choice: ")
        if choice.isdigit():
            choice = int(choice) 
            if 1 <= choice <= len(q_data["answers"]):
                break
        print("Invalid choice. Please enter a valid number.")

    _, result_mapping = q_data["answers"][choice - 1]
    for result_key, pts in result_mapping.items():
        scores_dict[result_key] += pts


#determining the result for each section based on category with the most points
def run_section(section_name, questions, results, scores):
    """Run one section of the quiz and return the chosen result info."""
    print(f"\n=== {section_name} ===")
    for i, q_data in enumerate(questions, start=1):
        ask_question(q_data, i, scores)

    # Determine final result with tie-breaking
    max_score = max(scores.values())
    top_keys = [k for k, v in scores.items() if v == max_score]
    chosen_key = random.choice(top_keys) #maybe keep this, or just say they're a tie between the two
    chosen_result = results[chosen_key]

    return {
        "key": chosen_key,
        "score": max_score,
        "all_scores": scores,
        "top_keys": top_keys,
        "name": chosen_result["name"],
        "description": chosen_result["description"],
    }


def main():
    print("Welcome to style quiz! *come back and jazzify this*")
    print("Step 1: Find out your color palette.")
    print("Step 2: Find out your jewelry style.")
    print("Step 3: Identify the clothing style that best suits your personality!")

    # ---- Section 1: Colors ----
    color_result = run_section(
        "Step 1: Your Color Palette", #not sure about this line
        color_questions,
        color_results,
        color_scores,
    )

    # ---- Section 2: Jewelry ----
    jewelry_result = run_section(
        "Step 2: Your Jewelry Style",
        jewelry_questions,
        jewelry_results,
        jewelry_scores,
    )

    # ---- Section 3: Style ----
    style_result = run_section(
        "Step 3: Your Clothing Style",
        style_questions,
        style_results,
        style_scores,
    )
    # ---- Final Combined Summary ----
    print("\n==============================")
    print("         YOUR RESULTS         ")
    print("==============================")

    print("\nColor Palette Result:")
    print(f"  {color_result['name']}")
    print(f"  {color_result['description']}")
    print(f"  (Score: {color_result['score']})")

    print("\nJewelry Style Result:")
    print(f"  {jewelry_result['name']}")
    print(f"  {jewelry_result['description']}")
    print(f"  (Score: {jewelry_result['score']})")

    print("\nClothing Style Result:")
    print(f"  {style_result['name']}")
    print(f"  {style_result['description']}")
    print(f"  (Score: {style_result['score']})")

    # Explaining that random was used when there were ties; might be changing this
    if len(color_result["top_keys"]) > 1:
        print("\n[Color palette tie among:", ", ".join(color_result["top_keys"]), "- one chosen at random.]")
    if len(jewelry_result["top_keys"]) > 1:
        print("[Jewelry type tie among:", ", ".join(jewelry_result["top_keys"]), "- one chosen at random.]")
    if len(style_result["top_keys"]) > 1:
        print("[Style tie among:", ", ".join(style_result["top_keys"]), "- one chosen at random.]")

if __name__ == "__main__":
    main()


##I asked Harvard AI Sandbox to help properly format the run_section function and lines 214-216 to correctly count up the point tally by asking it how to design a code that had multiple steps so that the results from each step would be separately tallied up and stored. 