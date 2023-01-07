import pandas as pd
import openai
import requests
import time
import random

key = 'YOUR KEY HERE'
openai.api_key = key

pool = ['James Joyce',
         'Jane Austen',
         'William Shakespeare',
         'Ernest Hemingway',
         'George Orwell',
         'Leo Tolstoy',
         'Charles Dickens',
         'J. K. Rowling',
         'Fyodor Dostoevsky',
         'Agatha Christie',
         'J. R. R. Tolkien',
         'C. S. Lewis',
         'F. Scott Fitzgerald',
         'Stephen King',
         'John Steinbeck',
         'Mark Twain',
         'Franz Kafka',
         'Virginia Woolf',
         'William Faulkner',
         'Herman Melville',
         'Jules Verne',
         'Edgar Allan Poe',
         'Toni Morrison',
         'Gabriel García Márquez',
         'Arthur Conan Doyle',
         'Neil Gaiman',
         'Miguel de Cervantes',
         'Hans Christian Andersen',
         'Alexandre Dumas',
         'Nora Roberts',
         'Oscar Wilde',
         'Lewis Carroll',
         'Nicholas Sparks',
         'Mary Shelley',
         'Dr. Seuss',
         'Hermann Hesse',
         'Mary Higgins Clark',
         'Anne Rice',
         'Geoffrey Chaucer',
         'Roald Dahl',
         'T. S. Eliot',
         'Margaret Atwood',
         'J. D. Salinger',
         'Jorge Luis Borges',
         'Emily Dickinson',
         'Maria Popova',
         'R. L. Stine',
         'Dante Alighieri',
         'George R. R. Martin',
         'Paulo Coelho']


def AuthorPicker(pool):
    return random.choice(pool)

def TextCreator(author, time):
    
    modified_prompt = "In the style of {}, tell me a fiction story that includes the time {}".format(author, time)

    x = openai.Completion.create(
      model="text-curie-001",
      prompt=modified_prompt,
      temperature=0.3,
        max_tokens =125
    )
    
    return x['choices'][0]['text']

def TextCleaner(text):
    return text.replace("\n","")

def Main(time, pool,author = ""):
    
    if author == "":
        author = AuthorPicker(pool)
    
    text = TextCreator(author, time)
    text = TextCleaner(text)
    
    return text, author, time
    
