import redis

class BoundedCache:

    @staticmethod
    def stringify(bytes: bytes):
        return str(bytes)[2:-1]
    
    def __init__(self, redis, expiration) -> None:
        self.__expiration: int = expiration
        self.__redis: redis.Redis = redis

    def healthcheck(self) -> dict:
        pass

    """
    schema:
    'lvp':uid:ipv4:
    """
    def setLastVisitedPage(self, uid: str, ipv4: str, uri: str) -> dict:
        try:
            key = f"lvp:{uid}:{ipv4}"
            self.__redis.set(
                key,
                uri
            )
            _exp = self.__redis.expire(
                key,
                self.__expiration
            )
            return {
                'success': True,
                'expiresIn': self.__expiration,
            }
        except Exception as _err:
            return {
                'success': False
            }

    def getLastVisitedPage(self, segregation: str) -> dict:

        try:
            return {
                'data': BoundedCache.stringify(self.__redis.get(segregation)),
                'success': True
            }
        except Exception as _err:
            return {
                'data': None,
                'success': False
            }

