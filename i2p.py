import img2pdf
from PIL import Image

try:
    # with open("test.pdf", "wb") as f:
    #     f.write(img2pdf.convert('test.jpg'))
    #     print('PDF created')
    file = 'E:/SPSS 19/test.jpg'
    im = Image.open(file)
    new_file = 'E:/SPSS 19/test1.pdf'
    im.save(new_file)
    print("PDF created successfully")

except Exception as e:
    print(e)