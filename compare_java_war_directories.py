import os
import subprocess
import sys

def extract_war(war_path, extract_path):
    """Extracts a WAR file to a specified directory."""
    print(f"Extracting {war_path} to {extract_path}")
    os.makedirs(extract_path, exist_ok=True)
    subprocess.run(["unzip", "-o", war_path, "-d", extract_path], check=True)

def decompile_classes(src_dir, dest_dir, cfr_path):
    """Decompiles Java class files from a directory using CFR."""
    print(f"Decompiling classes from {src_dir} to {dest_dir}")
    os.makedirs(dest_dir, exist_ok=True)
    for root, dirs, files in os.walk(src_dir):
        # Make sure corresponding directories exist in the destination
        relative_path = os.path.relpath(root, src_dir)
        destination_dir = os.path.join(dest_dir, relative_path)
        os.makedirs(destination_dir, exist_ok=True)
        
        for file in files:
            if file.endswith(".class"):
                class_file = os.path.join(root, file)
                subprocess.run(["java", "-jar", cfr_path, class_file, "--outputdir", dest_dir], check=True)

def compare_directories(dir1, dir2):
    """Compares two directories using the diff command and returns the output."""
    print(f"Comparing directories {dir1} and {dir2}")
    result = subprocess.run(["diff", "-ru", dir1, dir2], capture_output=True, text=True)
    return result.stdout

def main(war1_path, output1_path, war2_path, output2_path, cfr_path):
    extract_path1 = output1_path+"\extract"
    extract_path2 = output2_path+"\extract"
    decompiled_path1 = output1_path+"\decompile"
    decompiled_path2 = output2_path+"\decompile"

    extract_war(war1_path, extract_path1)
    extract_war(war2_path, extract_path2)

    decompile_classes(os.path.join(extract_path1, "WEB-INF", "classes"), decompiled_path1, cfr_path)
    decompile_classes(os.path.join(extract_path2, "WEB-INF", "classes"), decompiled_path2, cfr_path)

    diff_output = compare_directories(decompiled_path1, decompiled_path2)
    
    if diff_output:
        print("Differences found:")
        print(diff_output)
    else:
        print("No differences found.")

if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage: python compare_java_war_directories.py <path_to_war1> <path_to_output1> <path_to_war2> <path_to_output2> <path_to_cfr_jar>")
        sys.exit(1)

    war1, out1, war2, out2, cfr_jar = sys.argv[1:6]
    main(war1, out1, war2, out2, cfr_jar)