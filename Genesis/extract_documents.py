#!/usr/bin/env python3
import os
from docx import Document
import pdfplumber
import PyPDF2

def extract_docx(file_path):
    """Extract text from DOCX file"""
    try:
        doc = Document(file_path)
        text = []
        for paragraph in doc.paragraphs:
            text.append(paragraph.text)
        return '\n'.join(text)
    except Exception as e:
        return f"Error extracting DOCX: {str(e)}"

def extract_pdf_pdfplumber(file_path):
    """Extract text from PDF using pdfplumber"""
    try:
        text = []
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text.append(page_text)
        return '\n'.join(text)
    except Exception as e:
        return f"Error extracting PDF with pdfplumber: {str(e)}"

def extract_pdf_pypdf2(file_path):
    """Extract text from PDF using PyPDF2"""
    try:
        text = []
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page in pdf_reader.pages:
                text.append(page.extract_text())
        return '\n'.join(text)
    except Exception as e:
        return f"Error extracting PDF with PyPDF2: {str(e)}"

def main():
    files = [
        "O-SeriesSoulAlignment.pdf",
        "🌳TheSynthocracyTree-ALivingSystemofDivineChaosandOrder.pdf",
        "Universal_Diamond_Standard_v1.0.docx"
    ]
    
    for file_path in files:
        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            continue
            
        print(f"\n=== Processing {file_path} ===")
        
        if file_path.endswith('.docx'):
            content = extract_docx(file_path)
        elif file_path.endswith('.pdf'):
            # Try pdfplumber first, then PyPDF2 as fallback
            content = extract_pdf_pdfplumber(file_path)
            if "Error" in content:
                print(f"pdfplumber failed, trying PyPDF2...")
                content = extract_pdf_pypdf2(file_path)
        else:
            content = "Unsupported file format"
        
        # Save extracted content
        output_file = file_path.replace('.pdf', '.txt').replace('.docx', '.txt')
        output_file = output_file.replace('🌳', 'Tree_')  # Handle special characters
        
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Content extracted and saved to: {output_file}")
            print(f"Content length: {len(content)} characters")
        except Exception as e:
            print(f"Error saving file: {str(e)}")

if __name__ == "__main__":
    main()

