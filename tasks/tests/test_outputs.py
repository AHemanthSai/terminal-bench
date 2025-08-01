import os
import filecmp

def test_cleaned_logs_exist():
    assert os.path.exists("cleaned/app.log"), "cleaned/app.log was not created"

def test_blank_and_duplicates_removed():
    cleaned_file = "cleaned/app.log"
    with open(cleaned_file, "r") as f:
        lines = f.read().splitlines()

    assert "" not in lines, "Blank lines were not removed"
    assert len(lines) == len(set(lines)), "Duplicate lines were not removed"

def test_correct_output():
    with open("cleaned/app.log", "r") as out:
        output = out.read().strip()

    expected = """ERROR: Disk full
WARNING: High memory usage
INFO: Backup completed"""
    
    assert output == expected, "Cleaned output does not match expected result"
