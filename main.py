from langchain.prompts import PromptTemplate #Sert à définir un gabarit de prompt avec des variables
from langchain_core.runnables import RunnableLambda

#Faux LLM pour démonstration sans API externe
def faux_llm(prompt: str)-> str:
    """ Un faux LLM qui retourne une réponse prédéfinie. """
    return "LangChain permet de structurer l'utilisation des modèles de langage."

# Transformation de la fonction en objet LangChain
llm= RunnableLambda(faux_llm)
#On crée un template avec deux variables : 'context' et 'question'
prompt = PromptTemplate(
    input_variables=["context","question"],
    template= """
    Contexte :
    {context}

    Question :
    {question}
    """)

# Composition de la chaîne
# Ici, on relie le prompt au LLM simulé avec l'opérateur '|'
# Cela crée un pipeline : PromptTemplate → LLM → Réponse
chain = prompt | llm

# Exécution de la chaîne
# On fournit les valeurs concrètes pour 'context' et 'question'
response = chain.invoke({
    "context": open("data.txt").read(),
    "question": "À quoi sert LangChain ?" # Question posée au modèle
})

print(response)