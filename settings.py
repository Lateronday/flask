class BasicConfig:
    TEST = '1'
    DEBUG = True
    pass


class DevelopmentConfig(BasicConfig):
    pass


class TestConfig(BasicConfig):
    pass


class ProductConfig(BasicConfig):
    pass


config = {
    'development': DevelopmentConfig,
    'test': TestConfig,
    'product': ProductConfig
}
