import openai
import time

openai.api_key = "api key goes here"

def generate_love_story(characters, ages, story_type, detail_level):
    prompt = (f"Write a {detail_level} love story about {characters[0]['name']} and {characters[1]['name']}. "
              f"{characters[0]['name']} is {ages[0]} years old and {characters[1]['name']} is {ages[1]} years old. "
              f"{characters[0]['name']} is {characters[0]['description']} and goes by {characters[0]['pronoun']} "
              f"pronouns. {characters[1]['name']} is {characters[1]['description']} and goes by {characters[1]['pronoun']} "
              f"pronouns. {characters[0]['name']} likes {characters[0]['likes']} and {characters[1]['name']} likes {characters[1]['likes']}. "
              f"This is a {story_type} love story." )

    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.7,
        max_tokens=2048,
        n=1,
        stop=None,
        timeout=60,
    )

    message = completions.choices[0].text
    return message.strip()

def get_character_info():
    characters = []
    for i in range(2):
        name = input(f"Enter character {i+1}'s name: ")
        age = input(f"Enter character {i+1}'s age: ")
        pronoun = input(f"Enter character {i+1}'s pronoun (he/she/they): ")
        likes = input(f"Enter character {i+1}'s likes: ")
        description = input(f"Enter character {i+1}'s description: ")

        character = {
            "name": name,
            "age": age,
            "pronoun": pronoun,
            "likes": likes,
            "description": description,
        }
        characters.append(character)

    return characters


def main():
    characters = get_character_info()
    ages = [characters[i]['age'] for i in range(2)]
    story_type = input("What type of love story do you want (e.g. romantic, dramatic, comedic)? ")
    detail_level = input("How much detail do you want in the story (e.g. short, medium, long)? ")
    print("Generating love story...")
    story = generate_love_story(characters, ages, story_type, detail_level)
    print(story)

if __name__ == "__main__":
    main()
