# import base64

# # Your encoded data
# encoded_data = "9JhbCciOUIUzIINiinR5CCIGIkpXVCJ9.4YJObztlblt90eXBNjoiyWMNIZXNziwiZXiwjoxNzQwNjcyNDkxLCJPYXQIOE3MzgwODAOOTESimpOsS6GImY5ODdYmQwNCMYTQONGYSZGMYiVzZMmZIMihiYTBiiwidxMid9pZCIGOHODFTKbS6bcNF"

# # Try to decode
# try:
#     # Fix potential formatting issues
#     cleaned_data = encoded_data.replace(' ', '+')
    
#     # Add padding if needed
#     padding = 4 - len(cleaned_data) % 4
#     if padding != 4:
#         cleaned_data += '=' * padding
    
#     decoded_bytes = base64.b64decode(cleaned_data)
#     decoded_text = decoded_bytes.decode('utf-8')
#     print("Decoded text:", decoded_text)
# except Exception as e:
#     print(f"Error decoding: {e}")