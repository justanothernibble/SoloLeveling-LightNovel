from bs4 import BeautifulSoup
import sys
import os
import threading
import time
import requests

contentsDict = {}

def extract_chapter_content(i):    

    try:        
        response = requests.get(f'https://www.novelsonline.org/solo-leveling/chapter-{i}')
        soup = BeautifulSoup(response.text, 'html.parser')
        contentsDict[i] = soup
        # time.sleep(0.5)
    
    
    except Exception as e:
        print(f"\n⚠️ ERROR: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    start = time.time()
    threads = []
    for i in range(1,271):
        thread = threading.Thread(target=extract_chapter_content, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
        

    for i in range(1,271):
        print(f"Chapter {i}:")
        
        if not contentsDict[i]:
            raise Exception('❌ Chapter content container not found')
        
        # Enhanced filtering
        unwanted_strings = {
            'DevTools listening on ws://',
            'Your browser does not support JavaScript!',
            'WebGL has been deprecated'
        }

        paragraphs = []
        for p in contentsDict[i].find_all('p'):
            text = p.get_text(strip=True)
            if text and len(text) > 3:
                # Check against unwanted strings
                if not any(unwanted in text for unwanted in unwanted_strings):
                    paragraphs.append(text)

        if not paragraphs:
            raise Exception('❌ No readable text found in chapter content')

        for j in range(len(paragraphs)-1, 1, -1):
            # Delete paragraphs after "Note : Please download the sponsor's game to support us!" inclusive
            if paragraphs[j] == "Note : Please download the sponsor's game to support us!":
                del paragraphs[j:]
                break
            # Delete paragraphs after "< Chapter j > Fin." exclusive
            elif "< Chapter" in paragraphs[j] and "Fin." in paragraphs[j]:
                paragraphs = paragraphs[:j+1]
                break

        clean_output = "\n".join(paragraphs)
        print(clean_output.strip())
        chapters_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'chapters')
        # Define the file path for the specific chapter file
        file_path = os.path.join(chapters_dir, f'ch{i}.txt')
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(clean_output)

    end = time.time()
    print(f"\n⏱️ Time taken: {end - start:.2f} seconds")
    print("\n✅ Done!")
