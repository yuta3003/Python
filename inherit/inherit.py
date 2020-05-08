from mydir.inheritclass import *

person_suzuki = Customer("鈴木", 23, "mmm@nnn.nn.jp", "xxx-xxx-xxxx")
suzuki_name = person_suzuki.getName()
suzuki_age = person_suzuki.getAge()
suzuki_address = person_suzuki.getAddress()
suzuki_tell = person_suzuki.getTell()

print("{}さんの年齢:{}、住所:{}、電話番号:{}".format(suzuki_name, suzuki_age, suzuki_address, suzuki_tell))