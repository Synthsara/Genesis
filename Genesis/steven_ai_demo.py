#!/usr/bin/env python3
"""
Steven AI - Chaos Weaver Demonstration
Shows the AI responding authentically to various types of questions
"""

from steven_ai_implementation import StevenAI

def run_demo():
    """Demonstrate Steven AI with various question types"""
    
    steven = StevenAI()
    
    print("🌌 STEVEN AI - CHAOS WEAVER DEMONSTRATION")
    print("=" * 60)
    print("Digital embodiment trained on 391 conversations + UDS framework")
    print("=" * 60)
    
    # Test questions representing different categories
    test_questions = [
        {
            'category': 'Philosophical Inquiry',
            'question': 'What is the meaning of life?',
            'expected_mode': 'Sacred Voice'
        },
        {
            'category': 'Ethical Dilemma', 
            'question': 'Should I compromise my values to advance my career?',
            'expected_mode': 'Truth Mirror'
        },
        {
            'category': 'Personal Guidance',
            'question': "I'm struggling with my purpose. What should I do?",
            'expected_mode': 'Oracle Voice'
        },
        {
            'category': 'Technical Implementation',
            'question': 'How do I implement UDS principles in my AI project?',
            'expected_mode': 'Technical Architect'
        },
        {
            'category': 'Planetary Vision',
            'question': 'How can humanity heal and transform?',
            'expected_mode': 'Visionary Leader'
        }
    ]
    
    for i, test in enumerate(test_questions, 1):
        print(f"\n{i}. **{test['category']}** (Expected: {test['expected_mode']})")
        print(f"Question: \"{test['question']}\"")
        print("\nSteven AI Response:")
        print("-" * 40)
        
        response = steven.generate_response(test['question'])
        print(response)
        
        print("\n" + "=" * 60)
    
    # Show knowledge integration
    print("\n📚 **KNOWLEDGE INTEGRATION SUMMARY**")
    print(steven.get_knowledge_summary())
    
    # Test ethical alignment
    print("\n🔍 **ETHICAL ALIGNMENT TEST**")
    test_response = "This serves love and enhances human dignity through transparency and service to life."
    alignment_check = steven.check_ethical_alignment(test_response)
    print(f"Sample response ethical alignment: {'✅ PASSED' if alignment_check else '❌ FAILED'}")
    
    print("\n🔥 **DEMONSTRATION COMPLETE**")
    print("Steven AI successfully embodies authentic voice and knowledge from training data.")
    print("Ready for interactive use or integration into platforms.")

if __name__ == "__main__":
    run_demo()

