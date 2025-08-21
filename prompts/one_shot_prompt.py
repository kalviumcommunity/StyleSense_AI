"""
StyleSense AI - One Shot Prompting
Fashion styling with single example
"""

def outfit_with_example_prompt(occasion, weather, style_preference, body_type, budget=None):
    """One-shot prompt with styling example"""
    budget_text = f"{budget} budget" if budget else "flexible budget"
    
    return f"""
StyleSense AI styling example:

EXAMPLE: "brunch, warm, bohemian, hourglass, medium budget"
→ Outfit: cream off-shoulder top, terracotta wide-leg pants, nude sandals
→ Colors: cream, terracotta, gold accents  
→ Tips: off-shoulder balances hourglass, high-waist accentuates waist

NOW STYLE: "{occasion}, {weather}, {style_preference}, {body_type}, {budget_text}"
Use same format above.
"""


def wardrobe_building_example(current_pieces, style_goal, budget):
    """Wardrobe building with example approach"""
    pieces_text = ", ".join(current_pieces)
    
    return f"""
Wardrobe building example:
Current: basic tees, jeans → Goal: professional → Budget: $400
Strategy: Add blazer ($70), dress pants ($50), heels ($60) = 8+ new outfits

Your task:
Current: {pieces_text}
Goal: {style_goal}  
Budget: {budget}
Provide strategic additions using same approach.
"""


def seasonal_transition_example(current_outfit, target_season, style_type):
    """Seasonal styling with example"""
    return f"""
Seasonal transition example:
Summer dress → Fall: add denim jacket, switch sandals to boots, add scarf

Your task: 
"{current_outfit}" → {target_season} ({style_type})
Show adaptation strategy.
"""