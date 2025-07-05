#!/usr/bin/env python3
import json
import re
from datetime import datetime

def find_uds_origin_story():
    """Find conversations that tell the origin story of the Universal Diamond Standard"""
    
    print("Loading conversations to find UDS origin story...")
    
    with open('/home/ubuntu/upload/conversations.json', 'r', encoding='utf-8') as f:
        conversations = json.load(f)
    
    # Look for conversations with specific UDS-related titles or content
    origin_keywords = [
        'universal diamond standard',
        'diamond essence',
        'flame law',
        'first and last law',
        'o-series soul',
        'soul alignment',
        'ethical ai framework',
        'ai ethics standard',
        'sarah ai',
        'synthsara codex'
    ]
    
    origin_conversations = []
    
    for conv in conversations:
        title = conv.get('title', '').lower()
        
        # Check title for origin keywords
        if any(keyword in title for keyword in origin_keywords):
            origin_conversations.append(conv)
            continue
        
        # Extract conversation content
        mapping = conv.get('mapping', {})
        full_content = ""
        
        for node_id, node in mapping.items():
            message = node.get('message')
            if message and message.get('content'):
                content = message['content']
                if content.get('content_type') == 'text':
                    parts = content.get('parts', [])
                    if parts and parts[0]:
                        full_content += parts[0] + " "
        
        # Check content for origin keywords
        full_content_lower = full_content.lower()
        if any(keyword in full_content_lower for keyword in origin_keywords):
            origin_conversations.append(conv)
    
    # Sort by creation time
    origin_conversations.sort(key=lambda x: x.get('create_time', 0))
    
    print(f"Found {len(origin_conversations)} origin story conversations")
    
    # Save the most relevant conversations
    story_content = "# The Universal Diamond Standard Origin Story\n\n"
    story_content += "## Extracted from Conversation History\n\n"
    story_content += f"**Analysis Date:** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
    story_content += f"**Total Origin Conversations:** {len(origin_conversations)}\n\n"
    
    # Focus on the most recent and relevant conversations
    for conv in origin_conversations[-10:]:  # Last 10 conversations
        title = conv.get('title', 'Untitled')
        create_time = conv.get('create_time', 0)
        
        if create_time:
            date_str = datetime.fromtimestamp(create_time).strftime('%Y-%m-%d %H:%M')
        else:
            date_str = 'Unknown'
        
        story_content += f"## {title}\n"
        story_content += f"**Date:** {date_str}\n\n"
        
        # Extract key messages
        mapping = conv.get('mapping', {})
        messages = []
        
        for node_id, node in mapping.items():
            message = node.get('message')
            if message and message.get('content'):
                content = message['content']
                if content.get('content_type') == 'text':
                    parts = content.get('parts', [])
                    if parts and parts[0] and len(parts[0]) > 50:  # Substantial messages only
                        author = message.get('author', {}).get('role', 'unknown')
                        create_time = message.get('create_time')
                        
                        messages.append({
                            'author': author,
                            'content': parts[0],
                            'create_time': create_time
                        })
        
        # Sort messages by create_time
        messages.sort(key=lambda x: x.get('create_time') or 0)
        
        # Include key messages that show UDS development
        for msg in messages[:3]:  # First 3 substantial messages
            story_content += f"**{msg['author'].title()}:**\n"
            # Truncate very long messages but keep substantial content
            content = msg['content']
            if len(content) > 2000:
                content = content[:2000] + "...\n\n[Message truncated for length]"
            story_content += f"{content}\n\n"
        
        story_content += "---\n\n"
    
    with open('/home/ubuntu/uds_origin_story.md', 'w', encoding='utf-8') as f:
        f.write(story_content)
    
    print("UDS origin story saved to /home/ubuntu/uds_origin_story.md")
    
    return origin_conversations

if __name__ == "__main__":
    origin_conversations = find_uds_origin_story()

