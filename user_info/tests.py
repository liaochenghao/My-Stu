from django.test import TestCase
import time
# Create your tests here.
start = time.time()
time.sleep(2)
end = time.time()
print((end-start)/60)


hello = 'http://bobowang'
data = hello.replace('http','https')
print(data)