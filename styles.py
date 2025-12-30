# Style CSS i animacje dla Kalambury Zuzanny

def get_custom_css():
    return """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;500;600;700&display=swap');
    
    /* ===== GŁÓWNE STYLE ===== */
    
    /* Zapewnienie prawidłowego skalowania na urządzeniach mobilnych */
    html {
        -webkit-text-size-adjust: 100%;
        -ms-text-size-adjust: 100%;
    }
    
    * {
        box-sizing: border-box;
    }
    
    .stApp {
        background: linear-gradient(135deg, #FF6B9D 0%, #C44FE2 100%);
        font-family: 'Quicksand', sans-serif;
        min-height: 100vh;
        min-height: 100dvh; /* Dynamic viewport height dla mobilnych przeglądarek */
    }
    
    /* Ukryj domyślny header Streamlit */
    header[data-testid="stHeader"] {
        background: transparent;
    }
    
    /* Fix dla paska nawigacji Streamlit na mobilnych */
    section[data-testid="stSidebar"] {
        z-index: 999999;
    }
    
    /* Ukryj menu hamburger na mobilnych jeśli sidebar jest schowany */
    button[kind="header"] {
        display: none;
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
    
    /* ===== GŁÓWNY KONTENER ===== */
    .main .block-container {
        max-width: 1200px;
        padding-left: 2rem;
        padding-right: 2rem;
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    /* Fix dla kolumn Streamlit na mobilnych */
    @media (max-width: 640px) {
        div[data-testid="column"] {
            width: 100% !important;
            flex: 1 1 100% !important;
            min-width: 100% !important;
        }
        
        /* Dodaj odstęp między kartami gdy są pod sobą */
        div[data-testid="column"]:not(:last-child) {
            margin-bottom: 0.5rem;
        }
        
        /* Zmniejsz marginesy między elementami */
        .element-container {
            margin-bottom: 0.5rem !important;
        }
        
        /* Przyciski akcji - stack na mobilnych */
        div[data-testid="stHorizontalBlock"] {
            flex-wrap: wrap;
            gap: 0.5rem;
        }
        
        div[data-testid="stHorizontalBlock"] > div[data-testid="column"] {
            flex: 1 1 calc(50% - 0.25rem) !important;
            min-width: calc(50% - 0.25rem) !important;
        }
    }
    
    /* Na bardzo małych ekranach przyciski jeden pod drugim */
    @media (max-width: 380px) {
        div[data-testid="stHorizontalBlock"] > div[data-testid="column"] {
            flex: 1 1 100% !important;
            min-width: 100% !important;
        }
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
    
    /* Tablety i małe laptopy */
    @media (max-width: 992px) {
        .main .block-container {
            max-width: 100%;
            padding-left: 1.5rem;
            padding-right: 1.5rem;
        }
        
        .game-title {
            font-size: 3.5rem;
        }
        
        .game-subtitle {
            font-size: 1.4rem;
        }
        
        .word-text {
            font-size: 3rem;
        }
        
        .player-score {
            font-size: 3rem;
        }
        
        .player-name {
            font-size: 1.7rem;
        }
    }
    
    /* Tablety w pionie i duże telefony */
    @media (max-width: 768px) {
        .main .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
        }
        
        .game-title {
            font-size: 2.5rem;
        }
        
        .game-subtitle {
            font-size: 1.2rem;
            margin-bottom: 1rem;
        }
        
        .game-card {
            padding: 1.2rem;
            border-radius: 15px;
            margin: 0.5rem 0;
        }
        
        .player-card {
            padding: 1rem;
            border-radius: 15px;
        }
        
        .player-name {
            font-size: 1.3rem;
        }
        
        .player-score {
            font-size: 2.2rem;
        }
        
        .word-display {
            padding: 1.5rem 1rem;
            border-radius: 15px;
            margin: 1rem 0;
        }
        
        .word-text {
            font-size: 2rem;
            word-break: break-word;
        }
        
        .word-category {
            font-size: 1.1rem;
        }
        
        .mode-display {
            padding: 1rem;
            border-radius: 15px;
            margin: 1rem 0;
        }
        
        .mode-text {
            font-size: 1.8rem;
        }
        
        .mode-display > div:last-child {
            font-size: 0.9rem !important;
        }
        
        .timer-container {
            padding: 1rem;
            margin: 1rem 0;
            border-radius: 15px;
        }
        
        .timer-text {
            font-size: 3rem;
        }
        
        .timer-bar {
            height: 15px;
        }
        
        .round-info {
            font-size: 1.5rem;
            margin-bottom: 1rem;
        }
        
        .category-display {
            padding: 0.8rem 1rem;
            border-radius: 12px;
            margin: 1rem 0;
        }
        
        .category-label {
            font-size: 1.1rem;
        }
        
        .category-value {
            font-size: 1.3rem;
        }
        
        .reveal-prompt {
            font-size: 1.1rem;
            margin: 1rem 0;
        }
        
        .stButton > button {
            font-size: 1.1rem;
            padding: 0.8rem 1.5rem;
            min-height: 50px;
            border-radius: 25px;
        }
        
        .winner-text {
            font-size: 2.5rem;
            margin: 1rem 0;
        }
        
        .points-earned {
            font-size: 2.5rem;
            margin: 1rem 0;
        }
        
        /* Radio buttons mniejsze */
        .stRadio > div > label {
            font-size: 1rem !important;
            padding: 0.6rem 0.8rem !important;
        }
        
        .stMarkdown h3 {
            font-size: 1.4rem !important;
            margin-top: 1rem !important;
        }
    }
    
    /* Telefony - średnie */
    @media (max-width: 576px) {
        .main .block-container {
            padding-left: 0.5rem;
            padding-right: 0.5rem;
            padding-top: 1rem;
        }
        
        .game-title {
            font-size: 1.8rem;
            margin-bottom: 0.3rem;
        }
        
        .game-subtitle {
            font-size: 1rem;
            margin-bottom: 0.8rem;
        }
        
        .game-card {
            padding: 0.8rem;
            border-radius: 12px;
        }
        
        .player-card {
            padding: 0.7rem;
            border-radius: 12px;
        }
        
        .player-name {
            font-size: 1rem;
            margin-bottom: 0.2rem;
        }
        
        .player-score {
            font-size: 1.6rem;
        }
        
        .word-display {
            padding: 1rem 0.8rem;
            border-radius: 12px;
            margin: 0.8rem 0;
        }
        
        .word-text {
            font-size: 1.5rem;
            line-height: 1.3;
        }
        
        .word-category {
            font-size: 0.9rem;
            margin-top: 0.5rem;
        }
        
        .mode-display {
            padding: 0.8rem;
            border-radius: 12px;
            margin: 0.8rem 0;
        }
        
        .mode-text {
            font-size: 1.4rem;
        }
        
        .mode-display > div:last-child {
            font-size: 0.8rem !important;
            margin-top: 0.3rem !important;
        }
        
        .timer-container {
            padding: 0.8rem;
            margin: 0.8rem 0;
            border-radius: 12px;
        }
        
        .timer-text {
            font-size: 2.5rem;
        }
        
        .timer-bar {
            height: 12px;
            margin-top: 0.5rem;
        }
        
        .round-info {
            font-size: 1.2rem;
            margin-bottom: 0.8rem;
        }
        
        .category-display {
            padding: 0.6rem 0.8rem;
            border-radius: 10px;
            margin: 0.6rem 0;
        }
        
        .category-label {
            font-size: 0.9rem;
        }
        
        .category-value {
            font-size: 1.1rem;
        }
        
        .reveal-prompt {
            font-size: 0.95rem;
            margin: 0.8rem 0;
        }
        
        .stButton > button {
            font-size: 0.95rem;
            padding: 0.6rem 1rem;
            min-height: 44px;
            border-radius: 22px;
        }
        
        .winner-text {
            font-size: 1.8rem;
            margin: 0.8rem 0;
        }
        
        .points-earned {
            font-size: 1.8rem;
            margin: 0.8rem 0;
        }
        
        /* Radio buttons na telefonie */
        .stRadio > div {
            padding: 0.6rem !important;
            border-radius: 10px !important;
        }
        
        .stRadio > div > label {
            font-size: 0.9rem !important;
            padding: 0.5rem 0.6rem !important;
        }
        
        .stMarkdown h3 {
            font-size: 1.2rem !important;
            margin-top: 0.8rem !important;
        }
        
        /* Suwak na telefonie */
        div[data-baseweb="slider"] [role="slider"] {
            width: 22px !important;
            height: 22px !important;
        }
        
        /* Serduszka mniejsze na telefonach */
        .heart {
            font-size: 15px;
        }
    }
    
    /* Bardzo małe telefony */
    @media (max-width: 380px) {
        .main .block-container {
            padding-left: 0.3rem;
            padding-right: 0.3rem;
        }
        
        .game-title {
            font-size: 1.5rem;
        }
        
        .game-subtitle {
            font-size: 0.85rem;
        }
        
        .player-name {
            font-size: 0.9rem;
        }
        
        .player-score {
            font-size: 1.4rem;
        }
        
        .word-text {
            font-size: 1.3rem;
        }
        
        .mode-text {
            font-size: 1.2rem;
        }
        
        .timer-text {
            font-size: 2rem;
        }
        
        .stButton > button {
            font-size: 0.85rem;
            padding: 0.5rem 0.8rem;
            min-height: 40px;
        }
        
        .winner-text {
            font-size: 1.5rem;
        }
        
        .points-earned {
            font-size: 1.5rem;
        }
        
        .round-info {
            font-size: 1rem;
        }
        
        .reveal-prompt {
            font-size: 0.85rem;
        }
        
        .category-label,
        .category-value {
            font-size: 0.85rem;
        }
    }
    
    /* Tryb landscape na telefonach */
    @media (max-height: 500px) and (orientation: landscape) {
        .game-title {
            font-size: 1.5rem;
            margin-bottom: 0.2rem;
        }
        
        .game-subtitle {
            font-size: 0.9rem;
            margin-bottom: 0.5rem;
        }
        
        .player-card {
            padding: 0.5rem;
        }
        
        .word-display {
            padding: 0.8rem;
            margin: 0.5rem 0;
        }
        
        .word-text {
            font-size: 1.5rem;
        }
        
        .mode-display {
            padding: 0.5rem;
            margin: 0.5rem 0;
        }
        
        .mode-text {
            font-size: 1.3rem;
        }
        
        .timer-container {
            padding: 0.5rem;
            margin: 0.5rem 0;
        }
        
        .timer-text {
            font-size: 2rem;
        }
        
        .timer-bar {
            height: 10px;
        }
        
        .stButton > button {
            min-height: 36px;
            padding: 0.4rem 0.8rem;
        }
        
        .hearts-container {
            display: none;
        }
    }
    
    /* Poprawa dotykowa na urządzeniach mobilnych */
    @media (hover: none) and (pointer: coarse) {
        .stButton > button {
            min-height: 48px;
        }
        
        .player-card:hover {
            transform: none;
        }
        
        .stButton > button:hover {
            transform: none;
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

