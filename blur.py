from PIL import Image,ImageFilter

before = Image.open("test.jpg")
after = before.filter(ImageFilter.BoxBlur(10))
after.save("test-result.jpg")