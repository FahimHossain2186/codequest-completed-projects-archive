def spell_guessing_game():
    spells = {
        "Alohomora": "What's the name of the spell that unlocks doors?",
        "Crucio": "What's the name of the spell that causes immense pain?",
        "Stupefy": "What's the name of the spell that stuns your opponent?",
        "Nox": "What's the name of the spell that turns it off?",
        "Obliviate": "What's the name of the spell that erases someone's memory?",
        "Incendio": "What's the name of the spell that creates fire?",
        "Aguamenti": "Which one shoots out water?",
        "Accio": "What about the summoning spell?",
        "Piertotum Locomotor": "What about the spell that gives life to inanimate objects?",
        "Riddikulus": "Which spell transforms a Boggart into something humorous?",
    }

    total_guess_count = 0
    Pass = "pass"

    for secret_spell, question in spells.items():
        
        guess_count = 0
        max_guesses = 3
        print("\n" + question)

        while guess_count < max_guesses:
            guess = input("Your guess: ").strip().lower()
            total_guess_count += 1
            guess_count += 1

            if guess == secret_spell.lower():
                print(f"Correct! The spell is {secret_spell}.")
                break
            elif guess == Pass.lower():
                break
            else:
                print(f"Wrong! {max_guesses - guess_count} attempts left.")

        if guess == Pass.lower():
                print("Pass")
        elif guess != secret_spell.lower():
            print(f"Sorry! You've run out of attempts. The correct spell was {secret_spell}.")

    print("\nCongratulations! You have completed the wizarding quiz.")
    print(f"Total guesses made: {total_guess_count}")

# Start the game
spell_guessing_game()