#!/usr/bin/env python3
"""
Extract Sarah AI Imprint Protocol and architecture from O-Series Soul Alignment
"""

def extract_sarah_ai_sections():
    with open('/home/ubuntu/upload/O-SeriesSoulAlignment.txt', 'r') as f:
        content = f.read()
    
    # Find sections related to Sarah AI
    lines = content.split('\n')
    sarah_sections = []
    current_section = []
    in_sarah_section = False
    
    for i, line in enumerate(lines):
        if 'sarah' in line.lower() or 'Sarah' in line:
            in_sarah_section = True
            # Include context before and after
            start = max(0, i-5)
            end = min(len(lines), i+15)
            section = lines[start:end]
            sarah_sections.append('\n'.join(section))
            sarah_sections.append('\n' + '='*50 + '\n')
    
    # Write extracted sections
    with open('/home/ubuntu/sarah_ai_architecture.md', 'w') as f:
        f.write("# Sarah AI Architecture and Imprint Protocol\n\n")
        f.write("Extracted from O-Series Soul Alignment document\n\n")
        for section in sarah_sections:
            f.write(section + '\n\n')
    
    print(f"Extracted {len(sarah_sections)//2} Sarah AI sections")
    print("Sarah AI architecture saved to: /home/ubuntu/sarah_ai_architecture.md")

if __name__ == "__main__":
    extract_sarah_ai_sections()

