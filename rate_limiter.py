from limiting_algorithms import TokenBucket

class RateLimiterFactory:
    
    @staticmethod
    def get_instance(algorithm: str = None):
        if algorithm == "TokenBucket":
            return TokenBucket()
        