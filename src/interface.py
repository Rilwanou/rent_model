import streamlit as st
import pandas as pd
import numpy as np

# On importe le "moteur" de calcul que vous avez déjà créé
#import src.model as mf

# ---------------------------------------------------------------------
# CONFIGURATION DE LA PAGE
# ---------------------------------------------------------------------
st.set_page_config(
    page_title="Simulateur de Rente Minière",
    page_icon="⛏️",
    layout="wide"
)

st.title("⛏️ Simulateur de Partage de Rente Minière")
st.markdown("Une première interface pour visualiser l'impact du cours de l'or sur le partage de la rente (basé sur les données de Houndé, Code 2003).")

# ---------------------------------------------------------------------
# FONCTION DE CHARGEMENT DES DONNÉES
# ---------------------------------------------------------------------
@st.cache_data  # Met les données en cache pour la performance
def charger_donnees_simulation():
    """
    Charge les données nécessaires pour la simulation depuis vos fichiers CSV.
    """
    path_mine = 'data/donnees_mine_hounde.csv'
    path_amort = 'data/donnees_amortissement.csv'
    path_fiscal = 'data/donnees_fiscales_du_pays.csv'

    try:
        # Quantité d'Or Récupéré (oz) [cite: 117]
        qte_or_row = pd.read_csv(path_mine, skiprows=6, nrows=1).iloc[0]
        
        # OPEX (Coûts d'exploitation) [cite: 117]
        opex_row = pd.read_csv(path_mine, skiprows=18, nrows=1).iloc[0]
        
        # Total Amortissements [cite: 118]
        amort_row = pd.read_csv(path_amort, skiprows=76, nrows=1).iloc[0]
        
        # Taux Impôt Sociétés (Code 2003) [cite: 121]
        is_row = pd.read_csv(path_fiscal, skiprows=40, nrows=1).iloc[0]
        
        # Créer un DataFrame propre pour les années de production
        annees = [str(a) for a in range(2013, 2022)] 
        
        data = {
            'Qte_Or_oz': qte_or_row[annees].astype(float),
            'OPEX': opex_row[annees].astype(float),
            'Amortissement': amort_row[annees].astype(float),
            'Taux_IS': is_row[annees].astype(float)
        }
        
        df = pd.DataFrame(data)
        return df

    except FileNotFoundError as e:
        st.error(f"Erreur de chargement des fichiers de données: {e}")
        st.info("Vérifiez que vos fichiers CSV sont bien dans le dossier /data/")
        return None

# Chargement des données
df_base = charger_donnees_simulation()

if df_base is not None:
    # ---------------------------------------------------------------------
    # BARRE LATÉRALE (SIDEBAR) POUR LE LEVIER DE SIMULATION
    # ---------------------------------------------------------------------
    st.sidebar.header("⚙️ Paramètre Principal")
    
    # Levier unique: Cours de l'or
    # La valeur par défaut est 1300, comme dans vos données [cite: 117]
    cours_or_simule = st.sidebar.slider(
        "Cours de l'or (USD/oz)",
        min_value=1000,
        max_value=3000,
        value=1300, 
        step=50,
        help="Déplacez ce curseur pour recalculer l'ensemble de la simulation avec un nouveau prix de l'or."
    )

    # ---------------------------------------------------------------------
    # CŒUR DE LA SIMULATION (basé sur le levier)
    # ---------------------------------------------------------------------
    
    # Copie du DataFrame pour la simulation
    df_sim = df_base.copy()
    
    # 1. Appliquer le levier
    df_sim['Cours_Or'] = cours_or_simule
    df_sim['CA'] = df_sim['Qte_Or_oz'] * cours_or_simule # Recalcul du Chiffre d'Affaire

    # 2. Exécuter la simulation année par année
    resultats = []
    for annee, row in df_sim.iterrows():
        
        # A. Calculs des parts
        # Utilise les fonctions de votre fichier src/modele_fiscal.py
        redevance = mf.calculer_redevance_proportionnelle(row['CA'], row['Cours_Or'])
        
        benefice_imposable = mf.calculer_benefice_imposable(
            row['CA'], 
            row['OPEX'], 
            row['Amortissement'], 
            redevance
        )
        
        impot_etat = mf.calculer_impot_societes(benefice_imposable, row['Taux_IS'])
        
        # B. Parts finales
        part_etat = mf.calculer_part_etat(redevance, impot_etat)
        
        flux_investisseur = mf.calculer_flux_net_investisseur(
            row['CA'], 
            row['OPEX'], 
            redevance, 
            impot_etat
        )
        
        resultats.append({
            'Année': annee,
            'Chiffre d\'Affaire': row['CA'],
            'Part_Etat': part_etat,
            'Part_Investisseur': flux_investisseur,
            'Impôt Sociétés': impot_etat,
            'Redevance': redevance
        })

    df_resultats = pd.DataFrame(resultats).set_index('Année')

    # ---------------------------------------------------------------------
    # AFFICHAGE DES RÉSULTATS (PAGE PRINCIPALE)
    # ---------------------------------------------------------------------
    
    st.header(f"📈 Résultats de simulation (Cours de l'or à {cours_or_simule} $/oz)")

    # --- Indicateurs Clés (KPIs) ---
    total_etat = df_resultats['Part_Etat'].sum()
    total_investisseur = df_resultats['Part_Investisseur'].sum()
    total_ca = df_resultats['Chiffre d\'Affaire'].sum()
    
    if total_ca > 0:
        pct_etat_sur_ca = (total_etat / total_ca) * 100
    else:
        pct_etat_sur_ca = 0

    col1, col2, col3 = st.columns(3)
    col1.metric("Part Totale État", f"${total_etat:,.0f}", help="Total des impôts et redevances perçus par l'État (2013-2021).")
    col2.metric("Part Totale Investisseur", f"${total_investisseur:,.0f}", help="Flux de trésorerie net pour l'investisseur (2013-2021).")
    col3.metric("Taux Effectif (sur CA)", f"{pct_etat_sur_ca:.1f} %", help="Part totale de l'État / Chiffre d'Affaire total.")

    # --- Graphique Principal ---
    st.subheader("Partage Annuel (État vs. Investisseur)")
    
    df_graph = df_resultats[['Part_Etat', 'Part_Investisseur']]
    st.bar_chart(df_graph, height=400)

    # --- Données Détaillées ---
    with st.expander("Voir les données détaillées de la simulation"):
        st.dataframe(df_resultats.style.format("${:,.0f}"))

else:
    st.warning("Impossible de charger les données. L'application ne peut pas démarrer.")