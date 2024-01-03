import redis

class UnboundedCache:
    def __init__(self, redis, expiration):
        self.__expiration: int = expiration
        self.__redis: redis.Redis = redis

    def healthcheck(self) -> dict:
        pass

    """
    schema:
    'c':cid
    """
    def setCardData(self, data: dict):
        pass
    def getCardData(self, data: dict):
        pass

    def unsetCardData(self, cid: str):
        pass



    """
    schema:
    'u':uid
    """
    def setUserData(self, data: dict):
        pass

    def getUserData(self, uid: str):
        pass

    def unsetUserData(self, uid: str):
        pass



    """
    schema:
    'sc':strip
    """
    def setSearchedCids(self, strip: str, cids: list):
        pass
    def getSearchedCids(self, strip: str):
        pass
    def unsetSearchedCids(self, strip: str):
        pass




    """
    schema:
    'su':strip
    """
    def setSearchedUids(self, strip: str, uids: list):
        pass
    def getSearchedUids(self, strip: str):
        pass

    def unsetSearchedUids(self, strip: str):
        pass