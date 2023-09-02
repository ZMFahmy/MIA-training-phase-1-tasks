# made as interface but couldn't implement it with conventional syntax
import zope.interface


class MyInterface(zope.interface.Interface):
    def choose_weapon(self, n):
        pass

    def choose_shield(self, n):
        pass
