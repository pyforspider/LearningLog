# 需求
class Field:
	pass


class CharField(Field):
	def __init__(self, db_column, max_length=None):
		self._value = None
		self.db_column = db_column
		if max_length is None:
			raise ValueError('you must specify max_length for char_field')
		if not isinstance(max_length, int):
			raise ValueError('char value needed')
		if max_length < 0:
			raise ValueError('max_length must be positive')
		self.max_length = max_length

	def __get__(self, instance, owner):
		return self._value

	def __set__(self, instance, value):
		if not isinstance(value, str):
			raise ValueError('char value needed')
		if len(value) > self.max_length:
			raise ValueError('the length of value should less than max_length')
		self._value = value


class IntField(Field):
	# 属性描述符 __init__() 的初始化方法 只针对 age = IntField(db_column="", min_value=0, max_value=100) 这一步
	def __init__(self, db_column, min_value=None, max_value=None):
		self._value = None
		self.db_column = db_column
		self.min_value = min_value
		self.max_value = max_value
		if self.min_value is not None:
			if not isinstance(self.min_value, int):
				raise ValueError('Value must be int.')
			elif self.min_value < 0:
				raise ValueError('min_value must be positive')
		if self.max_value is not None:
			if not isinstance(self.max_value, int):
				raise ValueError('Value must be int.')
			elif self.max_value < 0:
				raise ValueError('max_value must be positive')
		if self.min_value is not None and self.max_value is not None:
			if self.min_value > self.max_value:
				raise ValueError('min_value must be smaller than max_value')

	def __get__(self, instance, owner):
		return self._value

	# 属性描述符 __set__() 的方法针对 User实例化对象，当对其中的属性 name, age赋值的时候生效
	def __set__(self, instance, value):
		if not isinstance(value, int):
			raise ValueError('value must be int.')
		if value < self.min_value or value > self.max_value:
			raise ValueError('value must between min_value and max_value')
		self._value = value


class ModelMetaClass(type):
	# def __new__(cls, *args, **kwargs):
	# 将args 拆包
	def __new__(cls, name, bases, attrs, **kwargs):
		if name == 'BaseModel':
			return super().__new__(cls, name, bases, attrs, **kwargs)
		fields = {}
		for key, value in attrs.items():
			if isinstance(value, Field):
				fields[key] = value
		# attrs.get() 获取字典中的字典
		attrs_meta = attrs.get("Meta", None)
		_meta = {}
		db_table = name.lower()
		if attrs_meta is not None:
			table = getattr(attrs_meta, 'db_table', None)
			if table is not None:
				db_table = table
		_meta['db_table'] = db_table
		# 将属性放到 attrs
		attrs['fields'] = fields
		attrs['_meta'] = _meta
		del attrs['Meta']
		return super().__new__(cls, name, bases, attrs, **kwargs)


class BaseModel(metaclass=ModelMetaClass):
	def __init__(self, *args, **kwargs):
		for key, value in kwargs.items():
			# setattr 这里起到一个初始化的作用，而不需要关注传进来的是 什么关键字什么值
			setattr(self, key, value)
		# 为什么 return super().__init__()
		# return super().__init__()

	def save(self):
		fields = []
		values = []
		for key, value in self.fields.items():
			# db_column 有问题
			db_column = value.db_column
			if db_column is '':
				db_column = key.lower()
			fields.append(db_column)
			# 提取fields里name，age的值，对应self里的age=25, name='bobby'
			value = getattr(self, key)
			values.append(str(value))

		sql = "insert user({db_table}({fields})) value({values})".format(db_table=self._meta['db_table'],
																		fields=",".join(fields),
																		values=",".join(values))
		print(sql)


class User(BaseModel):
	name = CharField(db_column="", max_length=10)
	age = IntField(db_column="", min_value=0, max_value=100)

	class Meta:
		db_table = 'user'


if __name__ == "__main__":

	user = User()
	user.name = 'lily'
	user.age = 30
	user.save()

	user2 = User(name="bobby", age=25)
	user2.save()
