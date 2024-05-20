#!/usr/bin/python3
from base_model import BaseModel

class MyModel(BaseModel):
    """
    Sample model inheriting from BaseModel.
    """
    pass


def test_base_model():
    """
    Tests the functionality of the BaseModel class.
    """
    my_model = MyModel()
    my_model.save()

    # Test instance creation and ID generation
    assert isinstance(my_model.id, str)
    assert len(my_model.id) == 36  # UUID format

    # Test created_at and updated_at attributes (indirectly)
    assert isinstance(my_model.created_at, datetime)
    assert isinstance(my_model.updated_at, datetime)
    assert my_model.created_at <= my_model.updated_at  # Created before updated

    # Test to_dict method and updated_at type
    model_dict = my_model.to_dict()
    assert isinstance(model_dict['updated_at'], str)  # Ensure ISO format

    # Additional tests (optional):
    # - Test __str__ method output format
    # - Test custom attribute handling in to_dict

if __name__ == '__main__':
    test_base_model()
    print("All tests passed!")
