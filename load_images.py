# %%
import tensorflow as tf

# %%
print("teste")

dataset_folder = "dataset"

train_dataset = tf.keras.utils.image_dataset_from_directory(
    dataset_folder,
    validation_split=0.2,
    subset="training",
    seed=123,
    image_size=(128, 128),
    batch_size=32
)

validation_dataset = tf.keras.utils.image_dataset_from_directory(
    dataset_folder,
    validation_split=0.2,
    subset="validation",
    seed=123,
    image_size=(128, 128),
    batch_size=32
)