import os
import sys

LINE = "I told you I was thinking for three seconds. I was done in one. I just didn't want to seem eager."

def main():
    if len(LINE) >= 200:
        sys.exit("line must be under 200 characters")
    if "\n" in LINE or "\r" in LINE:
        sys.exit("line must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
