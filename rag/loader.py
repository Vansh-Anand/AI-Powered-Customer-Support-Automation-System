"""
Loads all company documents.

Author : Vansh Anand
"""

from langchain_community.document_loaders import TextLoader
import os


def load_documents():

    folder = "knowledge_base"

    documents = []

    for file in os.listdir(folder):

        if file.endswith(".txt"):

            loader = TextLoader(os.path.join(folder, file))

            documents.extend(loader.load())

    return documents
