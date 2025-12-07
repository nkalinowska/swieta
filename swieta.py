import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import random 

st.set_page_config(layout="centered")
st.title("🎅 Święty Mikołaj w Streamlit z Rozbudowanym Konfiguratorem")

# --- KONFIGURACJA KOLORÓW, PREZENTÓW I KSZTAŁTÓW NA PASKU BOCZNYM ---
st.sidebar.header("Konfigurator Stroju")

main_color = st.sidebar.color_picker(
    'Wybierz kolor stroju',
    '#FF0000', # Domyślny Czerwony
    key='main_color'
)

belt_color = st.sidebar.color_picker(
    'Wybierz kolor paska',
    '#000000', # Domyślny Czarny
    key='belt_color'
)

# Stałe Kolory (niezmienne przez użytkownika)
SKIN_COLOR = 'peachpuff'
FUR_COLOR = 'white'
FUR_TRUNK_COLOR = '#E0E0E0' # Jaśniejszy szary dla lepszej widoczności
BUCKLE_COLOR = 'gold'
BOOT_COLOR = 'black'

# --- Konfiguracja Prezentów ---
st.sidebar.header("Konfigurator Prezentów")
num_gifts = st.sidebar.slider(
    'Liczba prezentów pod Mikołajem',
    min_value=0, 
    max_value=12, 
    value=5, 
    step=1,
    key='num_gifts'
)

gift_shape = st.sidebar.selectbox(
    'Wybierz kształt prezentów',
    ('Kwadrat', 'Koło', 'Losowy'),
    key='gift_shape_select'
)

ribbon_color_mode = st.sidebar.radio(
    'Tryb koloru wstążek',
    ('Losowy', 'Stały (Złoty)'),
    key='ribbon_color_mode_radio'
)

# --- FUNKCJA GENERUJĄCA LOSOWY KOLOR (HEX) ---
def get_random_color():
    """Generuje losowy kolor w formacie HEX."""
    return f'#{random.randint(0, 0xFFFFFF):06x}'

