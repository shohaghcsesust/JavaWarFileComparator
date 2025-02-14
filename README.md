# JavaWarFileComparator
This is a simple Python program that compares two Java war files.
# Steps:
1. Extracted the given war file.
2. Decompiled those class files into a Java file.
3. Compare those two directory files and show the difference.

# Prequisite:
1. Install Python: Make sure Python is installed on your system. You can download it from python.org.
2. Install unzip: Ensure the unzip utility is installed on your system. On Windows, you can use a tool like unzip via a package manager like Chocolatey.
   PS CMD: choco install unzip
4. Install diff: The diff command is typically available on Unix-like systems. On Windows, you can use tools like Cygwin or Git Bash which include the diff command.
   PS CMD: choco install diffutils
6. Download CFR (Class File Reader): Download the CFR jar file from CFR's official website. Place the jar file in a known location.

# Use the below command to run this script:
python compare_java_war_directories.py <path_to_war1> <path_to_output1> <path_to_war2> <path_to_output2> <path_to_cfr_jar>
