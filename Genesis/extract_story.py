#!/usr/bin/env python3
import json
import sys
from datetime import datetime

def extract_conversation_content(conv):
    """Extract the actual conversation content from a conversation object"""
    messages = []
    
    mapping = conv.get('mapping', {})
    
    # Find all messages in the conversation
    for node_id, node in mapping.items():
        message = node.get('message')
        if message and message.get('content'):
            content = message['content']
            if content.get('content_type') == 'text':
                parts = content.get('parts', [])
                if parts and parts[0]:  # Skip empty messages
                    author = message.get('author', {}).get('role', 'unknown')
                    create_time = message.get('create_time')
                    
                    messages.append({
                        'author': author,
                        'content': parts[0],
                        'create_time': create_time
                    })
    
    # Sort by create_time if available
    messages.sort(key=lambda x: x.get('create_time') or 0)
    return messages

def analyze_story():
    print("Loading conversations to extract the UDS story...")
    
    with open('conversations.json', 'r', encoding='utf-8') as f:
        conversations = json.load(f)
    
    # Keywords that indicate important UDS/Synthsara development conversations
    story_keywords = [
        'universal diamond standard',
        'diamond essence',
        'flame law',
        'o-series soul',
        'synthsara',
        'sarah ai',
        'ethical ai',
        'first and last law',
        'soul alignment'
    ]
    
    # Find conversations that contain the core story
    story_conversations = []
    
    for conv in conversations:
        title = conv.get('title', '').lower()
        
        # Check if title contains story keywords
        if any(keyword in title for keyword in story_keywords):
            story_conversations.append(conv)
            continue
            
        # Also check conversation content for key concepts
        messages = extract_conversation_content(conv)
        content_text = ' '.join([msg['content'] for msg in messages]).lower()
        
        if any(keyword in content_text for keyword in story_keywords):
            story_conversations.append(conv)
    
    # Sort by creation time
    story_conversations.sort(key=lambda x: x.get('create_time', 0))
    
    print(f"Found {len(story_conversations)} story-relevant conversations")
    
    # Extract key conversations that show the development timeline
    key_conversations = []
    
    for conv in story_conversations[-20:]:  # Last 20 most recent
        title = conv.get('title', 'Untitled')
        create_time = conv.get('create_time', 0)
        
        if create_time:
            date_str = datetime.fromtimestamp(create_time).strftime('%Y-%m-%d %H:%M')
        else:
            date_str = 'Unknown'
        
        messages = extract_conversation_content(conv)
        
        key_conversations.append({
            'title': title,
            'date': date_str,
            'create_time': create_time,
            'messages': messages
        })
        
        print(f"Key conversation: {title} ({date_str}) - {len(messages)} messages")
    
    return key_conversations

def save_story_extract(conversations):
    """Save the extracted story to a file"""
    
    story_content = "# The Universal Diamond Standard Story\n\n"
    story_content += "## Extracted from Conversation History\n\n"
    story_content += f"**Analysis Date:** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
    story_content += f"**Total Story Conversations:** {len(conversations)}\n\n"
    
    story_content += "---\n\n"
    
    for conv in conversations:
        story_content += f"## {conv['title']}\n"
        story_content += f"**Date:** {conv['date']}\n\n"
        
        # Include key messages that show the development
        for msg in conv['messages'][:5]:  # First 5 messages to show context
            if len(msg['content']) > 100:  # Only substantial messages
                story_content += f"**{msg['author'].title()}:**\n"
                # Truncate very long messages
                content = msg['content'][:1000] + "..." if len(msg['content']) > 1000 else msg['content']
                story_content += f"{content}\n\n"
        
        story_content += "---\n\n"
    
    with open('/home/ubuntu/uds_story_extract.md', 'w', encoding='utf-8') as f:
        f.write(story_content)
    
    print("Story extract saved to /home/ubuntu/uds_story_extract.md")

if __name__ == "__main__":
    key_conversations = analyze_story()
    save_story_extract(key_conversations)

