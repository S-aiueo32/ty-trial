class Base:
    def f(self, x: int) -> int:
        return x

class Sub(Base):
    def f(self, x: str) -> int:
        return len(x)
