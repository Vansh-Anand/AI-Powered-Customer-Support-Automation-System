from rag.rag_pipeline import retrieve_context

query = "Tell me about pricing plans."

context = retrieve_context(query)

print("="*60)

print("Retrieved Context\n")

print(context)
