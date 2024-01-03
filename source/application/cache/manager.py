import redis
from declarations.bounded import BoundedCache
from declarations.unbounded import UnboundedCache


class CacheManager:
    
    bounded: BoundedCache
    unbounded: UnboundedCache


    """
    dict schema:
    host: str
    port: int
    password: str
    expiration: int
    id: int
    """
    def __init__(
        self,
        databasesConfig,
    ) -> None:

        # try:
        #     self.unbounded = UnboundedCache(redis.Redis(
        #         host=databasesConfig['unbounded'].host,
        #         port=int(databasesConfig['unbounded'].port),
        #         db=databasesConfig['unbounded'].id,
        #         password=databasesConfig['unbounded'].password,
        #         charset='utf-8',
        #         errors='strict'
        #     ), databasesConfig['unbounded'].expiration)
        # except Exception as _err:
        #     print(_err)

        try:

            self.bounded = BoundedCache(redis.Redis(
                host=databasesConfig['bounded']['host'],
                port=int(databasesConfig['bounded']['port']),
                db=databasesConfig['bounded']['id'],
                password=databasesConfig['bounded']['password'],
                charset='utf-8',
                errors='strict'
            ), databasesConfig['bounded']['expiration'])
        except Exception as _err:
            print(_err)




    def globalHealthckeck(self):
        pass

    def __delattr__(self, __name: str) -> None:
        if __name in self.__dir__(): return

# Testing dataset
config = {
    'bounded': {
        'host': 'localhost',
        'port': 6379,
        'id': 0,
        'password': '&fgyHAS8FD',
        'expiration': 60
    }
}

cm = CacheManager(config)
print(cm.bounded.setLastVisitedPage('124144325', '123.54.7.8', 'user/7657658'))
print(cm.bounded.getLastVisitedPage('lvp:124144325:123.54.7.8')['data'])