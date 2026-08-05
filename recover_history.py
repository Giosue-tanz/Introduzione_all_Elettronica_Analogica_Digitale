import json
import os

conversations = [
    "f7699589-ff0a-4ed4-9b3e-e49b043eb488",
    "28351c3a-70fb-4a9e-ad9d-6915960fa1ed",
    "3a4a3d7f-a6de-4a2d-8de5-fcdb73e340b9"
]

output_dir = "/home/giosue/Scrivania/Elettronica digitale"

def apply_replace(target_file, target_content, replacement_content):
    path = os.path.join(output_dir, target_file)
    if not os.path.exists(path):
        return False
    with open(path, "r") as f:
        content = f.read()
    
    if target_content in content:
        content = content.replace(target_content, replacement_content)
        with open(path, "w") as f:
            f.write(content)
        return True
    return False

for conv in conversations:
    log_path = f"/home/giosue/.gemini/antigravity/brain/{conv}/.system_generated/logs/transcript_full.jsonl"
    if not os.path.exists(log_path):
        continue
        
    print(f"Replaying {conv}...")
    with open(log_path, "r") as f:
        for line in f:
            try:
                data = json.loads(line)
            except:
                continue
                
            for call in data.get("tool_calls", []):
                name = call.get("name", "")
                args = call.get("args", {})
                
                if name == "write_to_file":
                    target_file = args.get("TargetFile", "")
                    if target_file.startswith("/home/giosue"):
                        target_file = os.path.basename(target_file)
                    code_content = args.get("CodeContent", "")
                    if target_file and code_content:
                        with open(os.path.join(output_dir, target_file), "w") as out:
                            out.write(code_content)
                        print(f"Recovered {target_file}")
                
                elif name == "replace_file_content":
                    target_file = args.get("TargetFile", "")
                    if target_file.startswith("/home/giosue"):
                        target_file = os.path.basename(target_file)
                    tc = args.get("TargetContent", "")
                    rc = args.get("ReplacementContent", "")
                    if target_file and tc:
                        success = apply_replace(target_file, tc, rc)
                        if success:
                            print(f"Applied replace to {target_file}")
                        else:
                            print(f"Failed to apply replace to {target_file}")
                            
                elif name == "multi_replace_file_content":
                    target_file = args.get("TargetFile", "")
                    if target_file.startswith("/home/giosue"):
                        target_file = os.path.basename(target_file)
                    chunks = args.get("ReplacementChunks", [])
                    for chunk in chunks:
                        tc = chunk.get("TargetContent", "")
                        rc = chunk.get("ReplacementContent", "")
                        if target_file and tc:
                            success = apply_replace(target_file, tc, rc)
                            if success:
                                print(f"Applied multi_replace to {target_file}")
                            else:
                                print(f"Failed to apply multi_replace to {target_file}")
                
                elif name == "run_command":
                    cmd = args.get("CommandLine", "")
                    # execute python scripts if they were generated
                    if cmd.startswith("python3 append") or cmd.startswith("python3 fix") or cmd.startswith("python3 insert"):
                        print(f"Executing: {cmd}")
                        os.system(f"cd '{output_dir}' && {cmd}")
                        