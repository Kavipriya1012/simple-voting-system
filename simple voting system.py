# Function to display the voting options and take votes
def voting_system():
    # List of candidates
    candidates = ["Alice", "Bob", "Charlie"]

    # Dictionary to store the votes for each candidate
    votes = {candidate: 0 for candidate in candidates}

    print("Welcome to the Voting System!")
    print("Candidates:")
    for idx, candidate in enumerate(candidates, 1):
        print(f"{idx}. {candidate}")

    # Allow users to vote
    while True:
        try:
            vote = int(input("Enter the number of the candidate you want to vote for (1, 2, or 3): "))
            if vote < 1 or vote > len(candidates):
                print("Invalid choice. Please enter a number between 1 and 3.")
            else:
                # Increment the vote for the selected candidate
                votes[candidates[vote - 1]] += 1
                print(f"Thank you for voting for {candidates[vote - 1]}!")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Display the final vote counts
    print("\nVoting Results:")
    for candidate, vote_count in votes.items():
        print(f"{candidate}: {vote_count} vote(s)")

# Run the voting system
voting_system()

