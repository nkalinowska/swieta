import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import random 

st.set_page_config(layout="centered")
st.title("🎅 Święty Mikołaj w Streamlit z Konfiguratorem Kolorów")

# --- KONFIGURACJA KOLORÓW I PREZENTÓW NA PASKU BOCZNYM ---
st.sidebar.header("Konfigurator Stroju")

# Wybór Głównego Koloru (domyślnie Czerwony)
main_color = st.sidebar.color_picker(
    'Wybierz kolor stroju',
    '#FF0000', # Domyślny kolor (Czerwony)
    key='main_color'
)

# Wybór Koloru Paska (domyślnie Czarny)
belt_color = st.sidebar.color_picker(
    'Wybierz kolor paska',
    '#000000', # Domyślny kolor (Czarny)
    key='belt_color'
)

# NOWA OPCJA: Konfiguracja liczby prezentów
st.sidebar.header("Konfigurator Prezentów")
num_gifts = st.sidebar.slider(
    'Liczba prezentów pod choinką',
    min_value=0, 
    max_value=12, 
    value=5, # Domyślnie 5 prezentów
    step=1,
    key='num_gifts'
)

# Stałe kolory
SKIN_COLOR = 'peachpuff'
FUR_COLOR = 'white'
BUCKLE_COLOR = 'gold'
BOOT_COLOR = 'black'

# --- FUNKCJA GENERUJĄCA LOSOWY KOLOR (HEX) ---
def get_random_color():
    """Generuje losowy kolor w formacie HEX."""
    return f'#{random.randint(0, 0xFFFFFF):06x}'

# --- FUNKCJA GŁÓWNA RYSOWANIA ---
def draw_santa(main_color, belt_color, num_gifts):
    """
    Funkcja rysująca schematycznego Świętego Mikołaja.
    Przyjmuje argumenty main_color, belt_color i num_gifts.
    """
    
    fig, ax = plt.subplots(figsize=(6, 10))
    ax.set_xlim(0, 10)
    ax.set_ylim(-3, 9)
    ax.set_aspect('equal')
    ax.axis('off')

    # --- ELEMENTY GŁOWY, TUŁOWIA I NÓG (Kod Mikołaja pozostaje bez zmian) ---
    
    # Czapka (Kaptur - Dół) -> Używa main_color
    kaptur_dol = patches.Rectangle((3.5, 6.5), 3, 1, color=main_color, zorder=3)
    ax.add_patch(kaptur_dol)
    # Szczyt czapki (Trójkąt) -> Używa main_color
    czapka_x = np.array([4, 6, 5])
    czapka_y = np.array([7.5, 7.5, 9])
    ax.fill(czapka_x, czapka_y, color=main_color, zorder=3)
    # Puszysta kulka na czapce (stały kolor)
    kulka = patches.Circle((5, 9), radius=0.3, color=FUR_COLOR, zorder=4)
    ax.add_patch(kulka)
    # Puszyste futerko czapki (stały kolor)
    futerko = patches.Rectangle((3, 6.3), 4, 0.4, color=FUR_COLOR, zorder=4)
    ax.add_patch(futerko)
    # Głowa, Oczy, Nos, Broda (stałe kolory)
    glowa = patches.Circle((5, 5), radius=1.3, color=SKIN_COLOR, zorder=2)
    ax.add_patch(glowa)
    ax.plot(4.4, 5.5, 'o', markersize=4, color='black', zorder=5)
    ax.plot(5.6, 5.5, 'o', markersize=4, color='black', zorder=5)
    nos = patches.Circle((5, 5), radius=0.2, color='brown', zorder=5)
    ax.add_patch(nos)
    broda_x = np.array([3.5, 6.5, 5])
    broda_y = np.array([4, 4, 2])
    ax.fill(broda_x, broda_y, color=FUR_COLOR, zorder=1)
    # TUŁÓW, RĘCE I NOGI
    tulow = patches.Rectangle((3, 0), 4, 4, color=main_color, zorder=1)
    ax.add_patch(tulow)
    futerko_tulow = patches.Rectangle((3, 3.5), 4, 0.5, color=FUR_COLOR, zorder=2)
    ax.add_patch(futerko_tulow)
    pasek = patches.Rectangle((3, 2.8), 4, 0.5, color=belt_color, zorder=3)
    ax.add_patch(pasek)
    klamra = patches.Rectangle((4.5, 2.9), 1, 0.3, color=BUCKLE_COLOR, zorder=4)
    ax.add_patch(klamra)
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
    
    # 1. Określenie dostępnego obszaru dla prezentów (X: 0.5 do 9.5, Y: -3 do -0.5)
    X_START, X_END = 0.5, 9.5
    Y_MIN, Y_MAX = -3.0, -0.5
    
    # 2. Generowanie danych dla prezentów
    gifts_data = []
    
    # Używamy pętli for opartej na wartości z suwaka `num_gifts`
    for i in range(num_gifts):
        # Losowanie rozmiarów prezentu (nie za małe, nie za duże)
        w = random.uniform(0.7, 1.5)
        h = random.uniform(0.7, 1.5)
        
        # Losowanie pozycji (upewniamy się, że prezent mieści się w obszarze)
        x = random.uniform(X_START, X_END - w)
        y = random.uniform(Y_MIN, Y_MAX - h)
        
        # Dodajemy do listy
        gifts_data.append((x, y, w, h))

    # 3. Rysowanie dynamicznie wygenerowanych prezentów
    for x, y, w, h in gifts_data:
        # Losowy kolor dla głównej części prezentu
        gift_color = get_random_color()
        
        # Prezent (kwadrat/prostokąt)
        prezent = patches.Rectangle((x, y), w, h, color=gift_color, zorder=0, edgecolor='black', linewidth=1)
        ax.add_patch(prezent)
        
        # Losowy kolor dla wstążki
        ribbon_color = get_random_color() 
        
        # Wstążka Pionowa (dopasowana do rozmiaru prezentu)
        wstazka_v = patches.Rectangle((x + w/2 - 0.1, y), 0.2, h, color=ribbon_color, zorder=1)
        ax.add_patch(wstazka_v)
        
        # Wstążka Pozioma
        wstazka_h = patches.Rectangle((x, y + h/2 - 0.1), w, 0.2, color=ribbon_color, zorder=1)
        ax.add_patch(wstazka_h)
        
        # Dodatkowo, mała pętelka na górze
        if random.choice([True, False]): 
             petelka = patches.Circle((x + w/2, y + h - 0.1), radius=0.1, color=ribbon_color, zorder=2)
             ax.add_patch(petelka)


    # Wyświetlenie rysunku w Streamlit
    st.pyplot(fig)


# Uruchomienie funkcji rysującej Mikołaja z wybranymi kolorami i liczbą prezentów
draw_santa(main_color, belt_color, num_gifts)
