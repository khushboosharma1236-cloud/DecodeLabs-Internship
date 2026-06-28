import easyocr
print("Model load ho raha hai... pehli baar 20 sec lagega")

reader = easyocr.Reader(['en'])
result = reader.readtext('input.png', detail=0)
text = "\n".join(result)

with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(f"Input: input.png\n\nRecognized Text:\n{text}")

print("SUCCESS! output.txt ban gaya")
print("Text:", text)