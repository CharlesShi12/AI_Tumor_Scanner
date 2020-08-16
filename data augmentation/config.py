from keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img

# specifies what features you want to change when generating new augmented images
datagen = ImageDataGenerator(
        rotation_range = 10,
        width_shift_range = 0.1,
        height_shift_range = 0.1,
        shear_range = 0.1,
        zoom_range = 0.1,
        horizontal_flip = True,
        fill_mode = 'nearest')

# augments each image in the has_tumor dataset
for j in range (1, 156):
    img = load_img(f'MRI_Scans/has_tumor/has_tumor_example_{str(j)}.jpg')
    x = img_to_array(img)
    x = x.reshape((1,) + x.shape)
    i = 0

    generated_data = datagen.flow(x, batch_size=1,
                                  save_to_dir='Augmented/has_tumor_augmented', save_prefix='has_tumor', save_format='jpg')
    for batch in generated_data:
        i += 1
        if i > 30:
            break

# augments each image in the has_tumor dataset
for j in range (1, 100):
    img = load_img(f'MRI_Scans/no_tumor/no_tumor_example_{str(j)}.jpg')
    x = img_to_array(img)
    x = x.reshape((1,) + x.shape)
    i = 0

    generated_data = datagen.flow(x, batch_size=1,
                                  save_to_dir='Augmented/no_tumor_augmented', save_prefix='no_tumor', save_format='jpeg')
    for batch in generated_data:
        i += 1
        if i > 45:
            break
