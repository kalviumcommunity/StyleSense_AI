"""
StyleSense AI - User Prompt Templates
Assignment: System and User Prompt using RTFC Framework
Author: vishalm342
Date: 2025-08-19
"""

def create_outfit_request(occasion, weather, style_preference, body_type):
    """
    Creates a basic user prompt for outfit recommendations
    """
    return f"""
    I need outfit advice for the following situation:
    
    Occasion: {occasion}
    Weather: {weather}
    My style preference: {style_preference}
    Body type: {body_type}
    
    Please provide a complete outfit recommendation following your structured format.
    """

def create_wardrobe_help(request_type, details):
    """
    Creates a user prompt for general wardrobe assistance
    """
    return f"""
    I need help with: {request_type}
    Details: {details}
    
    Please provide your expert fashion advice.
    """

# Example usage (for demonstration only)
EXAMPLE_REQUEST = create_outfit_request(
    occasion="casual dinner date",
    weather="cool evening, 18°C",
    style_preference="minimalist chic",
    body_type="petite"
)