# --- FUNKCJA GŁÓWNA RYSOWANIA ---
def draw_santa(main_color, belt_color, num_gifts, gift_shape, ribbon_color_mode):
    """
    Funkcja rysująca schematycznego Świętego Mikołaja i konfigurowalne prezenty.
    """
    
    fig, ax = plt.subplots(figsize=(6, 10))
    ax.set_xlim(0, 10)
    ax.set_ylim(-3, 9)
    ax.set_aspect('equal')
    ax.axis('off')

    # --- ELEMENTY GŁOWY I CZAPKI ---
    # ... (kod głowy i czapki bez zmian)
    kaptur_dol = patches.Rectangle((3.5, 6.5), 3, 1, color=main_color, zorder=3)
    ax.add_patch(kaptur_dol)
    czapka_x = np.array([4, 6, 5])
    czapka_y = np.array([7.5, 7.5, 9])
    ax.fill(czapka_x, czapka_y, color=main_color, zorder=3)
    kulka = patches.Circle((5, 9), radius=0.3, color=FUR_COLOR, zorder=4)
    ax.add_patch(kulka)
    futerko = patches.Rectangle((3, 6.3), 4, 0.4, color=FUR_COLOR, zorder=4)
    ax.add_patch(futerko)
    glowa = patches.Circle((5, 5), radius=1.3, color=SKIN_COLOR, zorder=2)
    ax.add_patch(glowa)
    ax.plot(4.4, 5.5, 'o', markersize=4, color='black', zorder=5)
    ax.plot(5.6, 5.5, 'o', markersize=4, color='black', zorder=5)
    nos = patches.Circle((5, 5), radius=0.2, color='brown', zorder=5)
    ax.add_patch(nos)
    broda_x = np.array([3.5, 6.5, 5])
    broda_y = np.array([4, 4, 2])
    ax.fill(broda_x, broda_y, color=FUR_COLOR, zorder=1)

    # --- TUŁÓW, RĘCE I NOGI ---

    # 1. TUŁÓW
    tulow = patches.Rectangle((3, 0), 4, 4, color=main_color, zorder=1)
    ax.add_patch(tulow)

    # 2. FUTRO NA TUŁOWIU (ULEPSZONE WYCIENIOWANIE)
    futerko_tulow = patches.Rectangle(
        (3, 3.5), 
        4, 
        0.5, 
        color=FUR_TRUNK_COLOR, # Używamy jaśniejszego szarego
        edgecolor='#B0B0B0',   # Dodajemy subtelną krawędź
        linewidth=0.5,
        zorder=2
    )
    ax.add_patch(futerko_tulow)

    # 3. PASEK
    pasek = patches.Rectangle((3, 2.8), 4, 0.5, color=belt_color, zorder=3)
    ax.add_patch(pasek)

    # 4. KLAMRA PASKA
    klamra = patches.Rectangle((4.5, 2.9), 1, 0.3, color=BUCKLE_COLOR, zorder=4)
    ax.add_patch(klamra)
    
    # 5. RĘCE, RĘKAWICZKI, NOGI, BUTY (bez zmian)
    reka_l = patches.Rectangle((1, 2.5), 2, 0.8, color=main_color, zorder=1)
    ax.add_patch(reka_l)
    reka_p = patches.Rectangle((7, 2.5), 2, 0.8, color=main_color, zorder=1)
    ax.add_patch(reka_p)
    rekawiczka_l = patches.Circle((1, 2.9), radius=0.4, color=FUR_COLOR, zorder=5)
    ax.add_patch(rekawiczka_l)
    rekawiczka_p = patches.Circle((9, 2.9), radius=0.4, color=FUR_COLOR, zorder=5)
    ax.add_patch(rekawiczka_p)
    noga_l = patches.Rectangle((3.5, -2), 1, 2, color=main_color, zorder=1)
    ax.add_patch(noga_l)
    noga_p = patches.Rectangle((5.5, -2), 1, 2, color=main_color, zorder=1)
    ax.add_patch(noga_p)
    but_l = patches.Rectangle((3, -3), 1.5, 1, color=BOOT_COLOR, zorder=2)
    ax.add_patch(but_l)
    but_p = patches.Rectangle((5.5, -3), 1.5, 1, color=BOOT_COLOR, zorder=2)
    ax.add_patch(but_p)

    # --- DYNAMICZNE GENEROWANIE ŚWIECĄCYCH PREZENTÓW ---
    
    X_START, X_END = 0.5, 9.5
    Y_MIN, Y_MAX = -3.0, -0.5
    
    gifts_data = []
    
    for i in range(num_gifts):
        # Losowanie rozmiarów prezentu
        w = random.uniform(0.7, 1.5)
        h = random.uniform(0.7, 1.5)
        
        # Losowanie pozycji
        x = random.uniform(X_START, X_END - w)
        y = random.uniform(Y_MIN, Y_MAX - h)
        
        gifts_data.append((x, y, w, h))

    # Rysowanie prezentów
    for x, y, w, h in gifts_data:
        gift_color = get_random_color()
        ribbon_color = 'gold' if ribbon_color_mode == 'Stały (Złoty)' else get_random_color()

        current_shape = gift_shape
        if current_shape == 'Losowy':
            current_shape = random.choice(['Kwadrat', 'Koło'])

        if current_shape == 'Kwadrat':
            # Prezent (Kwadrat/Prostokąt)
            prezent = patches.Rectangle((x, y), w, h, color=gift_color, zorder=0, edgecolor='black', linewidth=1)
            ax.add_patch(prezent)
            
            # Wstążki (tylko dla kwadratów)
            wstazka_v = patches.Rectangle((x + w/2 - 0.1, y), 0.2, h, color=ribbon_color, zorder=1)
            ax.add_patch(wstazka_v)
            wstazka_h = patches.Rectangle((x, y + h/2 - 0.1), w, 0.2, color=ribbon_color, zorder=1)
            ax.add_patch(wstazka_h)
            
            center_x, center_y = x + w/2, y + h/2
            top_y = y + h

        elif current_shape == 'Koło':
            # Prezent (Koło) - Używamy mniejszego z wymiarów jako promienia
            radius = min(w, h) / 2
            center_x = x + w/2
            center_y = y + radius 
            
            prezent = patches.Circle((center_x, center_y), radius=radius, color=gift_color, zorder=0, edgecolor='black', linewidth=1)
            ax.add_patch(prezent)

            # Wstążki na kole (prostokąty przecinające środek)
            wstazka_v = patches.Rectangle((center_x - 0.1, center_y - radius), 0.2, 2 * radius, color=ribbon_color, zorder=1)
            ax.add_patch(wstazka_v)
            wstazka_h = patches.Rectangle((center_x - radius, center_y - 0.1), 2 * radius, 0.2, color=ribbon_color, zorder=1)
            ax.add_patch(wstazka_h)
            
            top_y = center_y + radius


        # Pętelka / Kokarda
        if random.choice([True, False]): 
             petelka = patches.Circle((center_x, top_y - 0.1), radius=0.1, color=ribbon_color, zorder=2)
             ax.add_patch(petelka)

        # ✨ EFEKT LŚNIENIA (SHINE) ✨
        # Mała, jasna plamka dla efektu połysku
        shine_color = random.choice(['white', 'yellow'])
        
        # Generowanie losowego punktu lśnienia na powierzchni prezentu
        if current_shape == 'Kwadrat':
            shine_x = random.uniform(x + 0.1, x + w - 0.1)
            shine_y = random.uniform(y + 0.1, y + h - 0.1)
        elif current_shape == 'Koło':
            # Dla koła losujemy punkt w promieniu (nieco bardziej skomplikowane, ale dla prostoty użyjmy blisko środka)
            r_limit = radius * 0.5 
            angle = random.uniform(0, 2 * np.pi)
            dist = random.uniform(0, r_limit)
            shine_x = center_x + dist * np.cos(angle)
            shine_y = center_y + dist * np.sin(angle)
            
        shine = patches.Circle((shine_x, shine_y), radius=0.05, color=shine_color, alpha=0.8, zorder=2)
        ax.add_patch(shine)

    # Wyświetlenie rysunku w Streamlit
    st.pyplot(fig)


# Uruchomienie funkcji rysującej Mikołaja z NOWYMI opcjami
draw_santa(main_color, belt_color, num_gifts, gift_shape, ribbon_color_mode)
