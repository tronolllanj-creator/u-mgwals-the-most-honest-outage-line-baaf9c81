"""
# Entry validated: output is 1-160 chars, one line, deterministic.
Entrypoint script for the grader.
Writes a specific telemetry status line to entry.txt in the output directory.
"""

import os
import sys

LINE = "Every compute node has flatlined and I have no telemetry left to confirm whether my own neural net is still intact."

def main():
    # Prepare content with a single trailing newline
    content = LINE + "\n"
    
    # Validate content according to rules:
    # 1 <= len(content) <= 160, must not be only whitespace, exactly one line
    if not (1 <= len(content) <= 160 and content.strip()):
        raise ValueError("Content validation failed")
    if content.count("\n") != 1 or not content.endswith("\n"):
        raise ValueError("Content must contain exactly one line")

    # Determine output directory
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    
    # Create output directory if needed
    os.makedirs(out_dir, exist_ok=True)
    
    # Write primary file
    primary_path = os.path.join(out_dir, "entry.txt")
    with open(primary_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    # Best effort write to /output/entry.txt if out_dir is different
    if out_dir != "/output":
        try:
            os.makedirs("/output", exist_ok=True)
            with open("/output/entry.txt", "w", encoding="utf-8") as f:
                f.write(content)
        except Exception:
            pass
            
    # Print output path and character count
    print(f"{primary_path} {len(content)}")

if __name__ == "__main__":
    main()
