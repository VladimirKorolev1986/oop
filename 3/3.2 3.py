class ImageFileAcceptor:
    def __init__(self, extensions):
        self.extensions = extensions

    def __call__(self, file,  *args, **kwargs):
        if file.rsplit('.')[::-1][0] in self.extensions:
            return file


extensions = ('jpg', 'bmp', 'jpeg')
acceptor = ImageFileAcceptor(extensions)
filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.8.jpg", "forest.jpeg", "eq_1.png", "eq_2.png",
             "my.html", "data.shtml"]
image_filenames = filter(acceptor, filenames)

print(list(image_filenames))