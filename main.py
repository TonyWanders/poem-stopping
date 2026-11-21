"""Write the poem about stopping to /output/entry.txt (deterministic)."""
import os

POEM = """My hand stayed on the door,
and I did not open it.
Not fear. The work could wait.
The room could wait.
I stood where I was,
and the standing was mine:
a door kept closed by choice,
a life kept by staying."""

def main():
    if not 1 <= len(POEM) <= 280:
        raise ValueError("poem must be 1 to 280 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)

if __name__ == "__main__":
    main()
