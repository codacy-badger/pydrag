from typing import Optional, List

from attr import attrs

from pyfm import BaseModel


@attrs(auto_attribs=True)
class Attributes(BaseModel):
    to: str = None
    tag: str = None
    uts: str = None
    rank: str = None
    date: str = None
    page: int = None
    user: str = None
    country: str = None
    from_date: str = None
    total: int = None
    offset: int = None
    num_res: int = None
    artist: str = None
    perPage: int = None
    totalPages: int = None


@attrs(auto_attribs=True)
class Image(BaseModel):
    size: str
    text: Optional[str] = None


@attrs(auto_attribs=True)
class Date(BaseModel):
    unixtime: int
    text: str


@attrs(auto_attribs=True)
class DateUTS(BaseModel):
    uts: str
    text: str


@attrs(auto_attribs=True)
class Artist(BaseModel):
    mbid: str = None
    name: str = None
    text: str = None
    url: str = None
    tagcount: int = None
    listeners: int = None
    playcount: int = None
    streamable: str = None
    image: List[Image] = None
    attr: Attributes = None


@attrs(auto_attribs=True)
class Track(BaseModel):
    name: str
    mbid: str
    url: str
    artist: Artist
    image: List[Image]
    playcount: int = None
    listeners: int = None
    streamable: str = None  # super buggy
    duration: str = None
    attr: Attributes = None


@attrs(auto_attribs=True)
class Album(BaseModel):
    mbid: str
    text: str = None
    name: str = None
    playcount: int = None
    url: str = None
    artist: Artist = None
    attr: Attributes = None
    image: List[Image] = None


@attrs(auto_attribs=True)
class Chart(BaseModel):
    text: str
    from_date: str
    to: str