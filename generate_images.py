#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import os

def create_solana_dashboard():
    # Create dashboard image
    img = Image.new('RGB', (1200, 600), color='#1a1a2e')
    draw = ImageDraw.Draw(img)
    
    # Header
    draw.rectangle([0, 0, 1200, 80], fill='#8b5cf6')
    
    # Title
    try:
        font_large = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", 32)
        font_medium = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", 18)
        font_small = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", 14)
    except:
        font_large = ImageFont.load_default()
        font_medium = ImageFont.load_default()
        font_small = ImageFont.load_default()
    
    # Title text
    draw.text((600, 40), "Solana Token Feed & Transfer App", fill='white', font=font_large, anchor='mm')
    
    # Navigation buttons
    draw.rectangle([50, 100, 250, 150], fill='#a855f7')
    draw.rectangle([300, 100, 500, 150], fill='#a855f7')
    draw.text((150, 125), "Cosmo", fill='white', font=font_medium, anchor='mm')
    draw.text((400, 125), "Transfer", fill='white', font=font_medium, anchor='mm')
    
    # Main content area
    draw.rectangle([50, 180, 1150, 580], fill='#2d3748')
    
    # Content cards
    draw.rectangle([80, 220, 580, 340], fill='#4a5568')
    draw.rectangle([620, 220, 1120, 340], fill='#4a5568')
    
    # Card content
    draw.text((100, 250), "Live Token Feed", fill='white', font=font_medium)
    draw.text((640, 250), "SOL Transfer Interface", fill='white', font=font_medium)
    
    # Footer
    draw.rectangle([0, 550, 1200, 600], fill='#8b5cf6')
    draw.text((600, 575), "Web3 DApp with Live Token Streaming & SOL Transfer", fill='white', font=font_small, anchor='mm')
    
    return img

def create_token_feed():
    # Create token feed image
    img = Image.new('RGB', (600, 400), color='#1a1a2e')
    draw = ImageDraw.Draw(img)
    
    # Header
    draw.rectangle([0, 0, 600, 60], fill='#8b5cf6')
    
    try:
        font_large = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", 20)
        font_medium = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", 14)
    except:
        font_large = ImageFont.load_default()
        font_medium = ImageFont.load_default()
    
    # Title
    draw.text((300, 30), "Live Token Feed", fill='white', font=font_large, anchor='mm')
    
    # Token cards
    for i in range(3):
        y_start = 80 + i * 90
        draw.rectangle([20, y_start, 580, y_start + 70], fill='#2d3748')
        
        # Token info
        draw.text((40, y_start + 20), f"Token {i + 1}", fill='white', font=font_medium)
        draw.text((40, y_start + 40), "Supply: 1,000,000", fill='white', font=font_medium)
        draw.text((40, y_start + 60), "Decimals: 6", fill='white', font=font_medium)
    
    return img

def create_transfer():
    # Create transfer interface image
    img = Image.new('RGB', (600, 400), color='#1a1a2e')
    draw = ImageDraw.Draw(img)
    
    # Header
    draw.rectangle([0, 0, 600, 60], fill='#8b5cf6')
    
    try:
        font_large = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", 20)
        font_medium = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", 14)
    except:
        font_large = ImageFont.load_default()
        font_medium = ImageFont.load_default()
    
    # Title
    draw.text((300, 30), "SOL Transfer Interface", fill='white', font=font_large, anchor='mm')
    
    # Form background
    draw.rectangle([50, 100, 550, 350], fill='#2d3748')
    
    # Form fields
    draw.rectangle([80, 130, 520, 170], fill='#4a5568')
    draw.rectangle([80, 200, 520, 240], fill='#4a5568')
    
    # Labels
    draw.text((80, 120), "Amount (SOL):", fill='white', font=font_medium)
    draw.text((80, 190), "Recipient Address:", fill='white', font=font_medium)
    
    # Button
    draw.rectangle([80, 280, 280, 320], fill='#8b5cf6')
    draw.text((180, 300), "Transfer SOL", fill='white', font=font_medium, anchor='mm')
    
    return img

if __name__ == "__main__":
    # Create images directory if it doesn't exist
    os.makedirs('images', exist_ok=True)
    
    # Generate images
    dashboard = create_solana_dashboard()
    token_feed = create_token_feed()
    transfer = create_transfer()
    
    # Save images
    dashboard.save('images/solana-app-dashboard.png')
    token_feed.save('images/solana-token-feed.png')
    transfer.save('images/solana-transfer.png')
    
    print("Generated Solana project images:")
    print("- solana-app-dashboard.png")
    print("- solana-token-feed.png") 
    print("- solana-transfer.png")
