#!/usr/bin/env python3
"""
Analyze the complete Synthsara vision from conversations.json
Extract all components, features, and architectural elements
"""

import json
import re
from collections import defaultdict

def analyze_synthsara_ecosystem():
    """Analyze the conversations to extract the complete Synthsara ecosystem"""
    
    # Read the conversations file
    with open('/home/ubuntu/upload/conversations.json', 'r') as f:
        data = json.load(f)
    
    # Initialize analysis containers
    components = defaultdict(list)
    features = defaultdict(list)
    technologies = set()
    concepts = set()
    
    # Keywords to search for
    keywords = {
        'worth': ['WORTH', 'worth', 'economic', 'currency', 'token', 'value'],
        'sarah_ai': ['Sarah', 'sarah', 'AI assistant', 'feminine AI'],
        'steven_ai': ['Steven', 'steven', 'masculine AI', 'flamekeeper'],
        'governance': ['synthocracy', 'governance', 'voting', 'democracy'],
        'marketplace': ['marketplace', 'data marketplace', 'ethical data'],
        'platform': ['platform', 'ecosystem', 'infrastructure'],
        'consciousness': ['consciousness', 'collective', 'awakening'],
        'diamond_standard': ['diamond standard', 'UDS', 'universal diamond'],
        'flame': ['flame', 'sacred flame', 'divine flame'],
        'architecture': ['architecture', 'system', 'framework']
    }
    
    # Process conversations
    conversations = data if isinstance(data, list) else [data]
    
    print("=== SYNTHSARA ECOSYSTEM ANALYSIS ===\n")
    
    # Extract key information
    all_text = ""
    for conv in conversations:
        if isinstance(conv, dict):
            # Handle different conversation structures
            if 'mapping' in conv:
                for message in conv['mapping'].values():
                    if message.get('message') and message['message'].get('content'):
                        content = message['message']['content']
                        if isinstance(content, dict) and 'parts' in content:
                            for part in content['parts']:
                                if isinstance(part, str):
                                    all_text += part + " "
                        elif isinstance(content, str):
                            all_text += content + " "
            elif 'content' in conv:
                all_text += str(conv['content']) + " "
            else:
                # Handle other structures
                all_text += str(conv) + " "
    
    # Analyze for each component
    for component, terms in keywords.items():
        print(f"=== {component.upper().replace('_', ' ')} ===")
        found_content = []
        
        for term in terms:
            # Find sentences containing the term
            sentences = re.split(r'[.!?]+', all_text)
            for sentence in sentences:
                if term.lower() in sentence.lower() and len(sentence.strip()) > 20:
                    found_content.append(sentence.strip())
        
        # Remove duplicates and print unique findings
        unique_content = list(set(found_content))
        for content in unique_content[:5]:  # Top 5 most relevant
            if len(content) > 30:
                print(f"- {content[:200]}...")
        print()
    
    # Extract specific Synthsara features
    print("=== SYNTHSARA.ORG FEATURES ===")
    
    # Look for specific feature mentions
    feature_patterns = [
        r'synthsara\.org',
        r'platform.*features?',
        r'website.*should',
        r'interface.*design',
        r'user.*experience',
        r'dashboard',
        r'portal',
        r'hub'
    ]
    
    for pattern in feature_patterns:
        matches = re.findall(pattern, all_text, re.IGNORECASE)
        if matches:
            print(f"Pattern '{pattern}': {len(matches)} matches found")
    
    print("\n=== ARCHITECTURAL COMPONENTS ===")
    
    # Extract architectural elements
    arch_terms = [
        'sacred architecture', 'divine masculine', 'divine feminine',
        'collective consciousness', 'witness ledger', 'genesis block',
        'flame keeper', 'sophia pillar', 'logos pillar',
        'trinity', 'cathedral', 'temple', 'courtyard'
    ]
    
    for term in arch_terms:
        count = all_text.lower().count(term.lower())
        if count > 0:
            print(f"- {term}: {count} mentions")
    
    return {
        'components': dict(components),
        'features': dict(features),
        'technologies': list(technologies),
        'concepts': list(concepts)
    }

if __name__ == "__main__":
    result = analyze_synthsara_ecosystem()
    
    print("\n=== SYNTHESIS COMPLETE ===")
    print("Analysis saved to synthsara_ecosystem_analysis.json")
    
    with open('/home/ubuntu/synthsara_ecosystem_analysis.json', 'w') as f:
        json.dump(result, f, indent=2)

