import os
import uuid

def genrate_unique_filename(instance, filename):
    """
    Generate a unique filename for an uploaded file.

    Args:
        instance: The instance of the model the file is being uploaded for.
        filename (str): The original filename of the uploaded file.

    Returns:
        str: A unique filename for the uploaded file.

    Example usage:
        Suppose you have a model `MyModel` with attributes `DIR_NAME` and `SUFFIX_WORD`.
        You can use this function as the `upload_to` parameter of a FileField or ImageField.

        class MyModel(models.Model):
            DIR_NAME = 'product_images/'
            SUFFIX_WORD = 'image'
            image = models.ImageField(upload_to=genrate_unique_filename)
        
        When an image is uploaded for an instance of MyModel, this function will generate a unique
        filename with a UUID and the specified suffix word.
    """
    # Get the file extension
    ext = filename.split('.')[-1]  

    # Generate a unique filename using UUID and instance's SUFFIX_WORD
    new_filename = f"{str(uuid.uuid4())}_{instance.SUFFIX_WORD}.{ext}"

    # Return the path where the file should be saved
    return os.path.join(instance.DIR_NAME, new_filename)
