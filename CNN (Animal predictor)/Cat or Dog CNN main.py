from compiler import *

inp=input('Image path : ')

test_image = image.load_img(inp, target_size = (64,64))
test_image = image.image_to_array(test_image)
test_image = np.expand_dims(test_image, axis=0)

res = classifier.predict(test_image)

print(training_setclass_indices)

if res[0][0] == 1:
    print('Dog')
else:
    print('Cat')
