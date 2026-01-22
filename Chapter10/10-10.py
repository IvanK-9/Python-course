# ============================================================
# EXERCISE 10-10: COMMON WORDS
# ============================================================
print("\n\n" + "="*60)
print("EXERCISE 10-10: COMMON WORDS")
print("="*60)

# Create a test file
with open('sample_text.txt', 'w', encoding='utf-8') as file:
    file.write("""The moon was drifting over waves,
Drifting soft and slow;
A Lantern and a Ladder
Strolled where starfish often go.
They sighed to see the tangled weeds
That swayed in lines below.
“If only all this knotted green,”
They mused, “could cease to grow!”
“The hour is right,” the Lantern said,
“To ponder many things:
Of clocks that hum at half-past one,
Of birds that walk with strings,
Of how a whisper turns to wind
And why the ocean sings.”
The Ladder leaned against the breeze
And nodded in the night:
“It seems a curious world indeed—
But curious feels just right.”
""")

try:
    with open('sample_text.txt', encoding='utf-8') as file:
        contents = file.read()
    
    # Count the word 'the'
    contents_lower = contents.lower()
    count = contents_lower.count('the')
    
    print(f"\n📊 The word 'the' appears {count} time(s) in the file.")
    print(f"\nFirst 200 characters of text:")
    print(contents[:200] + "...")
    
except FileNotFoundError:
    print("\n⚠️ File not found.")


print("\n\n" + "="*60)
print("ALL EXERCISES COMPLETED!")
print("="*60)