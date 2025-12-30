import streamlit as st
import random
import time
from datetime import datetime
import math

from words import WORDS, DIFFICULTY_NAMES, DIFFICULTY_MULTIPLIERS
from styles import get_custom_css, get_hearts_animation, get_confetti_animation

# Konfiguracja strony
st.set_page_config(
    page_title="Kalambury Zuzanny",
    page_icon="💕",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Meta viewport dla urządzeń mobilnych
st.markdown('''
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
''', unsafe_allow_html=True)

# Wstrzyknięcie stylów CSS
st.markdown(get_custom_css(), unsafe_allow_html=True)

# ===== INICJALIZACJA STANU GRY =====
def init_session_state():
    """Inicjalizuje stan gry w session_state"""
    defaults = {
        'game_started': False,
        'game_phase': 'menu',  # menu, playing, round_result, game_over
        'difficulty': 'easy',
        'current_round': 1,
        'total_rounds': 10,
        'current_player': 'Mateusz',
        'scores': {'Mateusz': 0, 'Zuzanna': 0},
        'current_word': None,
        'current_mode': None,  # 'show' lub 'tell'
        'timer_start': None,
        'used_words': [],
        'game_history': [],
        'word_revealed': False,
        'show_confetti': False,
        'last_points': 0,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def reset_game():
    """Resetuje grę do stanu początkowego"""
    st.session_state.game_started = False
    st.session_state.game_phase = 'menu'
    st.session_state.current_round = 1
    st.session_state.current_player = 'Mateusz'
    st.session_state.scores = {'Mateusz': 0, 'Zuzanna': 0}
    st.session_state.current_word = None
    st.session_state.current_mode = None
    st.session_state.timer_start = None
    st.session_state.used_words = []
    st.session_state.word_revealed = False
    st.session_state.show_confetti = False
    st.session_state.last_points = 0


def get_random_word():
    """Losuje hasło, które nie było jeszcze użyte"""
    difficulty = st.session_state.difficulty
    available = [w for w in WORDS[difficulty] if w['word'] not in st.session_state.used_words]
    
    if not available:
        return None
    
    word = random.choice(available)
    st.session_state.used_words.append(word['word'])
    return word


def get_random_mode():
    """Losuje tryb: pokazywanie lub opowiadanie"""
    return random.choice(['show', 'tell'])


def calculate_points(elapsed_seconds):
    """Oblicza punkty na podstawie czasu i trudności"""
    # Bazowe punkty za czas
    if elapsed_seconds <= 15:
        base_points = 5
    elif elapsed_seconds <= 30:
        base_points = 4
    elif elapsed_seconds <= 45:
        base_points = 3
    elif elapsed_seconds <= 60:
        base_points = 2
    else:
        base_points = 0
    
    # Mnożnik trudności
    multiplier = DIFFICULTY_MULTIPLIERS[st.session_state.difficulty]
    final_points = math.ceil(base_points * multiplier)
    
    return final_points


def start_new_round():
    """Rozpoczyna nową rundę"""
    word = get_random_word()
    if word is None:
        st.session_state.game_phase = 'game_over'
        return
    
    st.session_state.current_word = word
    st.session_state.current_mode = get_random_mode()
    st.session_state.timer_start = None  # Timer startuje dopiero po odkryciu hasła
    st.session_state.word_revealed = False
    st.session_state.game_phase = 'playing'
    st.session_state.show_confetti = False


def handle_correct_guess():
    """Obsługuje prawidłowe zgadnięcie"""
    # Sprawdź czy hasło zostało już odkryte (timer wystartował)
    if st.session_state.timer_start is None:
        st.warning("⚠️ Najpierw odkryj hasło klikając 'POKAŻ HASŁO I ROZPOCZNIJ!'")
        return False
    
    elapsed = time.time() - st.session_state.timer_start
    points = calculate_points(elapsed)
    
    # Punkty dostaje zgadujący (nie pokazujący)
    guesser = 'Zuzanna' if st.session_state.current_player == 'Mateusz' else 'Mateusz'
    st.session_state.scores[guesser] += points
    st.session_state.last_points = points
    st.session_state.show_confetti = True
    st.session_state.game_phase = 'round_result'
    return True


def handle_skip():
    """Obsługuje pominięcie hasła"""
    st.session_state.last_points = 0
    st.session_state.show_confetti = False
    st.session_state.game_phase = 'round_result'


def handle_reroll():
    """Przelosowuje hasło (czas nadal leci)"""
    word = get_random_word()
    if word is None:
        st.warning("Brak więcej haseł!")
        return
    st.session_state.current_word = word
    st.session_state.word_revealed = False


def next_round():
    """Przechodzi do następnej rundy"""
    if st.session_state.current_round >= st.session_state.total_rounds:
        save_game_to_history()
        st.session_state.game_phase = 'game_over'
    else:
        st.session_state.current_round += 1
        # Zmiana gracza
        st.session_state.current_player = 'Zuzanna' if st.session_state.current_player == 'Mateusz' else 'Mateusz'
        start_new_round()


def save_game_to_history():
    """Zapisuje wynik gry do historii"""
    scores = st.session_state.scores
    winner = 'Mateusz' if scores['Mateusz'] > scores['Zuzanna'] else 'Zuzanna'
    if scores['Mateusz'] == scores['Zuzanna']:
        winner = 'Remis'
    
    game_record = {
        'date': datetime.now().strftime('%Y-%m-%d %H:%M'),
        'difficulty': DIFFICULTY_NAMES[st.session_state.difficulty],
        'rounds': st.session_state.total_rounds,
        'mateusz_score': scores['Mateusz'],
        'zuzanna_score': scores['Zuzanna'],
        'winner': winner
    }
    st.session_state.game_history.append(game_record)


# ===== KOMPONENTY UI =====

def render_menu():
    """Renderuje ekran menu"""
    # Animowane serduszka w tle
    st.markdown(get_hearts_animation(), unsafe_allow_html=True)
    
    # Tytuł
    st.markdown('<h1 class="game-title">💕 Kalambury Zuzanny 💕</h1>', unsafe_allow_html=True)
    st.markdown('<p class="game-subtitle">Romantyczna gra dla dwojga</p>', unsafe_allow_html=True)
    
    # Karta ustawień
    st.markdown('<div class="game-card">', unsafe_allow_html=True)
    
    # Gracze
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('''
        <div class="player-card">
            <div class="player-name">🧔 Mateusz</div>
            <div style="font-size: 2rem;">💙</div>
        </div>
        ''', unsafe_allow_html=True)
    
    with col2:
        st.markdown('''
        <div class="player-card">
            <div class="player-name">👩 Zuzanna</div>
            <div style="font-size: 2rem;">💖</div>
        </div>
        ''', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Wybór trudności
    st.markdown("### 🎯 Poziom trudności")
    difficulty = st.radio(
        "Wybierz poziom:",
        options=['easy', 'medium', 'hard'],
        format_func=lambda x: {
            'easy': '🟢 Łatwy (popularne hasła, mnożnik x1)',
            'medium': '🟡 Średni (specyficzne hasła, mnożnik x1.5)',
            'hard': '🔴 Trudny (niszowe hasła, mnożnik x2)'
        }[x],
        horizontal=False,
        label_visibility="collapsed"
    )
    st.session_state.difficulty = difficulty
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Wybór liczby rund
    st.markdown("### 🔄 Liczba rund")
    rounds = st.slider(
        "Wybierz liczbę rund:",
        min_value=1,
        max_value=20,
        value=10,
        label_visibility="collapsed"
    )
    st.session_state.total_rounds = rounds
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Przycisk start
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🎮 Rozpocznij grę!", type="primary", use_container_width=True):
            st.session_state.game_started = True
            start_new_round()
            st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Historia wyników
    if st.session_state.game_history:
        with st.expander("📊 Historia wyników"):
            render_history()
    
    # Reset
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🗑️ Wyczyść historię", use_container_width=True):
        st.session_state.game_history = []
        st.rerun()


def render_game():
    """Renderuje ekran gry"""
    # Serduszka w tle
    st.markdown(get_hearts_animation(), unsafe_allow_html=True)
    
    # Informacja o rundzie
    st.markdown(
        f'<div class="round-info">Runda {st.session_state.current_round} / {st.session_state.total_rounds}</div>',
        unsafe_allow_html=True
    )
    
    # Wyniki graczy
    scores = st.session_state.scores
    current = st.session_state.current_player
    
    col1, col2 = st.columns(2)
    with col1:
        active_class = "active" if current == "Mateusz" else ""
        showing = "📣 Pokazuje!" if current == "Mateusz" else ""
        st.markdown(f'''
        <div class="player-card {active_class}">
            <div class="player-name">🧔 Mateusz {showing}</div>
            <div class="player-score">{scores["Mateusz"]} pkt</div>
        </div>
        ''', unsafe_allow_html=True)
    
    with col2:
        active_class = "active" if current == "Zuzanna" else ""
        showing = "📣 Pokazuje!" if current == "Zuzanna" else ""
        st.markdown(f'''
        <div class="player-card {active_class}">
            <div class="player-name">👩 Zuzanna {showing}</div>
            <div class="player-score">{scores["Zuzanna"]} pkt</div>
        </div>
        ''', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Tryb gry
    mode = st.session_state.current_mode
    mode_class = "mode-show" if mode == "show" else "mode-tell"
    mode_text = "🎭 POKAŻ!" if mode == "show" else "🗣️ OPOWIEDZ!"
    mode_desc = "Nie możesz mówić ani wydawać dźwięków!" if mode == "show" else "Opisz hasło słowami, ale nie używaj słów z hasła!"
    
    st.markdown(f'''
    <div class="mode-display {mode_class}">
        <div class="mode-text">{mode_text}</div>
        <div style="color: white; margin-top: 0.5rem;">{mode_desc}</div>
    </div>
    ''', unsafe_allow_html=True)
    
    # Hasło
    word = st.session_state.current_word
    if word:
        # Kategoria pokazuje się ZAWSZE - aby zgadujący wiedział czego się spodziewać
        st.markdown(f'''
        <div class="category-display">
            <span class="category-label">📂 Kategoria:</span>
            <span class="category-value">{word["category"]}</span>
        </div>
        ''', unsafe_allow_html=True)
        
        if st.session_state.word_revealed:
            st.markdown(f'''
            <div class="word-display">
                <div class="word-text">{word["word"]}</div>
            </div>
            ''', unsafe_allow_html=True)
        else:
            # Tylko przycisk do odkrycia hasła - bez komunikatu "ukryte"
            st.markdown('<div class="reveal-prompt">👇 Osoba pokazująca - kliknij aby zobaczyć hasło i rozpocząć! 👇</div>', unsafe_allow_html=True)
            if st.button("👁️ POKAŻ HASŁO I ROZPOCZNIJ!", use_container_width=True, key="reveal_btn"):
                st.session_state.word_revealed = True
                st.session_state.timer_start = time.time()  # Timer startuje dopiero teraz!
                st.rerun()
    
    # Timer - pokazuj tylko gdy hasło zostało odkryte
    if st.session_state.timer_start and st.session_state.word_revealed:
        elapsed = time.time() - st.session_state.timer_start
        remaining = max(0, 60 - int(elapsed))
        
        timer_class = ""
        bar_class = ""
        if remaining <= 10:
            timer_class = "danger"
            bar_class = "danger"
        elif remaining <= 20:
            timer_class = "warning"
            bar_class = "warning"
        
        bar_width = (remaining / 60) * 100
        
        st.markdown(f'''
        <div class="timer-container">
            <div class="timer-text {timer_class}">{remaining}s</div>
            <div class="timer-bar">
                <div class="timer-bar-fill {bar_class}" style="width: {bar_width}%;"></div>
            </div>
        </div>
        ''', unsafe_allow_html=True)
        
        # Automatyczne zakończenie po upływie czasu
        if remaining <= 0:
            handle_skip()
            st.rerun()
    elif not st.session_state.word_revealed:
        # Pokaż informację że timer jeszcze nie wystartował
        st.markdown('''
        <div class="timer-container">
            <div class="timer-text" style="color: #999;">60s</div>
            <div class="timer-bar">
                <div class="timer-bar-fill" style="width: 100%;"></div>
            </div>
            <div style="text-align: center; color: #666; margin-top: 0.5rem;">⏸️ Czas ruszy po odkryciu hasła</div>
        </div>
        ''', unsafe_allow_html=True)
    
    # Przyciski akcji
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("✅ Zgadł!", use_container_width=True, type="primary"):
            if handle_correct_guess():
                st.rerun()
    
    with col2:
        if st.button("🔄 Przelosuj", use_container_width=True):
            handle_reroll()
            st.rerun()
    
    with col3:
        if st.button("⏭️ Pomiń", use_container_width=True):
            handle_skip()
            st.rerun()
    
    # Przycisk resetu
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("🏠 Powrót do menu", use_container_width=True):
        reset_game()
        st.rerun()
    
    # Auto-refresh co sekundę dla timera (tylko gdy timer działa)
    if st.session_state.timer_start and st.session_state.word_revealed:
        time.sleep(0.1)
        st.rerun()


def render_round_result():
    """Renderuje wynik rundy"""
    # Serduszka w tle
    st.markdown(get_hearts_animation(), unsafe_allow_html=True)
    
    # Konfetti przy sukcesie
    if st.session_state.show_confetti:
        st.markdown(get_confetti_animation(), unsafe_allow_html=True)
        st.balloons()
    
    st.markdown(
        f'<div class="round-info">Runda {st.session_state.current_round} / {st.session_state.total_rounds}</div>',
        unsafe_allow_html=True
    )
    
    st.markdown('<div class="game-card">', unsafe_allow_html=True)
    
    # Hasło
    word = st.session_state.current_word
    if word:
        st.markdown(f'''
        <div class="word-display">
            <div class="word-text">{word["word"]}</div>
            <div class="word-category">Kategoria: {word["category"]}</div>
        </div>
        ''', unsafe_allow_html=True)
    
    # Wynik rundy
    points = st.session_state.last_points
    if points > 0:
        guesser = 'Zuzanna' if st.session_state.current_player == 'Mateusz' else 'Mateusz'
        st.markdown(f'<div class="points-earned">+{points} punktów dla {guesser}! 🎉</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="points-earned" style="color: #999;">Brak punktów 😢</div>', unsafe_allow_html=True)
    
    # Aktualny wynik
    scores = st.session_state.scores
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f'''
        <div class="player-card">
            <div class="player-name">🧔 Mateusz</div>
            <div class="player-score">{scores["Mateusz"]} pkt</div>
        </div>
        ''', unsafe_allow_html=True)
    with col2:
        st.markdown(f'''
        <div class="player-card">
            <div class="player-name">👩 Zuzanna</div>
            <div class="player-score">{scores["Zuzanna"]} pkt</div>
        </div>
        ''', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Przycisk następna runda
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        next_text = "➡️ Następna runda" if st.session_state.current_round < st.session_state.total_rounds else "🏆 Pokaż wyniki"
        if st.button(next_text, type="primary", use_container_width=True):
            next_round()
            st.rerun()
    
    # Powrót do menu
    if st.button("🏠 Powrót do menu", use_container_width=True):
        reset_game()
        st.rerun()


def render_game_over():
    """Renderuje ekran końca gry"""
    # Serduszka w tle
    st.markdown(get_hearts_animation(), unsafe_allow_html=True)
    
    # Konfetti!
    st.markdown(get_confetti_animation(), unsafe_allow_html=True)
    st.balloons()
    
    scores = st.session_state.scores
    
    # Zwycięzca
    if scores['Mateusz'] > scores['Zuzanna']:
        winner = "🧔 Mateusz"
        winner_emoji = "🏆"
    elif scores['Zuzanna'] > scores['Mateusz']:
        winner = "👩 Zuzanna"
        winner_emoji = "🏆"
    else:
        winner = "Remis!"
        winner_emoji = "🤝"
    
    st.markdown(f'<div class="winner-text">{winner_emoji} {winner} wygrywa! {winner_emoji}</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="game-card">', unsafe_allow_html=True)
    
    st.markdown("<h2 style='text-align: center; color: #6B2D7B;'>Wyniki końcowe</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        medal = "🥇" if scores['Mateusz'] > scores['Zuzanna'] else ("🥈" if scores['Mateusz'] < scores['Zuzanna'] else "🏅")
        st.markdown(f'''
        <div class="player-card">
            <div class="player-name">{medal} Mateusz</div>
            <div class="player-score">{scores["Mateusz"]} pkt</div>
        </div>
        ''', unsafe_allow_html=True)
    
    with col2:
        medal = "🥇" if scores['Zuzanna'] > scores['Mateusz'] else ("🥈" if scores['Zuzanna'] < scores['Mateusz'] else "🏅")
        st.markdown(f'''
        <div class="player-card">
            <div class="player-name">{medal} Zuzanna</div>
            <div class="player-score">{scores["Zuzanna"]} pkt</div>
        </div>
        ''', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Przyciski
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 Zagraj ponownie", type="primary", use_container_width=True):
            reset_game()
            st.session_state.game_started = True
            start_new_round()
            st.rerun()
    
    with col2:
        if st.button("🏠 Powrót do menu", use_container_width=True):
            reset_game()
            st.rerun()
    
    # Historia
    if st.session_state.game_history:
        st.markdown("<br>", unsafe_allow_html=True)
        with st.expander("📊 Historia wyników"):
            render_history()


def render_history():
    """Renderuje tabelę historii wyników"""
    if not st.session_state.game_history:
        st.info("Brak zapisanych gier")
        return
    
    for i, game in enumerate(reversed(st.session_state.game_history)):
        winner_emoji = "🏆" if game['winner'] != 'Remis' else "🤝"
        st.markdown(f"""
        **Gra {len(st.session_state.game_history) - i}** ({game['date']})
        - Poziom: {game['difficulty']} | Rundy: {game['rounds']}
        - Mateusz: {game['mateusz_score']} pkt | Zuzanna: {game['zuzanna_score']} pkt
        - {winner_emoji} Zwycięzca: {game['winner']}
        ---
        """)


# ===== GŁÓWNA APLIKACJA =====

def main():
    init_session_state()
    
    if st.session_state.game_phase == 'menu':
        render_menu()
    elif st.session_state.game_phase == 'playing':
        render_game()
    elif st.session_state.game_phase == 'round_result':
        render_round_result()
    elif st.session_state.game_phase == 'game_over':
        render_game_over()


if __name__ == "__main__":
    main()

