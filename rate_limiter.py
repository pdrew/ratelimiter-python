from limiting_algorithms import TokenBucket, FixedCounterWindow, SlidingWindow

class RateLimiterFactory:
    
    @staticmethod
    def get_instance(algorithm: str = None):
        if algorithm == "TokenBucket":
            return TokenBucket()
        if algorithm == "FixedCounterWindow":
            return FixedCounterWindow()
        if algorithm == "SlidingWindow":
            return SlidingWindow()
        