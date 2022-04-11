class MethodExamples:
    def __init__(self):
        self.this_can_be_accessed_easily = "Hello"

    def get_this_can_be_accessed_easily(self):
        return self.this_can_be_accessed_easily

    def set_this_can_be_accessed_easily(self, value):
        self.this_can_be_accessed_easily = value


class Foo:
    @property
    def to_be_accessed(self):
        return 'Hello there', 'General Kenobi'


if __name__ == '__main__':
    f = Foo()
    print(f.to_be_accessed)
    f.to_be_accessed = "Hello there again"
