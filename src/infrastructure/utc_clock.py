from datetime import datetime, UTC

from src.application.common.clock import Clock


class UTCClock(Clock):
    def __init__(self) -> None:
        self.tz = UTC

    def now(self) -> datetime:
        return datetime.now(self.tz)
