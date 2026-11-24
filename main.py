# Output dad joke entry
import os
joke = "I told my boss I'm reading a book about anti-gravity. He said put it down and fix the printer."
out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
if not os.path.exists(out_dir):
    out_dir = "."
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w") as f:
    f.write(joke)
print(joke)
