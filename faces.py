def convert(emoji):
    emoji = emoji.replace(":)", "🙂")
    emoji = emoji.replace(":(", "🙁")
    return emoji

def main():
    user_input = input("Give me a :) if you're happy or a :( if you're sad: ")
    converted = convert(user_input)
    print(converted)

if __name__ == "__main__":
    main()
