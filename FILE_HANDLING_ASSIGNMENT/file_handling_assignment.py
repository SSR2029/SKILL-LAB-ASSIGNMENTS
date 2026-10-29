
# Create required text files

with open('document.txt', 'w') as file:
    file.write('Python is easy to learn and Python is useful.')

with open('data.txt', 'w') as file:
    file.write('old is a word. old is repeated.')

with open('reverse.txt', 'w') as file:
    file.write('Hello Python\nWelcome to Skill 60\nFile Handling')

with open('stats.txt', 'w') as file:
    file.write('Python is easy.\nPython is useful.\nI am learning Python.')


# 1. Counting Words in a File

def count_words():
    with open('document.txt', 'r') as file:
        content = file.read()
    return len(content.split())

print("1.", count_words())


# 2. Finding and Replacing Text

def replace_word():
    with open('data.txt', 'r') as file:
        content = file.read()

    content = content.replace('old', 'new')

    with open('data.txt', 'w') as file:
        file.write(content)

replace_word()
print("2. Text replaced")


# 3. Reading a File in Reverse

def reverse_file():
    with open('reverse.txt', 'r') as file:
        lines = file.readlines()

    for line in lines:
        print(line.strip()[::-1])

print("3.")
reverse_file()


# 4. Counting Lines, Words, and Characters

def count_stats():
    with open('stats.txt', 'r') as file:
        content = file.read()

    lines = content.splitlines()
    words = content.split()
    characters = len(content)

    return len(lines), len(words), characters

print("4.", count_stats())
