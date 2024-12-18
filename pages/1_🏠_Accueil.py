import streamlit as st


# Titre principal
st.title("TalentTracker, détectez les étoiles montantes du football 🎯")

# Description rapide
st.write("Avec Talent Tracker, vous allez pouvoir analyser les statistiques de différents joueurs et nations pour dénicher les meilleurs talents. Voici quelques points de vue intéressants pour exploiter cet outil :")

# Séparation avec une ligne
st.markdown("---")

# Section 1: Le sélectionneur de nation
st.subheader("1. Explorez les talents de chaque nation 🌍")
col1, col2 = st.columns(2)
with col1:
    st.image("https://eliastorage.blob.core.windows.net/images/wc.png?sp=r&st=2024-12-04T23:33:10Z&se=2024-12-20T07:33:10Z&spr=https&sv=2022-11-02&sr=b&sig=WdpL3mi8JXfJDPSPBptE%2Bd55Pzya7og%2BNffjdLHIbFc%3D", caption="Image générée avec Copilot")
with col2 : 
    st.write("""
        🎯 **Objectif**
                
        - Trouver un joueur spécifique pour compléter une équipe nationale.

        🔎 **Comment ?**
        - Grâce à des filtres simples, vous pouvez sélectionner un pays et un poste précis. L'application vous fournira une liste de joueurs correspondant à ces critères, avec des statistiques détaillées comme la moyenne d'âge, la note OVR, et bien plus.

        💡 **Exemple pratique**
        - Le sélectionneur d’une équipe nationale peut rechercher des talents pour combler des postes clés dans l’équipe pour une compétition majeure comme la Coupe du Monde. 🏆
    """)

# Séparation avec une ligne
st.markdown("---")

# Section 3: Le joueur en comparaison
st.subheader("2. Trouvez le joueur qu'il vous faut 🎯")
col1, col2 = st.columns(2)
with col1:
    st.image("https://eliastorage.blob.core.windows.net/images/manager.png?sp=r&st=2024-12-04T23:32:27Z&se=2024-12-20T07:32:27Z&spr=https&sv=2022-11-02&sr=b&sig=HabO6S3oCTsiFZ00NUeAU%2F4tRdTqeFHx2mGJ9XX1GXw%3D", caption="Image générée avec Copilot")
with col2:
    st.write("""
        🎯 **Objectif**
        - Trouver des joueurs aux profils similiaires à un joueur donné et les comparer.

        🔍 **Comment ?**
        - En sélectionnant un joueur, l'algorithme de machine learning K-NN va retrouver les 5 joueurs se rapprochant le plus en terme de caractéristiques.

        💡 **Exemple pratique**
        - Trouver un joueur qui comblerait le départ de Kylian Mbappé au PSG avec des caractéristiques similaires
    """)

st.markdown("---")
st.write("⚡️ Développé avec Streamlit | Par Elias Ait Hassou")