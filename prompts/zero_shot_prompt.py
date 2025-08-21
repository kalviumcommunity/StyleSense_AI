"""
StyleSense AI - Zero Shot Prompting
Direct fashion styling without examples
"""

def generate_outfit_prompt(occasion, weather, style_preference, body_type, budget=None):
    """Generate zero-shot outfit recommendation prompt"""
    budget_text = f"within {budget} budget" if budget else "flexible budget"
    
    return f"""
You are StyleSense AI fashion stylist.

REQUEST: {occasion}, {weather}, {style_preference} style, {body_type} figure, {budget_text}

PROVIDE:
1. Outfit (top, bottom, shoes)
2. Colors (2-3 shades)
3. Accessories 
4. Body-type tips
5. Weather notes

Be practical and confidence-boosting.
"""


def analyze_wardrobe_prompt(current_items, style_goals):
    """Generate wardrobe analysis prompt"""
    items_text = ", ".join(current_items)
    
    return f"""
Analyze wardrobe: {items_text}
Goal: {style_goals}

Provide:
1. Missing pieces
2. Current outfit combos  
3. Buy priorities
4. Optimization tips
"""


def color_coordination_prompt(skin_tone, hair_color, eye_color, preferred_colors=None):
    """Generate color palette prompt"""
    prefs = f", likes {', '.join(preferred_colors)}" if preferred_colors else ""
    
    return f"""
Create color palette for: {skin_tone} skin, {hair_color} hair, {eye_color} eyes{prefs}

Recommend:
1. Best colors
2. Neutrals
3. Accents  
4. Colors to avoid
"""