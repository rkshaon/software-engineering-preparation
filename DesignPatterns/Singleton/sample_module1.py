# sample_module1.py
import example_singleton as singleton

print(singleton.shared_variable)
singleton.shared_variable += "(modified by samplemodule1)"
