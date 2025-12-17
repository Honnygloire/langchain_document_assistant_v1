# LangChain – Document Assistant (V1)

Mini-projet de découverte de **LangChain**.

---

## Objectif

Ce projet illustre la mécanique de **LangChain** à travers un exemple simple :  
poser une question sur un document texte et obtenir une réponse générée par un modèle de langage (LLM).  

Pour éviter les contraintes liées aux API externes (clé OpenAI, quotas, facturation), j’ai choisi d’utiliser un **faux LLM** simulé.  
Cela permet de démontrer la structure et le fonctionnement de LangChain sans dépendances externes.

---

## Structure du projet

```bash
langchain/
├── data.txt #Document texte à interroger
├── main.py #Script principal avec la logique LangChain
└── README.md #Documentation du projet
```


---

## Installation

1. **Cloner le repo**
   ```bash
   git clone https://github.com/<ton-user>/langchain-document-assistant-v1.git
   cd langchain-document-assistant-v1
2. **Installer les dépedances*
pip install -r requirements.txt


## Explication des choix

Faux LLM (faux_llm) : J’ai choisi de simuler un modèle de langage pour éviter les problèmes de quota ou de clé API. Cela permet de se concentrer sur la mécanique de LangChain.

RunnableLambda : Sert à transformer une fonction Python en “runnable” compatible avec LangChain. Ici, il encapsule faux_llm pour l’utiliser comme un LLM.

PromptTemplate : Définit un gabarit de prompt avec deux variables (context, question). Ce choix permet de séparer la logique du prompt des données injectées.

Chaîne (prompt | llm) : J’ai utilisé l’opérateur | pour relier le prompt au LLM. Ce pipeline illustre la philosophie de LangChain : composer des briques modulaires.

invoke() : Méthode moderne pour exécuter la chaîne avec des données concrètes. J’ai choisi invoke plutôt que run car run est déprécié dans les versions récentes.

## Exécution

Lancer le script :
```bash 
python3 main.py
```
Exemple de sortie :
```bash 
LangChain permet de structurer l'utilisation des modèles de langage.
```