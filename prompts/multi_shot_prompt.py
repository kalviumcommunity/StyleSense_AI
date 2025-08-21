"""
StyleSense AI - Multi Shot Prompting  
Fashion styling with multiple examples
"""

def multi_shot_fashion_prompt(occasion, weather, style_preference, body_type, budget=None):
    """Multi-shot prompt with multiple styling examples"""
    budget_text = f"{budget} budget" if budget else "flexible budget"
    
    return f"""
StyleSense AI - Multiple styling examples:

EXAMPLE 1 - Professional: "interview, cold, minimalist, pear, medium"
→ Navy blazer, charcoal pants, white blouse, block heels
→ High-waist balances pear shape, structured pieces create clean lines

EXAMPLE 2 - Casual: "brunch, warm, bohemian, hourglass, low" 
→ Off-shoulder top, denim shorts, sandals, kimono layer
→ Off-shoulder emphasizes waist, flowy fabrics suit bohemian style

EXAMPLE 3 - Evening: "dinner, cool, romantic, rectangle, high"
→ Wrap dress, strappy heels, delicate blazer
→ Wrap style creates curves, midi length elongates

YOUR TASK: "{occasion}, {weather}, {style_preference}, {body_type}, {budget_text}"
Follow detailed approach from examples.
"""


def multi_versatility_prompt(wardrobe_pieces, lifestyle_needs):
    """Multi-shot versatile styling prompt"""
    pieces_text = ", ".join(wardrobe_pieces)
    needs_text = ", ".join(lifestyle_needs)
    
    return f"""
Versatile styling examples:

WARDROBE 1: blazer, jeans, white shirt, heels, sneakers
→ Professional: blazer + dress pants + shirt + heels
→ Casual: jeans + shirt + sneakers (blazer tied around waist)
→ Date: jeans + shirt + blazer + heels

WARDROBE 2: cardigan, striped tee, white jeans, boots, skirt  
→ Work: skirt + tee + cardigan + boots
→ Weekend: jeans + tee + cardigan + sneakers

YOUR WARDROBE: {pieces_text}
NEEDS: {needs_text}
Create multiple versatile combinations.
"""


def multi_color_coordination(base_colors, accent_preferences, skin_tone):
    """Multi-shot color coordination examples"""
    base_list = ", ".join(base_colors)
    accent_list = ", ".join(accent_preferences)
    
    return f"""
Color coordination examples:

WARM TONES: navy + cream + coral
→ Navy grounds, cream lightens, coral adds warmth
→ Gold jewelry ties together

COOL TONES: charcoal + white + emerald  
→ Charcoal sophistication, white freshness, emerald pop
→ Silver accessories enhance cool undertones

YOUR PALETTE: Base: {base_list}, Accents: {accent_list}, Skin: {skin_tone}
Create harmonious combinations with rationale.
"""
