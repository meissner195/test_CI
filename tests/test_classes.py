import unittest
from my_module.my_function import MyImmutableClass, MyMutableClass, MyDerivedClass


class TestMyClasses(unittest.TestCase):
    def test_immutable_class(self):
        my_immutable_obj = MyImmutableClass(10)
        self.assertEqual(my_immutable_obj.value, 10)

        # Immutable objects should not be modifiable
        with self.assertRaises(AttributeError):
            my_immutable_obj.value = 20

    def test_mutable_class(self):
        my_mutable_obj = MyMutableClass()
        my_mutable_obj.add_item(1)
        my_mutable_obj.add_item(2)
        self.assertEqual(my_mutable_obj.get_items(), [1, 2])

    def test_virtual_class(self):
        my_derived_obj = MyDerivedClass()
        my_derived_obj.set_value(100)
        self.assertEqual(my_derived_obj.get_value(), 100)

if __name__ == '__main__':
    unittest.main()