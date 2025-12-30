# Style CSS i animacje dla Kalambury Zuzanny

def get_custom_css():
    return """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;500;600;700&display=swap');
    
    /* ===== GŁÓWNE STYLE ===== */
    .stApp {
        background: linear-gradient(135deg, #FF6B9D 0%, #C44FE2 100%);
        font-family: 'Quicksand', sans-serif;
    }
    
    /* Ukryj domyślny header Streamlit */
    header[data-testid="stHeader"] {
        background: transparent;
    }
    
    /* ===== ANIMOWANE SERDUSZKA W TLE ===== */
    .hearts-container {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        overflow: hidden;
        z-index: 0;
    }
    
    .heart {
        position: absolute;
        font-size: 20px;
        animation: float-up 6s ease-in infinite;
        opacity: 0.6;
    }
    
    @keyframes float-up {
        0% {
            transform: translateY(100vh) rotate(0deg);
            opacity: 0;
        }
        10% {
            opacity: 0.6;
        }
        90% {
            opacity: 0.6;
        }
        100% {
            transform: translateY(-100vh) rotate(360deg);
            opacity: 0;
        }
    }
    
    /* ===== TYTUŁ GRY ===== */
    .game-title {
        text-align: center;
        font-size: 4.5rem;
        font-weight: 700;
        color: white;
        text-shadow: 4px 4px 8px rgba(0, 0, 0, 0.3);
        margin-bottom: 0.5rem;
        animation: title-glow 2s ease-in-out infinite alternate;
    }
    
    .game-subtitle {
        text-align: center;
        font-size: 1.8rem;
        color: #FFE4EE;
        margin-bottom: 2rem;
    }
    
    @keyframes title-glow {
        from {
            text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.3), 0 0 20px rgba(255, 255, 255, 0.3);
        }
        to {
            text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.3), 0 0 40px rgba(255, 255, 255, 0.6);
        }
    }
    
    /* ===== KARTY ===== */
    .game-card {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
        margin: 1rem 0;
    }
    
    .player-card {
        background: linear-gradient(135deg, #FFE4EE 0%, #E8D5F2 100%);
        border-radius: 20px;
        padding: 2rem;
        text-align: center;
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.15);
        transition: transform 0.3s ease;
    }
    
    .player-card:hover {
        transform: scale(1.02);
    }
    
    .player-card.active {
        border: 4px solid #FF6B9D;
        box-shadow: 0 8px 40px rgba(255, 107, 157, 0.5);
    }
    
    .player-name {
        font-size: 2rem;
        font-weight: 700;
        color: #6B2D7B;
        margin-bottom: 0.5rem;
    }
    
    .player-score {
        font-size: 3.5rem;
        font-weight: 700;
        color: #FF6B9D;
    }
    
    /* ===== HASŁO ===== */
    .word-display {
        background: linear-gradient(135deg, #6B2D7B 0%, #C44FE2 100%);
        border-radius: 20px;
        padding: 3rem 2rem;
        text-align: center;
        margin: 2rem 0;
        box-shadow: 0 10px 40px rgba(107, 45, 123, 0.4);
    }
    
    .word-text {
        font-size: 4rem;
        font-weight: 700;
        color: white;
        text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.3);
        line-height: 1.2;
    }
    
    .word-category {
        font-size: 1.4rem;
        color: #FFE4EE;
        margin-top: 1rem;
    }
    
    .reveal-prompt {
        text-align: center;
        font-size: 1.5rem;
        color: white;
        margin: 1.5rem 0 1rem 0;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
        animation: pulse-text 1.5s ease-in-out infinite;
    }
    
    @keyframes pulse-text {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.7; }
    }
    
    /* Kategoria - zawsze widoczna */
    .category-display {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 15px;
        padding: 1.2rem 2rem;
        text-align: center;
        margin: 1.5rem 0;
        box-shadow: 0 5px 20px rgba(0, 0, 0, 0.15);
    }
    
    .category-label {
        font-size: 1.5rem;
        font-weight: 600;
        color: #6B2D7B;
    }
    
    .category-value {
        font-size: 1.8rem;
        font-weight: 700;
        color: #FF6B9D;
        margin-left: 0.5rem;
    }
    
    /* Ukryte hasło */
    .word-hidden {
        background: linear-gradient(135deg, #666 0%, #444 100%);
        border-radius: 20px;
        padding: 2.5rem 2rem;
        text-align: center;
        margin: 1rem 0;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3);
    }
    
    .word-hidden-text {
        font-size: 2.5rem;
        font-weight: 700;
        color: #ddd;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
    }
    
    .word-hidden-hint {
        font-size: 1.2rem;
        color: #aaa;
        margin-top: 0.5rem;
    }
    
    /* Przycisk pokaż hasło - biały i wyrazisty */
    button[key="reveal_btn"], 
    .stButton > button:has-text("POKAŻ HASŁO") {
        background: white !important;
        color: #6B2D7B !important;
        font-weight: 700 !important;
        border: 3px solid #FF6B9D !important;
    }
    
    /* ===== TRYB GRY ===== */
    .mode-display {
        text-align: center;
        padding: 1.5rem 2rem;
        border-radius: 20px;
        margin: 1.5rem 0;
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.2);
    }
    
    .mode-show {
        background: linear-gradient(135deg, #4CAF50 0%, #8BC34A 100%);
    }
    
    .mode-tell {
        background: linear-gradient(135deg, #2196F3 0%, #03A9F4 100%);
    }
    
    .mode-text {
        font-size: 3rem;
        font-weight: 700;
        color: white;
        text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.3);
        animation: pulse-mode 1s ease-in-out infinite;
    }
    
    @keyframes pulse-mode {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.05); }
    }
    
    /* ===== TIMER ===== */
    .timer-container {
        text-align: center;
        margin: 2rem 0;
        padding: 1.5rem;
        background: rgba(255, 255, 255, 0.9);
        border-radius: 20px;
        box-shadow: 0 5px 20px rgba(0, 0, 0, 0.1);
    }
    
    .timer-text {
        font-size: 5rem;
        font-weight: 700;
        color: #6B2D7B;
    }
    
    .timer-text.warning {
        color: #FF9800;
        animation: timer-pulse 0.5s ease-in-out infinite;
    }
    
    .timer-text.danger {
        color: #F44336;
        animation: timer-pulse 0.3s ease-in-out infinite;
    }
    
    @keyframes timer-pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.1); }
    }
    
    .timer-bar {
        width: 100%;
        height: 20px;
        background: #E0E0E0;
        border-radius: 15px;
        overflow: hidden;
        margin-top: 1rem;
    }
    
    .timer-bar-fill {
        height: 100%;
        background: linear-gradient(90deg, #4CAF50, #8BC34A);
        border-radius: 10px;
        transition: width 1s linear;
    }
    
    .timer-bar-fill.warning {
        background: linear-gradient(90deg, #FF9800, #FFC107);
    }
    
    .timer-bar-fill.danger {
        background: linear-gradient(90deg, #F44336, #E91E63);
    }
    
    /* ===== PRZYCISKI ===== */
    .stButton > button {
        font-family: 'Quicksand', sans-serif;
        font-weight: 600;
        border-radius: 30px;
        padding: 1rem 2.5rem;
        font-size: 1.4rem;
        transition: all 0.3s ease;
        border: none;
        min-height: 60px;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 20px rgba(0, 0, 0, 0.2);
    }
    
    /* Przycisk główny (start) */
    div[data-testid="stButton"] > button[kind="primary"] {
        background: linear-gradient(135deg, #FF6B9D 0%, #C44FE2 100%);
        color: white;
        animation: pulse-button 2s ease-in-out infinite;
    }
    
    @keyframes pulse-button {
        0%, 100% { box-shadow: 0 5px 20px rgba(255, 107, 157, 0.4); }
        50% { box-shadow: 0 5px 30px rgba(255, 107, 157, 0.8); }
    }
    
    /* ===== RUNDA INFO ===== */
    .round-info {
        text-align: center;
        font-size: 2.2rem;
        color: white;
        font-weight: 600;
        margin-bottom: 1.5rem;
        text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.3);
    }
    
    /* ===== PUNKTY ===== */
    .points-earned {
        text-align: center;
        font-size: 3.5rem;
        font-weight: 700;
        color: #FFD700;
        text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.3);
        animation: points-pop 0.5s ease-out;
        margin: 1.5rem 0;
    }
    
    @keyframes points-pop {
        0% { transform: scale(0); opacity: 0; }
        50% { transform: scale(1.2); }
        100% { transform: scale(1); opacity: 1; }
    }
    
    /* ===== KONFETTI ===== */
    .confetti {
        position: fixed;
        width: 10px;
        height: 10px;
        top: -10px;
        animation: confetti-fall 3s ease-in-out forwards;
    }
    
    @keyframes confetti-fall {
        0% {
            transform: translateY(0) rotate(0deg);
            opacity: 1;
        }
        100% {
            transform: translateY(100vh) rotate(720deg);
            opacity: 0;
        }
    }
    
    /* ===== WINNER SCREEN ===== */
    .winner-text {
        text-align: center;
        font-size: 4rem;
        font-weight: 700;
        color: #FFD700;
        text-shadow: 4px 4px 8px rgba(0, 0, 0, 0.3);
        animation: winner-glow 1s ease-in-out infinite alternate;
        margin: 2rem 0;
    }
    
    @keyframes winner-glow {
        from {
            text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.3), 0 0 20px rgba(255, 215, 0, 0.5);
        }
        to {
            text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.3), 0 0 60px rgba(255, 215, 0, 1);
        }
    }
    
    /* ===== DIFFICULTY BUTTONS ===== */
    .difficulty-easy {
        background: linear-gradient(135deg, #4CAF50 0%, #8BC34A 100%) !important;
    }
    
    .difficulty-medium {
        background: linear-gradient(135deg, #FF9800 0%, #FFC107 100%) !important;
    }
    
    .difficulty-hard {
        background: linear-gradient(135deg, #F44336 0%, #E91E63 100%) !important;
    }
    
    /* ===== HISTORIA ===== */
    .history-table {
        background: rgba(255, 255, 255, 0.9);
        border-radius: 10px;
        overflow: hidden;
    }
    
    /* ===== GŁÓWNY KONTENER - SZERSZY ===== */
    .main .block-container {
        max-width: 1200px;
        padding-left: 2rem;
        padding-right: 2rem;
    }
    
    /* ===== SUWAK RUND - BIAŁY I WIDOCZNY ===== */
    .stSlider > div > div > div {
        background: white !important;
    }
    
    .stSlider [data-testid="stTickBar"] > div {
        background: rgba(255, 255, 255, 0.8) !important;
    }
    
    .stSlider > div > div > div > div {
        background: white !important;
        border: 3px solid #FF6B9D !important;
    }
    
    div[data-baseweb="slider"] > div {
        background: rgba(255, 255, 255, 0.9) !important;
        height: 10px !important;
        border-radius: 5px !important;
    }
    
    div[data-baseweb="slider"] > div > div {
        background: linear-gradient(135deg, #FF6B9D 0%, #C44FE2 100%) !important;
    }
    
    div[data-baseweb="slider"] [role="slider"] {
        background: white !important;
        border: 4px solid #FF6B9D !important;
        width: 28px !important;
        height: 28px !important;
        box-shadow: 0 4px 15px rgba(255, 107, 157, 0.4) !important;
    }
    
    /* Etykiety suwaka */
    .stSlider label {
        color: white !important;
        font-size: 1.3rem !important;
        font-weight: 600 !important;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3) !important;
    }
    
    .stSlider [data-testid="stTickBarMin"],
    .stSlider [data-testid="stTickBarMax"] {
        color: white !important;
        font-size: 1.2rem !important;
        font-weight: 600 !important;
    }
    
    /* ===== RADIO BUTTONS - POZIOM TRUDNOŚCI ===== */
    .stRadio > label {
        color: white !important;
        font-size: 1.4rem !important;
        font-weight: 600 !important;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3) !important;
    }
    
    .stRadio > div {
        background: rgba(255, 255, 255, 0.95) !important;
        border-radius: 15px !important;
        padding: 1rem !important;
        box-shadow: 0 5px 20px rgba(0, 0, 0, 0.15) !important;
    }
    
    .stRadio > div > label {
        color: #6B2D7B !important;
        font-size: 1.2rem !important;
        font-weight: 600 !important;
        padding: 0.8rem 1rem !important;
        border-radius: 10px !important;
        margin: 0.3rem 0 !important;
        transition: all 0.3s ease !important;
    }
    
    .stRadio > div > label span,
    .stRadio > div > label p,
    .stRadio > div label[data-baseweb="radio"] span {
        color: #6B2D7B !important;
    }
    
    .stRadio > div > label:hover {
        background: rgba(255, 107, 157, 0.1) !important;
    }
    
    /* Radio button - tekst opcji */
    div[role="radiogroup"] label {
        color: #6B2D7B !important;
    }
    
    div[role="radiogroup"] label span {
        color: #6B2D7B !important;
    }
    
    /* Nagłówki w menu */
    .stMarkdown h3 {
        color: white !important;
        font-size: 1.8rem !important;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3) !important;
        margin-top: 1.5rem !important;
    }
    
    /* ===== PRZYCISK POKAŻ HASŁO - BIAŁY ===== */
    .stButton > button[kind="secondary"],
    div[data-testid="stButton"] > button:not([kind="primary"]) {
        background: white !important;
        color: #6B2D7B !important;
        border: 3px solid #FF6B9D !important;
        font-weight: 700 !important;
    }
    
    div[data-testid="stButton"] > button:not([kind="primary"]):hover {
        background: #FFE4EE !important;
        border-color: #C44FE2 !important;
    }
    
    /* ===== RESPONSYWNOŚĆ ===== */
    @media (max-width: 768px) {
        .game-title {
            font-size: 2.5rem;
        }
        
        .word-text {
            font-size: 2.5rem;
        }
        
        .timer-text {
            font-size: 3.5rem;
        }
        
        .player-score {
            font-size: 2.5rem;
        }
        
        .player-name {
            font-size: 1.5rem;
        }
        
        .mode-text {
            font-size: 2rem;
        }
        
        .round-info {
            font-size: 1.5rem;
        }
    }
    </style>
    """


def get_hearts_animation():
    """Generuje HTML z animowanymi serduszkami w tle"""
    import random
    hearts = ""
    for i in range(15):
        left = random.randint(0, 100)
        delay = random.uniform(0, 5)
        size = random.randint(15, 35)
        hearts += f'<div class="heart" style="left: {left}%; animation-delay: {delay}s; font-size: {size}px;">💕</div>'
    
    return f'<div class="hearts-container">{hearts}</div>'


def get_confetti_animation():
    """Generuje HTML z animacją konfetti"""
    import random
    colors = ['#FF6B9D', '#C44FE2', '#FFD700', '#4CAF50', '#2196F3', '#FF9800']
    confetti = ""
    for i in range(50):
        left = random.randint(0, 100)
        delay = random.uniform(0, 2)
        color = random.choice(colors)
        size = random.randint(8, 15)
        confetti += f'''
        <div class="confetti" style="
            left: {left}%; 
            animation-delay: {delay}s; 
            background: {color};
            width: {size}px;
            height: {size}px;
            border-radius: {random.choice(['0', '50%'])};
        "></div>'''
    
    return f'<div style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: 9999;">{confetti}</div>'

