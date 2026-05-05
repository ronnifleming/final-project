##code.py

#color questions and possible results
#based on natural coloring
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
        "description": "Light colors like lavender, baby blue, and light pink look great on you!"
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
            ("Other/dyed", {"earth": 1}),
        ]
    },
]



#jewelry results and questions
#based on lifestyle and comfort preferences as well as stylistic choices

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
        "description": "You want jewelry that adds a statement without feeling cumbersome. Go for jewel-forward options that allow you to customize the color that adds the most fitting sparkle to the rest of your look."
    },
    "pearl-forward": {
        "name": "Pearl-forward jewelry",
        "description": "You're a busy person who likes to complete their look with something elegant and timeless. Look for pearl necklaces (they can be choker-style or have pendants) and dangly pearl earrings."
    }
}

jewelry_scores = {key: 0 for key in jewelry_results.keys()}

jewelry_questions = [
    #the three below questions are based on practicality - dainty jewelry and pearl-basedtend to be best for active lifestyles, while chunky jewelrly is most impractical
    {
        "question": "How important is it to you that you can wear your jewelry for physical activities?",
        "answers": [
            ("Very", {"dainty": 1}),
            ("Somewhat", {"pearl-forward": 1}),
            ("Not at all", {"jewel-forward": 1, "chunky": 1}),
        ]
    },
    #new (elaborates on above)
     {
        "question": "If important, what physical activities do you plan to wear it for?",
        "answers": [
            ("All, including swimming and contact sports", {"dainty": 1, "pearl-forward": 1}),
            ("Moderate activities, such as walking and yoga.", {"jewel-forward": 1}),
            ("Not important/no activities", {"chunky": 1}),
        ]
    },
    {
       "question": "How do you feel about jewelry that makes noise?",
        "answers": [
            ("I want it to announce my arrival.", {"chunky": 1}),
            ("I'm not about it.", {"dainty": 1}),
            ("A bit of jangling is fine.", {"jewel-forward": 1, "pearl-forward": 1}),
        ]
    },
    #following question based on stylistic preferences; jewel-forward and chunky will be most noticeable, while dainty and pearl are more subtle
    {
        "question": "Do you want your jewelry to make a statement or simply complement the rest of your outfit?",
        "answers": [
            ("Make a statement!", {"jewel-forward": 1, "chunky": 1}),
            ("Just add a little razzle-dazzle to the rest of my outfit.", {"dainty": 1}),
            ("Maybe add a bit of elegance, nothing too bold.", {"pearl-forward": 1}),
        ]
    },
    #this is more personality-based; which do you want your jewelry to emulate?
    {
        "question": "Which do you like better, the beach or the mountains?",
        "answers": [
            ("The beach", {"pearl-forward": 1}),
            ("The mountains", {"jewel-forward": 1}),
            ("Neither", {"chunky": 1}), #chunky jewelry is less reminiscent of nature than the beach or mountains, and dainty jewelry fits equally well for all three
        ]
    }
]



#style results and questions
#based on personality: determining what style of clothing best suits someone's "vibe" and lifestyle


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
    #some more stylistic questions that might help highlight a style that is already drawn to - they already have stylistic preferences, this is helping compile them into a cohesive theme
    {
        "question": "Which pair of shoes are you picking?",
        "answers": [
            ("Strappy sandals", {"boho": 1}),
            ("Ankle boots", {"chic": 1}),
            ("Mary Janes", {"vintage": 1}),
            ("Air Jordans", {"streetwear": 1}),
        ]
    },
    #new - adding more about options they might already go for
    {
        "question": "Which would you layer with in cold weather?",
        "answers": [
            ("Leather jacket", {"chic": 1}),
            ("Adidas windbreaker", {"sporty": 1}),
            ("Embroidered jean jacket", {"boho": 1}),
            ("Mesh knit", {"beachy": 1}),
        ]
    },
    {
        "question": "Which accessory would you add?",
        "answers": [
            ("Chunky belt", {"streetwear": 1}),
            ("Headband", {"sporty": 1}),
            ("Bermuda bag", {"vintage": 1}),
            ("A paisley scarf", {"boho": 1}),
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
    print(f"\n** {section_name} **")
    for i, q_data in enumerate(questions, start=1):
        ask_question(q_data, i, scores)

    # Determine final result with tie-breaking
    max_score = max(scores.values())
    top_keys = [k for k, v in scores.items() if v == max_score]
    #chosen_key = random.choice(top_keys) #maybe keep this, or just say they're a tie between the two
    #chosen_result = results[chosen_key]

    #builds list of result dictionaries for all top keys rather than selecting one
    top_results = [
        {
            "key": key,
            #moved these three things from the below return statement
            "name": results[key]["name"],
            "description": results[key]["description"],
            "score": max_score,
        }
        for key in top_keys
    ]

    return {

        "max_score": max_score,
        "all_scores": scores,
        "top_keys": top_keys,
        "top_results": top_results,
    }

def print_score_breakdown(title, scores, results_lookup):
    """Print all scores in descending order."""
    print(f"\n{title} Breakdown: ")
    # Sort by score (high to low), then by key for consistency
    for key, score in sorted(scores.items(), key=lambda item: (-item[1], item[0])):
        name = results_lookup[key]["name"]
        print(f" {name}: {score}")


def main():
    print("\n\nWelcome to the PERSONAL BRANDING QUIZ! \nAfter taking this three-part quiz, you will be on your way to defining a personal style that uniquely suits your natural complexion, lifestyle, and interests.")
    print("\nStep 1: Find your color palette.")
    print("Step 2: Find your jewelry style.")
    print("Step 3: Determine the clothing style that best suits your personality!")

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


     # Colors

    print("\n\nColor Palette Result(s):")
    if len(color_result["top_keys"]) > 1:
        print("You matched multiple color palettes equally well: "
              + ", ".join(color_result["top_keys"]) + ".")
    for res in color_result["top_results"]:
        print(f"  {res['name']}")
        print(f"  {res['description']}")
        #print(f"  (Your score: {res['score']})\n")


    # Jewelry
    print("\n\nJewelry Style Result(s):")
    if len(jewelry_result["top_keys"]) > 1:
        print("You matched multiple jewelry types equally well: "
              + ", ".join(jewelry_result["top_keys"]) + ".")
    for res in jewelry_result["top_results"]:
        print(f"  {res['name']}")
        print(f"  {res['description']}")
        #print(f"  (Your score: {res['score']})\n")

    # Clothing Style
    print("\n\nClothing Style Result(s):")
    if len(style_result["top_keys"]) > 1:
        print("You matched multiple clothing styles equally well: "
              + ", ".join(style_result["top_keys"]) + ".")
    for res in style_result["top_results"]:
        print(f"  {res['name']}")
        print(f"  {res['description']}")
        #print(f"  (Your score: {res['score']})\n")



    # ---- Ask if user wants full score breakdown ----
    see_breakdown = input("\nWould you like to see your full score breakdown for each section? (y/n): ")
    if see_breakdown.strip().lower().startswith("y"):
        print_score_breakdown("Color Palette", color_result["all_scores"], color_results)
        print_score_breakdown("Jewelry Style", jewelry_result["all_scores"], jewelry_results)
        print_score_breakdown("Clothing Style", style_result["all_scores"], style_results)

if __name__ == "__main__":
    main()


##I asked Harvard AI Sandbox to help properly format the run_section function and lines 214-216 to correctly count up the point tally by asking it how to design a code that had multiple steps so that the results from each step would be separately tallied up and stored.
